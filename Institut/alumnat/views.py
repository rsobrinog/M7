from django.shortcuts import render, redirect
from .forms import AlumnatForm
from .models import Alumnat


students = [
    {
        'id': 1,
        'name': 'Roger',
        'surname': 'Sobrino',
    },
    {
        'id': 2,
        'name': 'Oriol',
        'surname': 'Roca',
    }
]
def students_list(request):
    context = {'students':students}
    return render(request,'students_list.html', context)

def stu_form(request):
    form = AlumnatForm()

    if request.method == 'POST':
        form = AlumnatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_list')

    context={'form':form}
    return render(request, 'form.html', context)

def update(request,pk):
    student = Alumnat.objects.get(id=pk)
    form = AlumnatForm(instance=student)

    if request.method == 'POST':
        form = AlumnatForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_list')

    context = {'form':form}
    return render(request,'form.html',context)
