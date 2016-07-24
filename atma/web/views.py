from django.shortcuts import render,HttpResponseRedirect,HttpResponse,render_to_response,RequestContext
from django.forms.models import model_to_dict
from .models import NGO,Strategy,Project,Priority_Areas



# Create your views here.
def index(request):	
	return render_to_response('index.html')

def volunteer(request):	
	return render_to_response('volunteer.html')

def ngo_survey(request):	
	return render_to_response('Survey_form.html')

def find_locator(request):	
	return render_to_response('find_locator.html')

def AIP(request, year=""):
	AIP_Details_query=Project.objects.filter(strategy__year=year)
	projects = []
	AIP_Details=Project.objects.filter(strategy__year=year)
	for project_queryset in AIP_Details:
		project = model_to_dict(project_queryset)
		project['quarters'] = list(map(lambda x: "Yes" if x else "", [project['quarter'] - 1 == x for x in range(4)]))
		projects.append(project)
	return render_to_response('AIP.html',{'AIP':projects},context_instance=RequestContext(request))

def Quarter_Details(request,quar=""):
	QP_Details=Project.objects.filter(quarter=int(quar))	
	return render_to_response('QP.html',{'NGO':QP_Details},context_instance=RequestContext(request))


def Dashboard(request,NGO_selected=""):
	Priority_Areas_Object=Priority_Areas.objects.filter(NGO_name=NGO_selected) 	#find selected NGO details
	Strategy_Object=Strategy.objects.filter(NGO_name=NGO_selected)
	Project_Object=Project.objects.filter(NGO_name=NGO_selected)
	return render_to_response('Dashboard.html',{'Priority_Areas_Object':Priority_Areas_Object,'Strategy_Object':Strategy_Object,'Project_Object':Project_Object},context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html')
