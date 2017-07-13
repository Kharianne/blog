from django.contrib import admin
from .forms import LabelForm


class LabelAdmin(admin.ModelAdmin):
    form = LabelForm
