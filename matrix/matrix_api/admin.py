from django.contrib import admin

# Register your models here.

from django.apps import apps


for model in apps.get_app_config('matrix_api').get_models():
    admin.site.register(model)
