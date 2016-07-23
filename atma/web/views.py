from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def AIP(request):
	return render_to_response('AIP.html')