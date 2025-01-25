from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import RegisterForm, CustomerForm

from .models import Customer

# Create your views here.

#----------------------DISPLAY RECORDS OR LOGIN--------------------
def home(request):
    customers = Customer.objects.all()
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You logged in successfully!!")
            return redirect('home')
        else:
            messages.error(request, "Failed to log in!!")
            return redirect('home')

    context = {'customers': customers}
    return render(request, 'login-signup.html', context)


#----------------------LOGOUT USER--------------------
def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!!")
    return render(request, 'login-signup.html')

#----------------------REGISTER A NEW USER--------------------
def registerUser(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You registered successfully')
            return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)

#----------------------DISPLAY SINGLE CUSTOMER RECORD--------------------
def customerRecord(request, pk):
    customer = Customer.objects.get(id=pk)

    context = {'customer': customer}
    return render(request, 'record.html', context)

#----------------------DELETE A CUSTOMER RECORD--------------------
def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)

    if request.user.is_authenticated:
        customer.delete()
        messages.success(request, "Customer's record deleted successfully!!")
        return redirect('home')

    context = {'customer': customer}
    return render(request, 'home', context)

#----------------------ADD A NEW CUSTOMER RECORD--------------------
def addRecord(request):
    form = CustomerForm()

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Customer's record added successfully")
                return redirect('home')

    context = {'form': form}
    return render(request, 'add-record.html', context)

#----------------------UPDATE A CUSTOMER RECORD--------------------
def updateRecord(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST, instance=customer)
            if form.is_valid():
                form.save()
                messages.success(request, "Record updated successfully")
                return redirect('home')
    
    else:
        messages.info(request, "You must be logged in!!")
        return redirect('home')

    context = {'form': form}
    return render(request, 'add-record.html', context)