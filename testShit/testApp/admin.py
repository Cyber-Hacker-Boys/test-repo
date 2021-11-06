from django.contrib import admin

from .models import Jojo, Ass, Master


# Register your models here.

class JojoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'ass')
    list_filter = ('ass', 'date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Jojo, JojoAdmin)
admin.site.register(Ass)
admin.site.register(Master)
