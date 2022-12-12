from django.forms import ModelForm
from Discos.models import disco

class disco_form (ModelForm):
    
    class Meta:
        model = disco
        fields = '__all__'