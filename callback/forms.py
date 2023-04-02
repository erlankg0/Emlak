from django.forms import forms
from callback.models import Callback


class CallBackForms(forms.Form):
    class Meta:
        model = Callback
        fields = '__all__'
