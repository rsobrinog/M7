from django.shortcuts import render


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