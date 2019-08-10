from django.http import HttpResponse
from django.shortcuts import render

from Django0716.utils import search


def hello(request):
    return HttpResponse("Hello World")


def hello_name(request, name):
    return HttpResponse("Hello %s" % name)


def hello_add(request, x, y):
    return HttpResponse("Hello %d + %d = %d" % (x, y, (x+y)))


def hello2_add(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    return HttpResponse("Hello2 %d + %d = %d" % (x, y, (x+y)))


def hello_template(request):
    return render(request, 'hello.html')


def hello_template_name(request, name):
    dict = {'name':name, 'age':20}
    return render(request, 'hello_name.html', dict)


def hello_template_users(request):
    dict = {}
    users = [
             {'name': 'vincent', 'age': 30},
             {'name': 'anita', 'age': 28},
             {'name': 'howard', 'age': 15},
             {'name': 'joanna', 'age': 10}
            ]
    dict['users'] = users
    return render(request, 'hello_users.html', dict)


def fruit_form(request):
    return render(request, 'fruit_form.html')


def fruit_result(request):
    dict = {}
    dict.update({request.GET['fruit_name1']: request.GET['fruit_vote1']})
    dict.update({request.GET['fruit_name2']: request.GET['fruit_vote2']})
    dict.update({request.GET['fruit_name3']: request.GET['fruit_vote3']})
    return render(request, 'fruit_result.html', {'data': dict})


def youbike_form(request):
    return render(request, 'youbike_form.html')


def youbike_result(request):
    dict = search(float(request.GET['lat']), float(request.GET['lng']), int(request.GET['dist']), int(request.GET['sbi']), int(request.GET['bemp']))
    return render(request, 'youbike_result.html', {'data': dict})


def login_form(request):
    return render(request, 'login_form.html')


