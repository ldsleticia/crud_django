from app.models import Carros
from django.forms import ModelForm


class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']
