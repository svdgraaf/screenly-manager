from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Client
from .forms import ClientForm
import pybonjour
from .browse import get_services
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404


def index(request):
    clients = Client.objects.all()
    return render_to_response('index.haml', locals(), RequestContext(request))


def clients(request):
    clients = Client.objects.all()

    if request.GET.get('discover'):
        _discover_bonjour_clients()

    return render_to_response('clients.haml', {'clients': clients}, RequestContext(request))


def client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(instance=client)
    return render_to_response('client.haml', locals(), RequestContext(request))


def _discover_bonjour_clients():
    clients_bonjour = get_services('_screenly._tcp.')
    for client in clients_bonjour:
        try:
            Client.objects.get(last_ip=client['hosttarget'])
        except:
            obj = Client(name=client['fullname'].split('.')[0], last_ip=client['hosttarget'], port=client['port'])
            obj.save()