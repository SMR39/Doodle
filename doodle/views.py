from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


from doodle.models import Meeting
from doodle.models import DateChoice
from doodle.models import Room


def index(request):
    meeting_list = Meeting.objects.order_by('meeting_name')
    template = loader.get_template('doodle/index.html')
    context = RequestContext(request, {
                             'meeting_list': meeting_list,
                             })
    return HttpResponse(template.render(context))

#def list(request, meeting_id):
#   return HttpResponse("You're looking at lists of meeting %s." % meeting_id)

def details(request, meeting_id):
    p = get_object_or_404(Meeting, pk=meeting_id)
    try:
        selected_choice = p.datechoice_set.get(pk=request.POST['DateChoice'])
    except (KeyError, DateChoice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'doodle/details.html', {
                      'meeting': p,
                      'error_message': "You didn't select a choice.",
                      })
    else:
            selected_choice.nbVotes += 1
            p.nbVotesRequired -= 1
            selected_choice.save()
            p.save()
            return HttpResponseRedirect(reverse('doodle:results', args=(p.id,)))

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
def chooseroom(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    room_list = Room.objects.all()
    return render(request,'doodle/chooseroom.html',{'meeting':meeting, 'room_list':room_list})        

def room(request, meeting_id):
    room_list = Meeting.objects.order_by('room')
    template = loader.get_template('doodle/room.html')
    context = RequestContext(request, {
                             'room_list': room_list,
                             })
    return HttpResponse(template.render(context))

def roomselect(request, meeting_id):
    p = get_object_or_404(Meeting, pk=meeting_id)
    try:
        selected_room=get_object_or_404(Room, pk=request.POST['choice'])
    except (KeyError,Room.DoesNotExist):
        #redisplay the same form
        room = Room.objects.all()
        return render(request,'doodle/chooseroom.html',{
                            'meeting' : p,'room':room,
                            'error_message': "You didn't select a choice",
                            })
    else:
        p.room= selected_room
        p.save()
        return render(request, 'doodle/roomselect.html', {'p': p})



def results(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    maxim = 0
    if meeting.nbVotesRequired == 0:
        for date in meeting.datechoice_set.all():
            if date.nbVotes > maxim:
                maxim = date.nbVotes
                finalDate = date
        meeting.date = finalDate.date_to_be_choosed
        meeting.save()
    
    return render(request, 'doodle/results.html', {'meeting': meeting})

def roomdetail(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    return render(request, 'doodle/roomdetail.html', {'meeting': meeting})    

