from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render_to_response,RequestContext
from .models import NGO,Strategy,Project,Priority_Areas



# Create your views here.
def index(request):	
	return render_to_response('index.html')

def AIP(request, year=""):
	AIP_Details=Project.objects.filter(strategy__year=year).values()
	for project in AIP_Details:
		import pdb; pdb.set_trace()
		project['quarters'] = list(map(lambda x: "Yes" if x else "", [ project['quarter'] - 1 == x for x in range(4) ]))
	return render_to_response('AIP.html',{'AIP':AIP_Details},context_instance=RequestContext(request))

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