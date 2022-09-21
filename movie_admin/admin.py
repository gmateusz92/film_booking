from django.contrib import admin
from . import models


admin.site.register(models.MovieMaster)
admin.site.register(models.AdminSide)
admin.site.register(models.SetMovie)