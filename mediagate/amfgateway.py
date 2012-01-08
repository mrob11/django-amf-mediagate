from pyamf.remoting.gateway.django import DjangoGateway
from mediagate import views

services = {
    'mediagate.getFile': views.getfile,
}

mediagateGateway = DjangoGateway(services)