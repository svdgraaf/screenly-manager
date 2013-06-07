from django.shortcuts import render_to_response
from django.template import RequestContext
import select
import sys
import pybonjour

timeout = 5
hosts = []
resolved = []

def index(request):
    return render_to_response('index.haml', locals(), RequestContext(request))


