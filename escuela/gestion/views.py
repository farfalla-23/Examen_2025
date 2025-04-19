from django.shortcuts import render , redirect, get_list_or_404
from .models import Curso,Alumno
def inicio(request):
    return render(request,'gestion/inicio.html')

def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_curso']
        turno = request.POST['turno']
        preceptor = request.POST['preceptor']
        Curso.objects.create(nombre_curso= nombre, turno=turno, preceptor=preceptor)
        return redirect('inicio')
    return render(request, 'gestion/crear_curso.html')

def crear_alumno(request):
    cursos= Curso.objects.all()
    if request.method == 'POST':
        Alumno.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            dni_alumno=request.POST['dni'],
            edad=request.POST['edad'],
            gmail=request.POST['gmail'],
            telefono=request.POST['telefono'],
            id_curso_alumno_id=request.POST['curso']
        )
        return redirect('inicio')
    return render(request,'gestion/crear_alumno.html',{'cursos': cursos})

def ver_curso(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion/ver_cursos.html',{'cursos':cursos})

#Nuevo
def eliminar_alumno(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    alumnos = Alumno.objects.filter(id_curso_alumno=curso)

    if request.method == 'POST':
        alumno_id = request.POST.get('alumno_id') 
        if alumno_id:  
            try:
                alumno = Alumno.objects.get(id=alumno_id)
                alumno.delete() 
                return redirect('eliminar_alumno', curso_id=curso_id) 
            except Alumno.DoesNotExist:
                return ("Alumno no encontrado")

    return render(request, 'gestion/eliminar_alumno.html', {'curso': curso, 'alumnos': alumnos})

def seleccionar_curso_eliminar(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion/seleccionar_curso_eliminar.html', {'cursos': cursos})
