from django import forms


class BuscarCursosForm(forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()

class BuscarCamadaForm(forms.Form):
    camada = forms.IntegerField()