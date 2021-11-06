from django.contrib import admin

from .models import Jojo, Ass


# Register your models here.

class JojoAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('ass',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Jojo, JojoAdmin)
admin.site.register(Ass)
