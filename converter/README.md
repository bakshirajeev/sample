# Tableau to Power BI Converter

This folder contains a simple command line tool that demonstrates how a Tableau
workbook can be converted into a minimal Power BI dataset definition. The tool
parses the workbook XML and produces a JSON file that lists worksheets and data
sources as Power BI tables.

This is **not** a full fidelity converter to the PBIX format but serves as a
starting point for automating migrations.

## Usage

```bash
python3 tableau_to_powerbi.py <workbook.twbx or workbook.twb> [-o output.json]
```

The resulting JSON file can be inspected or further transformed into a PBIX
using the Power BI APIs.
