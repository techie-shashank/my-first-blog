from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mypage(request):
	return render(request,'aboutme/mypage.html',{})
