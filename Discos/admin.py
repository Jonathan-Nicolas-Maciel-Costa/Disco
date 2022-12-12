from django.contrib import admin
from .models import disco, pais, selo_fonografico, genero_musical

# Register your models here.

admin.site.register(disco)


admin.site.register(pais)
admin.site.register(selo_fonografico)
admin.site.register(genero_musical)