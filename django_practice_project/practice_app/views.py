from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from django.template import RequestContext

from practice_app.models import Employee
from faker import Faker
from practice_app.forms import StudentForm


def try_it(request):
    return HttpResponse('<h1>tryit executed</h1>')


def get_system_time(request):
    date = datetime.now()
    my_dict = {'date_time': date}
    return render(request, 'practice_app/tp.html', context=my_dict)


def get_or_create_db_record(request):
    fake_data = Faker()
    for i in range(5):
        ename = fake_data.name()
        eid = fake_data.random_number(5)
        e_department = 'information Technology'
        e_post = fake_data.random_element(
            elements=('Software Engineer', 'Python Developer', 'Python Full Stack developer'))
        e_address = fake_data.random_element(elements=('kandivali', 'Borivali', 'Malad', 'Chembur', 'Uttarpradesh'))

        emp_records = Employee.objects.get_or_create(ename=ename, eid=eid, e_department=e_department, e_post=e_post,
                                                     e_address=e_address)
    return HttpResponse()


def employee_info_view(request):
    employee_data = Employee.objects.all()
    my_dict = {'e_data': employee_data}
    return render(request, 'practice_app/tp.html', context=my_dict)


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('message')
        else:

            print(form.errors)

    else:
        form = StudentForm()

    my_dict = {'form': form}
    return render(request, 'practice_app/studentform.html', my_dict)


def success(request):
    return HttpResponse('<h1>Your Data is Submitted Successfuly</h1>')
