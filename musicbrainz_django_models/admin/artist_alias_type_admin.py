from django.contrib import admin


class artist_alias_type_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'child_order', 'description', 'gid')
    readonly_fields = ('id', 'name', 'parent', 'child_order', 'description', 'gid')
