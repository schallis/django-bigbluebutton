from django.http import (Http404, HttpResponseRedirect, HttpResponseNotFound,
                        HttpResponse)
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import login as django_login
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import messages
import hashlib

from bbb.models import Meeting

def home_page(request):
    context = RequestContext(request, {
    })
    return render_to_response('home.html', context)


@login_required
def begin_meeting(request):

    if request.method == "POST":
        begin_url = "http://bigbluebutton.org"
        return HttpResponseRedirect(begin_url)

    context = RequestContext(request, {
    })

    return render_to_response('begin.html', context)

@login_required
def meetings(request):

    #meetings = Meeting.objects.all()
    meetings = Meeting.get_meetings()

    context = RequestContext(request, {
        'meetings': meetings,
    })

    return render_to_response('meetings.html', context)

def join_meeting(request, meeting_id):
    form_class = Meeting.JoinForm

    if request.method == "POST":
        # Get post data from form
        form = form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            password = data.get('password')

            return HttpResponseRedirect(Meeting.join_url(meeting_id, name, password))
    else:
        form = form_class()

    context = RequestContext(request, {
        'form': form,
        'meeting_name': meeting_id,
    })

    return render_to_response('join.html', context)

@login_required
def delete_meeting(request, meeting_id, password):
    if request.method == "POST":
        #meeting = Meeting.objects.filter(meeting_id=meeting_id)
        #meeting.delete()
        Meeting.end_meeting(meeting_id, password)

        msg = 'Successfully ended meeting %s' % meeting_id
        messages.success(request, msg)
        return HttpResponseRedirect(reverse('meetings'))
    else:
        msg = 'Unable to end meeting %s' % meeting_id
        messages.error(request, msg)
        return HttpResponseRedirect(reverse('meetings'))

@login_required
def create_meeting(request):
    form_class = Meeting.CreateForm

    if request.method == "POST":
        # Get post data from form
        form = form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            meeting = Meeting()
            meeting.name = data.get('name')
            #password = hashlib.sha1(data.get('password')).hexdigest()
            meeting.attendee_password = data.get('attendee_password')
            meeting.moderator_password = data.get('moderator_password')
            meeting.meeting_id = data.get('meeting_id')
            try:
                url = meeting.start()
                meeting.save()
                msg = 'Successfully created meeting %s' % meeting.meeting_id
                messages.success(request, msg)
                return HttpResponseRedirect(reverse('meetings'))
            except:
                return HttpResponse("An error occureed whilst creating the " \
                                    "meeting. The meeting has probably been "
                                    "deleted recently but is still running.")

    else:
        form = form_class()

    context = RequestContext(request, {
        'form': form,
    })

    return render_to_response('create.html', context)
