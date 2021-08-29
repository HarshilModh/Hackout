from django.db.models import fields
from admission.models import collegedetails
from django.shortcuts import render
from django.http.response import HttpResponse
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="shyam",
    passwd="shyam",
    database="college_information"
)
mycursor = mydb.cursor()
# Create your views here.
def home(request):
    ranks = request.POST.get('rank')
    city = request.POST.get('city')
    cast = request.POST.get('cast')
    field = request.POST.get('field')
    qur = "select * from collegedata where city='{}' and Category='{}' and Course_name ='{}' ".format(city,cast,field)
    mycursor.execute(qur)
    result = mycursor.fetchall()
    # if result is not None:
    #     return render(request,'webhtml/home.html',{'result':result})
    # else:
    return render(request,'webhtml/home.html',{'result': result})
def result(request):
    ranks = request.POST.get('rank')
    city = request.POST.get('city')
    cast = request.POST.get('cast')
    field = request.POST.get('field')
    qur = "select * from collegedata where city='{}' and Category='{}' and Course_name ='{}' ".format(city,cast,field)
    mycursor.execute(qur)
    result = mycursor.fetchall()
    # if result is not None:
    #     return render(request,'webhtml/home.html',{'result':result})
    # else:
    return render(request,'webhtml/result.html',{'result': result})
def output(request):
    return render(request,'webhtml/output.html')