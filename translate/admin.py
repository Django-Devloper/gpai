from django.contrib import admin
from .models import Translator
# Register your models here.

class TranslatorAdmin(admin.ModelAdmin):
    fields = ['input_language', 'output_language', 'user_input','assistant_output']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.updated_by = request.user
            obj.deleted_by = request.user
        super().save_model(request, obj, form, change)

    list_display = ['input_language', 'output_language', 'user_input','assistant_output']
    readonly_fields = ['assistant_output']

admin.site.register(Translator,TranslatorAdmin)
