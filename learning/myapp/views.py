from django.shortcuts import render ,redirect

# Create your views here.
from .models import Item
from .models import *
from .models import Formdata
from django.db.models import Q
from .forms import Itemform

from django.http import HttpResponse ,JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def index(request):
    
    data = {
        'status' : True , 
        'message' : 'django server'
    }
    return JsonResponse(data)

# create
def create_item(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        # D:\myproject\Last_time_learning\Last_time_learning-\learning\myapp\templates
    else:
        form = Itemform()
    return render(request, 'myapp/item_form.html', {'form': form})
        

# read
def item_list(request):
    items = Item.objects.all()
    return render(request , 'myapp/item_list.html', {'items': items})


# update
def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = Itemform(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = Itemform(instance=item)
    return render(request, 'myapp/item_form.html', {'form': form})


def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'myapp/item_confirm_delete.html', {'item': item})


def form(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        print(name , email , password , gender)

        # formdata = Formdata(name , email , password , gender)
        formdata = Formdata(name=name, email=email, password=password, gender=gender)
        formdata.save()

        return redirect('success')


    return render(request, 'myapp/form.html')


def searchbox(request):
    students = Formdata.objects.all()
    # college = students.college.
    search = request.GET.get('search_box')
    print(search)
    print('--------------------------------')
    print('--------------------------------')
    print('--------------------------------')
    print('--------------------------------')

    # search_box = request.Get
    if search:
        students = students.filter(Q(name__icontains =search) |  Q(email__icontains=search) | Q(college__college_name__icontains = search) | Q(gender__icontains=search))
        # email = students.filter(email__icontains =search)
        

    context = {'students' :students , 'search':search  }
    # print(context)
    return render(request ,  'myapp/searchbox.html' , context) 





def login_portal(request):
    print(request.user)
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username , password)
        print(username , password)
        print(username , password)
        print(username , password)
        print(username , password)
        print(username , password)
        print(username , password)

        user_obj =User.objects.filter(username = username)
        
        if not user_obj.exists():
            messages.error(request, ' username does not exist')
            return redirect('/')
        
        if True:
            print(authenticate(username = username , password = password ))
        
        user_obj = authenticate(username = username , password = password )
        

        if not user_obj:
            messages.error(request, 'Invalid credentials')

            return redirect('/login/') 
        
        
        login( request ,user_obj)
        messages.error(request, 'u got it.')
        return redirect('/success/')
    return render(request , 'myapp/login.html')




def registration_portal(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
        print(username , email , password)

        user_obj = User.objects.filter(Q(email=email) | Q(username=username))

        if user_obj.exists():
            messages.error(request , 'Username already exists')
            return redirect('/')
        user_obj = User.objects.create(
            username=username, 
            email=email
            )

        # user_obj = User(username=username, email=email)
        user_obj.set_password(password)  # Hash the password before saving
        user_obj.save()
        messages.error(request , 'Success account created.')


    return render(request , 'myapp/registration.html')


@login_required(login_url='/login/')
def success_view(request):
    # if request.user.is_authenticated:
    #     print('yes')
    #     print(request.user)

    return render(request, 'myapp/success.html')

def logout_portal(request):
    logout(request)  # Log the user out
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/')  # Redirect to homepage or login page
