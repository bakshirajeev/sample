import React, { useEffect, useState } from 'react';
import { Container, Typography, List, ListItem, ListItemText } from '@mui/material';

export default function EmployeeList() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    fetch('/api/employees/')
      .then((res) => res.json())
      .then(setEmployees)
      .catch(console.error);
  }, []);

  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>Employees</Typography>
      <List>
        {employees.map((emp) => (
          <ListItem key={emp.id}>
            <ListItemText primary={`${emp.first_name} ${emp.last_name}`} secondary={emp.email} />
          </ListItem>
        ))}
      </List>
    </Container>
  );
}
