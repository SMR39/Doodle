from django.contrib import admin
from doodle.models import Room
from doodle.models import Meeting
from doodle.models import DateChoice

class ChoiceInline(admin.StackedInline):
    model = DateChoice
    extra = 3

class MeetingAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields':['meeting_name']}),
                 ('No of required votes',{'fields':['nbVotesRequired'],'classes':['collapse']}),
                 ('Allocate Room',{'fields':['room'],'classes':['collapse']}),
                 ]
    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Room)
admin.site.register(Meeting,MeetingAdmin)
admin.site.register(DateChoice)