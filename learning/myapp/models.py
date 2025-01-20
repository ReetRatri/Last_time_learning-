from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Students(models.Model):
    gender_choice = (('Male' , 'Male') , ('Female' , 'Female'))
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    Email = models.EmailField()
    gender = models.CharField(max_length=10 ,choices=gender_choice , default='Male')
    Profile_image = models.ImageField(null = True , blank=True , upload_to='myapp')


class College_Formdata(models.Model):
    college_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=100)
    


class Formdata(models.Model):
    # class Meta:
    #    __all__ = ["Formdata"]


    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    college = models.ForeignKey(
        College_Formdata,  # Ensure College_Formdata model exists
        on_delete=models.CASCADE,  
        null=True,  
        blank=True  
    )    
    gender = models.CharField(max_length=10 ,choices=[('male', 'Male'), ('female', 'Female')], default='Male')
