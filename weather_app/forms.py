from django.forms import ModelForm, TextInput
from .models import Weather


class WeatherForm(ModelForm):
    class Meta:
        model = Weather
        fields = "__all__"
        widgets = {'city_name': TextInput(attrs={'class': 'input-group form-control w-50', 'placeholder': 'City Name'})}
