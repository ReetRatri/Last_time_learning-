from django.contrib import admin

# Register your models here.

from .models import Formdata #,Persons

# admin.site.register(Formdata)
# admin.site.register(Persons)

# we can do above both by adding decorators

# class OrderInline(admin.TabularInline):
#     model = Persons
#     extra = 0



@admin.register(Formdata)
class FormdataAdmin(admin.ModelAdmin):
    list_display = (
    "name" , 
    "email" , 
   
    "college__college_name" , 
    "gender"
    )

# adding search
    search_fields =(
    "name" , 
    "email" , 
   
    
    "gender"
    )
    # inlines = [OrderInline]


# for filter
# @admin.register(Persons)
# class Personadmin(admin.ModelAdmin):
#     list_display = (

#     'person_name' , 
#     'address' , 
#     'phone_number'



#     )
    # list_filter()




