from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render_to_response,RequestContext
from .models import NGO,Strategy,



# Create your views here.
def index(request):	
	return render_to_response('index.html')

def AIP(request):
	return render_to_response('AIP.html')

def QP(request):
	return render_to_response('QP.html')

def Dashboard(request,NGO_selected=""):
	NGO_details=Strategy.objects.filter(NGO_name=NGO_selected) 	#find selected NGO details

	return render(request, 'Dashboard.html', {'NGO_details':NGO_details})

def login(request):
	return render_to_response('login.html')