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
    return render(request, 'fruit_form.html' )


def fruit_result(request):
    dict = {}
    dict.update({request.GET['fruit_name1']: request.GET['fruit_vote1']})
    dict.update({request.GET['fruit_name2']: request.GET['fruit_vote2']})
    dict.update({request.GET['fruit_name3']: request.GET['fruit_vote3']})
    return render(request, 'fruit_result.html', {'data': dict})


def youbike_form(request):
    dict = {}
    dict['lat'] = request.COOKIES['lat'] if 'lat' in request.COOKIES else 24.990205
    dict['lng'] = request.COOKIES['lng'] if 'lng' in request.COOKIES else 121.312054
    dict['dist'] = request.COOKIES['dist'] if 'dist' in request.COOKIES else 500
    dict['sbi'] = request.COOKIES['sbi'] if 'sbi' in request.COOKIES else 20
    dict['bemp'] = request.COOKIES['bemp'] if 'bemp' in request.COOKIES else 20

    return render(request, 'youbike_form.html', {'data': dict})


def youbike_result(request):
    lat = float(request.GET['lat'])
    lng = float(request.GET['lng'])
    dist = int(request.GET['dist'])
    sbi = int(request.GET['sbi'])
    bemp = int(request.GET['bemp'])

    dict = search(lat, lng, dist, sbi, bemp)
    response = render(request, 'youbike_result.html', {'data': dict})
    # 存入 cookies
    response.set_cookie('lat', lat)
    response.set_cookie('lng', lng)
    response.set_cookie('dist', dist)
    response.set_cookie('sbi', sbi)
    response.set_cookie('bemp', bemp)
    return response


def login_form(request):
    dict = {}
    dict['email'] = request.COOKIES['email'] if 'email' in request.COOKIES else ''
    dict['password'] = request.COOKIES['password'] if 'password' in request.COOKIES else ''
    dict['remember'] = 'checked' if 'remember' in request.COOKIES else ''
    return render(request, 'login_form.html', {'data': dict})


def login_result(request):
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    remember = request.POST.get('remember', False)
    response = HttpResponse("Hello " + email + ", " + password + ", " + str(remember))
    # 將資料存進 cookie
    if remember:
        response.set_cookie('email', email)
        response.set_cookie('password', password)
        response.set_cookie('remember', remember)
    else:
        response.delete_cookie('email')
        response.delete_cookie('password')
        response.delete_cookie('remember')
    return response
