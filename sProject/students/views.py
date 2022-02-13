from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from students.models import Student, Profile
# Create your views here.
def index(request):
    return HttpResponse("성공적인가요")

def regStudent(request):
	return render(request, 'students/registerStudent.html')

def regConStudent(request):
	name = request.POST['name']
	major = request.POST['major']
	age = request.POST['age']
	grade = request.POST['grade']
	gender = request.POST['gender']
	
	qs = Student(s_name=name, s_major=major, s_age=age, s_grade=grade, s_gender=gender)
	qs.save()
	
	return HttpResponseRedirect(reverse('students:stuAll'))

def readStudentAll(request):
	qs = Student.objects.all()
	context = {'student_list': qs}
	return render(request, 'students/readStudents.html', context)


def upload(request):
    return render(request,'students/upload.html')

def upload_create(request):
    form=Profile()
    form.title=request.POST['title']
    try:
        form.image=request.FILES['image']
    except: #이미지가 없어도 그냥 지나가도록-!
        pass
    form.save()
    return redirect('/students/profile/')

def profile(request):
    profile=Profile.objects.all()
    return render(request,'students/profile.html',{'students':profile})
