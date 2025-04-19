from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicio, name='inicio'),
    path('crear_curso/',views.crear_curso, name='crear_curso'),
    path('crear_alumno/',views.crear_alumno, name='crear_alumno'),
    path('ver_curso/',views.ver_curso, name='ver_curso'),
    # path('eliminar_alumno/', views.seleccionar_curso, name='seleccionar_curso'),
    # path('eliminar_alumno/<int:id_curso>/', views.eliminar_alumnos_curso, name='eliminar_alumnos_curso'),
    # path('borrar_alumno/<int:id_alumno>/', views.borrar_alumno, name='borrar_alumno'),
    
    
     
]      


