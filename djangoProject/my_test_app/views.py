from django.http import HttpResponse
from django.shortcuts import render
"""
render 渲染模板
request:请求
template_name:模板名字
context:数据源
"""
def index(request):
    context = {
        'con':'你是一个聪明人,eiheihjie'
    }
    return render(request,"my_test_app/test.html",context=context)
    #return HttpResponse("./templates/test.html")