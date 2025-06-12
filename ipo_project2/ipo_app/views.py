from django.shortcuts import render
from .models import IPO
from rest_framework import viewsets
from .models import Company, Document
from .serializers import CompanySerializer, IPOSerializer, DocumentSerializer

def ipo_list_view(request):
    ipos = IPO.objects.all()
    return render(request, 'ipo_app/ipo_list.html', {'ipos': ipos})

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
