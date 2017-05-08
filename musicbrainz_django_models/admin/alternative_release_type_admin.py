from django.contrib import admin


class alternative_release_type_admin(admin.ModelAdmin):
    list_display = ('id', 'name')
