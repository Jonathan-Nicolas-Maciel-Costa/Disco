from django.contrib import admin
from django.urls import path,  include
from .views import  (index_view,
                    detalhes_view,
                    header_view,
                    footer_view,
                    teste_view,
                    create,
                    detalhesClassView,
                    indexClassView,
                    createClass,
                    updateClass,
                    deleteClass
)

urlpatterns = [
    
    #path('', index_view, name='Home'),
    path('', indexClassView.as_view(), name='Home'),

    
    path('header', header_view, name='header'),
    
    path('footer', footer_view, name='footer'),
    path('teste', teste_view, name='text'),
    
    path('<int:pk>/', detalhesClassView.as_view(), name='Detalhes_classView'),
    path('<int:discos_id>/', detalhes_view, name='Detalhes'),  #nao é mais utilizado
    
    path('add_disco/', createClass.as_view(), name="criar_disco"),
    #path('add_disco', create, name="criar_disco")
    
    path('update_disco/<int:pk>/', updateClass.as_view(),  name="update"),
    path('deletar_disco/<int:pk>/', deleteClass.as_view(),  name="deletar")
]
