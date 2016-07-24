from django.contrib import admin

# Register your models here.
from .models import Strategy, Priority_Areas,Project

class StrategyAdmin(admin.ModelAdmin):
	list_display=('NGO_name','strategy_name')	

class Priority_Areas_Admin(admin.ModelAdmin):
	list_display=('NGO_name','priority_area')

class Project_Admin(admin.ModelAdmin):
	list_display=('project_name','status')

admin.site.register(Strategy,StrategyAdmin)
admin.site.register(Priority_Areas,Priority_Areas_Admin)
admin.site.register(Project,Project_Admin)