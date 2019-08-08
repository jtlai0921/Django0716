from django.http import HttpResponse
from django.shortcuts import render
from math import sin, cos, sqrt, atan2, radians
import requests
import json

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


def search(mylat, mylng, dist, sbi, bemp):
    url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json'
    r = requests.get(url)
    root_object = json.loads(r.text)
    result_object = root_object['result']
    records_array = result_object['records']
    dict = {}
    for record in records_array:
        lat = float(record['lat'])
        lng = float(record['lng'])
        m = distance(mylat, mylng, lat, lng)
        t = '%.1f' % (m / (3000/60))
        if int(record['sbi']) >= sbi and int(record['bemp']) >= bemp and m <= dist:
            record['m'] = m//1
            record['t'] = t
            dict.update({record['sna']: record})

    return dict

def distance(point_1_lat, point_1_lon, point_2_lat, point_2_lon):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(float(point_1_lat))
    lon1 = radians(float(point_1_lon))
    lat2 = radians(float(point_2_lat))
    lon2 = radians(float(point_2_lon))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c * 1000  # m 公尺
    return distance