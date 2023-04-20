from django.shortcuts import render,redirect
from .forms import TeacherForm
from .models import Teacher


def teachers_list(request):
    teachers = Teacher.objects.all().values()
    context={'teachers':teachers}
    return render(request, 'teachers_list.html', context)

def teach_form(request):
    form = TeacherForm()

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers_list')

    context = {'form':form}
    return render(request, 'form.html', context)


def update(request,pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers_list')

    context = {'form':form}
    return render(request,'form.html',context)


def delete(request,pk):
    teacher = Teacher.objects.get(id=pk)

    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers_list')

    context = {'teacher':teacher}
    return render(request, 'delete.html', context)