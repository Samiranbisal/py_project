from django.http import HttpResponse
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

def aboutUs(requst):
    return HttpResponse("Hi Samiran...! Good Morning...!")

def couseDetails(requst,couseid):
    return HttpResponse(f"Hi Samiran...! Good Morning...! {couseid}")