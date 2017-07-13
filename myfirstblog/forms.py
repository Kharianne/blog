from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Label


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = "__all__"
        widgets = {
          'color': TextInput(attrs={'type': 'color'})
      }
