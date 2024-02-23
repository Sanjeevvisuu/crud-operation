import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","main_files_1.settings")

import django
django.setup()

from faker import Faker
faker=Faker()
from random import *
from rest_app.models import *

def gen(n):
    for i in range(n):
        fname = faker.name()
        fschool = faker.company()  
        fDOB = faker.date_of_birth()
        fblood_group = faker.random_element(elements=('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
        ffather_name = faker.name()
        
        stu,created=students.objects.get_or_create(name=fname,school=fschool,DOB=fDOB,blood_group=fblood_group,father_name=ffather_name)
        if created:
            print(f"student created .{stu.name}")
        else:
            print("student not created .")
gen(30)
