from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View 

def fbv(request):
    return HttpResponse('This is function Based Views')

class cbv(View):
    def get(self,request):
        return HttpResponse('This is Class Based Views')

class cbv_first(View):
    def get(self,request):
        return render(request,'cbv_first.html')