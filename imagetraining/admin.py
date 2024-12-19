from django.contrib import admin
from .models import ObjectModelTraining,TrainingImages,SampleImages
# Register your models here.

class SampleImagesAdmin(admin.ModelAdmin):
    fields = ['file','name']
    list_display  = ['file','name']

    # def has_change_permission(self, request, obj=None):
    #     return None
    #
    # def has_add_permission(self, request, obj):
    #     return  None


class SampleImagesInline(admin.TabularInline):
    model = SampleImages
    extra = 1
    fields = ['file','name']
    readonly_fields = ['file','name']

class TrainingImagesAdmin(admin.ModelAdmin):
    fields = ['file']
    list_display = ['file', 'name']

class TrainingImagesInline(admin.TabularInline):
    model = TrainingImages
    extra = 5
    fields = ['file']
    readonly_fields = ['name']

class ObjectModelTrainingAdmin(admin.ModelAdmin):
    inlines = [TrainingImagesInline, SampleImagesInline]
    fields = ['name' ,'seed']
    list_display = ['name' ,'seed' , 'duration']
    exclude= ['created_by', 'updated_by', 'deleted_by', 'created_at', 'updated_at', 'deleted_at']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.updated_by = request.user
            obj.deleted_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(ObjectModelTraining,ObjectModelTrainingAdmin)
admin.site.register(TrainingImages,TrainingImagesAdmin)
admin.site.register(SampleImages,SampleImagesAdmin)