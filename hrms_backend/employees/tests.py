from django.test import TestCase
from .models import Department, Employee

class EmployeeModelTests(TestCase):
    def test_create_employee(self):
        dept = Department.objects.create(name='HR')
        emp = Employee.objects.create(first_name='John', last_name='Doe', email='john@example.com', department=dept)
        self.assertEqual(str(emp), 'John Doe')
