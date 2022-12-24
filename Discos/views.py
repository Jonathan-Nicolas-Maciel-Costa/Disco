from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import disco
from  django.urls import reverse_lazy
from .form import disco_form

from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
) 

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

class detalhesClassView(LoginRequiredMixin,DetailView): 
    template_name="detalhes.html"
    model = disco
    queryset = disco.objects.all()
    

class indexClassView(LoginRequiredMixin,ListView):
    template_name="index.html"
    model = disco
    queryset = disco.objects.all()
    
class createClass (LoginRequiredMixin,CreateView):
    template_name="criar_disco.html"
    model = disco
    fields = '__all__'
    success_url = reverse_lazy('Home')
    
class updateClass(LoginRequiredMixin,UpdateView):
    template_name="criar_disco.html"
    model = disco
    fields = '__all__'
    success_url = reverse_lazy('Home')
    
class deleteClass(LoginRequiredMixin,DeleteView):
    template_name="deletar.html"
    model = disco
    fields = '__all__'
    success_url = reverse_lazy('Home')
    
"""    
def index_view (request):

    discos = disco.objects.all()
    discozin = disco.objects.all()
    #discos = disco.objects.get(id=discos_id)
    context = {
        'discos': discos,
        'discozin': discozin
    }
    
    return render(request, 'index.html',  context)

def detalhes_view (request, discos_id):

    discos = get_object_or_404(disco, id=discos_id)
    discozin = disco.objects.all()
    #discos = disco.objects.get(id=discos_id)
    context = {
        'discos': discos,
        'discozin': discozin
    }
    return render (request, 'detalhes.html', context)

def header_view(request):

    return render(request, 'header.html', {}) 

def footer_view(request):
    
    discos = disco.objects.all()
    context = {'discos': discos}
    
    return render (request, 'footer.html', context)

def teste_view(request):
    discos = disco.objects.all()
    context = {'discos': discos}
    return  render (request, 'base.html', context)

def create (request):
    discozin = disco.objects.all()
    form = disco_form()
    if request.method == "POST":
        form = disco_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Home'))
        else:
            return render(request, 'criar_disco.html', context)
    
    else:
        form = disco_form()
        context = {   
            'discozin':discozin,
            'form':form
        }
        return render(request, 'criar_disco.html', context)
 """