from django.shortcuts import render
from .forms import AlumnatForm


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
    form = AlumnatForm
    context={'form':form}
    return render(request, 'form.html', context)