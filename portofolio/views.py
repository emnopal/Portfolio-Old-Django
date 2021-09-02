from django.shortcuts import render
from portofolio.models import Portofolio

# Create your views here.
def portofolio_index(requests):
    portofolio = Portofolio.objects.all()
    context = {
        'portofolio': portofolio
    }
    return render(requests, 'index.html', context)

def portofolio_detail(requests, pk):
    portofolio = Portofolio.objects.get(pk=pk)
    context = {
        'portofolio': portofolio
    }
    return render(requests, 'detail.html', context)