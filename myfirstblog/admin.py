from django.contrib import admin
from .models import Post, Category, Label
from .custom_admin import LabelAdmin


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Label, LabelAdmin)
