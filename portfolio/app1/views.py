from django.shortcuts import render
import datetime
# # Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    first_date = datetime.date(2019, 0o2, 0o3)
    second_date = datetime.date.today()
    result =  second_date - first_date
    a = result.days
    d, y, w = int(a), None, None
    y = (int)(d / 365)
    m = (int)((d % 365) / 30)
    d = (a-((y*365)+(m*30)))
    yrs = y
    mnths = m
    days = d
    return render(request,'about.html', {'con':yrs,'con2':mnths,'con3':days})

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')

def skills(request):
    return render(request,'skills.html')
