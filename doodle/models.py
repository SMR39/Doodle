from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name + '.'


class Meeting(models.Model):
    room = models.ForeignKey(Room, null=True,blank=True)
    meeting_name = models.CharField(max_length=200,default='')
    date = models.DateTimeField('Date_Selected',null=True,blank=True)
    nbVotesRequired = models.IntegerField(default=10)
    status = models.CharField(max_length=50,default='Open')
    def __unicode__(self):
        return self.meeting_name + '.'


class DateChoice(models.Model):
    meeting = models.ForeignKey(Meeting,null=True,blank=True)
    nbVotes = models.IntegerField(default=0)
    date_to_be_choosed = models.DateTimeField('Date To be Choosed')
    def __unicode__(self):
        return '_ Date To be Choosed' + str(self.date_to_be_choosed) + '.'