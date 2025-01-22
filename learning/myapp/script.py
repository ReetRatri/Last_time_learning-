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



def bulkrecords(number):
    # number =10000
    print(number)
    # create = [Persons(person_name = fake.name() , address = fake.address() , phone_number = fake.phone_number() ) for _ in range (10000)]

    # Persons.objects.bulk_create(create)
    for i in range(10000):
        Persons.objects.create(
            person_name = fake.name() ,
            address = fake.address() ,
            phone_number = fake.phone_number()
        )


def bulkdelete(numer):
    numer = 10000
    Persons.objects.all().delete()

# bulkrecords(10000)
