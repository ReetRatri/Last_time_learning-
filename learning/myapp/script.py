from faker import Faker
from .models import *
import random
fake = Faker('en_IN')

# def scripting_db(records= 982)-> None:
#     for i in range(records):
#         college_name = fake.company() + " College"
#         college_address =fake.address()
#         College_Formdata.objects.create(

#             college_name =  college_name,
#             college_address = college_address
#         )
     

def scripting_db(records=82) -> None:
    colleges = College_Formdata.objects.all()
    for i in range(1000):   # Corrected range usage
        choice = ['Male', 'Female']
        name = fake.name()  # Faker methods return strings directly
        email = fake.email()
        password = fake.password()
        gender = random.choice(choice)  # Corrected gender selection
        college = random.choice(colleges)

        Formdata.objects.create(
            name=name,  # Removed extra ()
            email=email,  
            password=password,  
            gender=gender,
            college = college

        )





