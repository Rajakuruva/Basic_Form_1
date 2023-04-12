from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Sample(request):
    if request.method=='POST':
        name=request.POST['un']
        pw=request.POST['pw']
        # print(name)
        # print(pw)
        return HttpResponse(f"Data Submitted  of {name}")
    
    return render(request,'Sample.html')

def Ex1(request):
    if request.method=='POST':
        First_name=request.POST['fs']
        Last_name=request.POST['ls']
        pw=request.POST['pws']
        print(First_name)
        print(Last_name)
        print(pw)
        return HttpResponse("Data Will be submitted successfully complted!!!")

    return render(request,'Ex1.html')