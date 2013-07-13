# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.conf import settings

def jasmine(request):
    return render_to_response('SpecRunner.html', 
            context_instance=RequestContext(request))

def jasmine_ci(request):
    return render_to_response('SpecRunnerCi.html', 
            context_instance=RequestContext(request))
