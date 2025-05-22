#!/usr/bin/env python3
"""Simple Tableau to Power BI converter.

This tool reads a Tableau workbook (.twb or .twbx) and outputs a minimal
representation of a Power BI dataset as JSON. It is not a full fidelity
converter but demonstrates how workbook elements could be extracted and
mapped to Power BI concepts.
"""

import argparse
import json
import os
import xml.etree.ElementTree as ET
import zipfile


def load_twb(path: str) -> ET.ElementTree:
    """Load a TWB XML from either a .twb file or inside a .twbx archive."""
    if path.endswith('.twbx'):
        with zipfile.ZipFile(path, 'r') as z:
            # assume the workbook file is the first .twb in archive
            twb_name = next((n for n in z.namelist() if n.endswith('.twb')), None)
            if not twb_name:
                raise ValueError('No .twb file found in archive')
            with z.open(twb_name) as f:
                return ET.parse(f)
    else:
        return ET.parse(path)


def parse_workbook(tree: ET.ElementTree) -> dict:
    root = tree.getroot()
    # Get workbook name
    workbook_name = root.get('name', 'TableauWorkbook')
    # Datasources
    datasources = []
    for ds in root.findall('.//datasource'):
        ds_name = ds.get('name')
        if ds_name:
            datasources.append(ds_name)
    # Worksheets
    worksheets = []
    for ws in root.findall('.//worksheet'):
        ws_name = ws.get('name')
        if ws_name:
            worksheets.append(ws_name)
    return {
        'workbookName': workbook_name,
        'datasources': datasources,
        'worksheets': worksheets,
    }


def convert_to_powerbi(parsed: dict) -> dict:
    """Map parsed Tableau info to a very simple Power BI dataset structure."""
    dataset = {
        'datasetName': parsed['workbookName'],
        'tables': [
            {'name': ws, 'columns': []} for ws in parsed['worksheets']
        ],
        'datasources': parsed['datasources'],
    }
    return dataset


def main():
    parser = argparse.ArgumentParser(description='Convert Tableau workbook to a Power BI dataset definition.')
    parser.add_argument('workbook', help='Path to .twb or .twbx file')
    parser.add_argument('-o', '--output', default='powerbi-dataset.json', help='Output JSON file path')
    args = parser.parse_args()

    if not os.path.exists(args.workbook):
        raise SystemExit(f'Workbook {args.workbook} not found')

    tree = load_twb(args.workbook)
    parsed = parse_workbook(tree)
    dataset = convert_to_powerbi(parsed)

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2)

    print(f'Power BI dataset definition written to {args.output}')


if __name__ == '__main__':
    main()
