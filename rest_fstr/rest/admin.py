from django.contrib import admin
from .models import User, Coords, PerevalAdded, PerevalImages, PerevalAreas, SprActivitiesTypes
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'phone')

class CoordsAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'height')

class PerevalAddedAdmin(admin.ModelAdmin):
    list_display = ('user', 'coord', 'beautyTitle', 'title', 'status')

class PerevalImagesAdmin(admin.ModelAdmin):
    list_display = ('pereval', 'date_added')

class PerevalAreasAdmin(admin.ModelAdmin):
    list_display = ('id_parent', 'title')

class SprActivitiesTypesAdmin(admin.ModelAdmin):
    list_display = ('title',)

# Регистрация моделей
admin.site.register(User, UserAdmin)
admin.site.register(Coords, CoordsAdmin)
admin.site.register(PerevalAdded, PerevalAddedAdmin)
admin.site.register(PerevalImages, PerevalImagesAdmin)
admin.site.register(PerevalAreas, PerevalAreasAdmin)
admin.site.register(SprActivitiesTypes, SprActivitiesTypesAdmin)
# Register your models here.
