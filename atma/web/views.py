from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render_to_response,RequestContext
from .models import NGO,Strategy,Project,Priority_Areas



# Create your views here.
def index(request):	
	return render_to_response('index.html')

def AIP(request):
	return render_to_response('AIP.html')

def QP(request):
	return render_to_response('QP.html')

def Dashboard(request,NGO_selected=""):
	Priority_Areas_Object=Priority_Areas.objects.filter(NGO_name=NGO_selected) 	#find selected NGO details
	Strategy_Object=Strategy.objects.filter(NGO_name=NGO_selected)
	Project_Object=Project.objects.filter(NGO_name=NGO_selected)
	return render_to_response('Dashboard.html',{'Priority_Areas_Object':Priority_Areas_Object,'Strategy_Object':Strategy_Object,'Project_Object':Project_Object},context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html')

def Populate_Project(request):
	return render_to_response('login.html')