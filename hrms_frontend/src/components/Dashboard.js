import React from 'react';
import { Typography, Container } from '@mui/material';

export default function Dashboard() {
  return (
    <Container sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Welcome to the HRMS Dashboard
      </Typography>
    </Container>
  );
}
