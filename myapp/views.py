from django.shortcuts import render
from myapp.forms import StudentReg

def req_val(request):
    if request.method =="POST":
        data = StudentReg(request.POST)
        #print(data) thsi is the first type
        #print(request.method)
        if data.is_valid():
            print("validated")
            name =data.cleaned_data['name']
            email =data.cleaned_data['email']
            print(name+email)
    else:
        data = StudentReg()
        print(request.method,data)
    return render(request,"index.html",{"form":data})
