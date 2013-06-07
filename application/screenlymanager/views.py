from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Client
from .forms import ClientForm
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404


def index(request):
    clients = Client.objects.all()
    return render_to_response('index.haml', locals(), RequestContext(request))


def clients(request):
    clients = Client.objects.all()
    return render_to_response('clients.haml', locals(), RequestContext(request))


def client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(instance=client)
    return render_to_response('client.haml', locals(), RequestContext(request))