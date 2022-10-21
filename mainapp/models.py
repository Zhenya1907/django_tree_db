from django.db import models


class Department(models.Model):
    name = models.CharField(max_lenght=50, verbose_name='Department')
    parent_id = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.pk} {self.name} {self.parent_id}'


class Employee(models.Model):
    first_name = models.CharField(max_lenght=10, verbose_name='First name')
    middle_name = models.CharField(max_lenght=15, verbose_name='Middle name')
    last_name = models.CharField(max_lenght=20, verbose_name='Last name')
    position = models.CharField(max_lenght=50, verbose_name='Position')
    employment_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Employment date')
    salary = models.DecimalField(max_digits=6, decimal_places=0, verbose_name='Salary', default=0)
    department_id = models.ForeignKey(Department)

    def __str__(self) -> str:
        return f'{self.pk} {self.first_name}'
