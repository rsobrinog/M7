from django.shortcuts import render
from .forms import TeacherForm

teachers=[
    {
        'id': 1,
        'name': 'Paco',
        'surname': 'Celeste'
    },
    {
        'id': 2,
        'name': 'Maria',
        'surname': 'Celestina'
    }
]
def teachers_list(request):
    context={'teachers':teachers}
    return render(request, 'teachers_list.html', context)

def teach_form(request):
    form = TeacherForm()
    context = {'form':form}
    return render(request, 'form.html', context)
