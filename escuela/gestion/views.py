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

# def seleccionar_curso(request):
#     cursos = Curso.objects.all()
#     return render(request, 'gestion/seleccionar_curso.html', {'cursos': cursos})

# def eliminar_alumnos_curso(request, id_curso):
#     curso = get_object_or_404(Curso, pk=id_curso)
#     alumnos = Alumno.objects.filter(id_curso_alumno=curso.id_curso)
#     return render(request, 'gestion/eliminar_alumnos.html', {'curso': curso, 'alumnos': alumnos})

# def borrar_alumno(request, id_alumno):
#     alumno = get_object_or_404(Alumno, pk=id_alumno)
#     id_curso = alumno.id_curso_alumno
#     alumno.delete()
#     return redirect('eliminar_alumnos_curso', id_curso=id_curso)
