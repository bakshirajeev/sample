import React, { useEffect, useState } from 'react';
import { Container, Typography, List, ListItem, ListItemText } from '@mui/material';

export default function DepartmentList() {
  const [departments, setDepartments] = useState([]);

  useEffect(() => {
    fetch('/api/departments/')
      .then((res) => res.json())
      .then(setDepartments)
      .catch(console.error);
  }, []);

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>Departments</Typography>
      <List>
        {departments.map((dept) => (
          <ListItem key={dept.id}>
            <ListItemText primary={dept.name} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
}
