from django.shortcuts import render, get_object_or_404
from .models import IPO
from rest_framework import viewsets
from .serializers import IPOSerializer

# View for listing IPOs
def ipo_list(request):
    ipos = IPO.objects.all()
    return render(request, 'IPO_App/ipo_list.html', {'ipos': ipos})

# View for displaying details of a single IPO
def ipo_details(request, id):
    ipo = get_object_or_404(IPO, id=id)
    return render(request, 'IPO_App/ipo_details.html', {'ipo': ipo})

# REST API ViewSet for IPOs
class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
