from django.forms import ModelForm
from .models import Alumnat

class AlumnatForm(ModelForm):
    class Meta:
        model = Alumnat
        fields = '__all__'