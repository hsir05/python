from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
import os, time, random

# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def testapi(request):
    print(request)
    print(request.method)
    if request.method == "GET":
        print(request.GET.get('aa'))
        resp = {'code': 100, 'type': 'Get', 'data': {'main': request.GET.get('aa')}}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        print(request.POST)
        print(request.body)
        str1 = str(request.body, encoding="utf-8")
        data = eval(str1)
        print(data)
        print(data['aa'])
        print(type(request.body))
        resp = {'code': 100, 'data': {'main': data['aa']}}
        return HttpResponse(json.dumps(resp), content_type="application/json")
@csrf_exempt
def upload(request):
    if request.method == 'GET':
        resp = {'code': 100, 'type': 'get', 'data': {'message':'post上传'}}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    elif request.method == "POST":
        obj = request.FILES.get('file')

        # 文件扩展名
        ext = os.path.splitext(obj.name)[1]  # [0] 为文件名称
        # 文件目录
        d = os.path.dirname(obj.name)
        # 定义文件名，年月日时分秒随机数
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 100)
        # 重写合成文件名
        file_path = os.path.join(d, fn + ext)

        f = open(os.path.join('upload', file_path), 'wb')
        for line in obj.chunks():
            f.write(line)
        f.close()

        resp = {'code': 100, 'data': {'path': 'upload/' + file_path}}
        return HttpResponse(json.dumps(resp), content_type="application/json")

