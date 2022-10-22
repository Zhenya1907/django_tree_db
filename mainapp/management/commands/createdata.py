from django.core.management.base import BaseCommand
from faker import Faker
from mainapp.models import Department, Employee
import random


NUMBER_OF_DEPARTMENTS = 25
NUMBER_OF_EMPLOYEES = 50

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(NUMBER_OF_DEPARTMENTS):

            Department.objects.create(
                name = fake.unique.company(),
                parent_id = random.randint(0, 4)
            )

        for _ in range(NUMBER_OF_EMPLOYEES):
            departments_pk = Department.objects.values_list('id', flat=True)
            Employee.objects.create(
                first_name = fake.first_name(),
                middle_name = fake.language_name(),
                last_name = fake.last_name(),
                position = fake.job(),
                employment_date = fake.date(),
                salary = random.randint(1000, 10000),
                department_id_id = random.choice(departments_pk)
            )

        check_departments = Department.objects.all().count()
        check_employees = Employee.objects.all().count()

        self.stdout.write(self.style.SUCCESS(f'Number of departments: {check_departments}\n Number of employees: {check_employees}'))


