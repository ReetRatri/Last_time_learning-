from django.shortcuts import render ,redirect

# Create your views here.
from .models import Item
from .models import *
from .models import Formdata
from django.db.models import Q
from .forms import Itemform

from django.http import HttpResponse ,JsonResponse


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

def success_view(request):
    return render(request, 'myapp/success.html')

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


