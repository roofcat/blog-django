from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin


from .models import Entrada


class EntradaAdmin(admin.ModelAdmin):
	pass


admin.site.register(Entrada, EntradaAdmin)