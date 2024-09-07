from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def homepage(requst):
    data={
        "title":  "Home Page",
        "message": "Welcome to Home Page",
        "list": ["Java", "python", 'php', 'javascript'],
        'student_Details':[
            {'name': 'John', 'age': 20},
            {'name': 'Emma', 'age': 21},
            {'name': 'Oliver', 'age': 19},
            {"name": "king", "age": 25},
        ]
        
    }
    return render(requst, "index.html",data)

def about(request):
    return render(request, "about.html")

def userform(request):
    fromdata = 0  # Initialize fromdata as 0
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1', 0))  # Get 'num1' with default 0
            n2 = int(request.POST.get('num2', 0))  # Get 'num2' with default 0

            fromdata = n1 + n2  # Store the sum in fromdata
            return HttpResponseRedirect('/')
    finally:
        pass  # You can use pass if nothing is needed in the finally block
    return render(request, "userfrom.html", {'output': fromdata})  # Pass the sum to the template


def aboutUs(requst):
    return HttpResponse("Hi Samiran...! Good Morning...!")

def couseDetails(requst,couseid):
    return HttpResponse(f"Hi Samiran...! Good Morning...! {couseid}")