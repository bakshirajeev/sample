from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
