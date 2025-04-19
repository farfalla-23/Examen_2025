from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('crear_curso/',views.crear_curso, name='crear_curso'),
    path('crear_alumno/',views.crear_alumno, name='crear_alumno'),
    path('ver_curso/',views.ver_curso, name='ver_curso'),
    #Nuevo
    path('eliminar_alumno/', views.seleccionar_curso_eliminar, name='seleccionar_curso_eliminar'),
    path('eliminar_alumno/<int:curso_id>/', views.eliminar_alumno, name='eliminar_alumno'),


    
    
     
]      


