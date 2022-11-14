from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class': 'input', 'type':'text', 'placeholder': 'City Name', "id":'city'})}
        