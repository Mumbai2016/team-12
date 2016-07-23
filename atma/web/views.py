from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def AIP(request):
	return render_to_response('AIP.html')

def QP(request):
	return render_to_response('QP.html')

def Dashboard(request):
	return render_to_response('Dashboard.html')

def index(request):
	return render_to_response('index.html')

def login(request):
	return render_to_response('login.html')