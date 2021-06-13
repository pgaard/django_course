from meetups.forms import RegistrationForm
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Meetup, Participant
import logging
# Create your views here.

def index(request):
  # return HttpResponse('hello world')

  meetups = Meetup.objects.all()

  return render(request, 'meetups/index.html', {
    'show_meetups': True,
    'meetups': meetups
  })  #  folder relative to templates folder

logger = logging.getLogger(__name__)

def meetup_details(request, meetup_slug): # 2nd parameter must match dynamic data from urls.py path call
  try:
    selected_meetup = Meetup.objects.get(slug=meetup_slug)
    if request.method == 'GET':
      # just display the detail page
      registration_form = RegistrationForm()     
    else:
      # form submission to add new participant
      registration_form = RegistrationForm(request.POST) # django will parse post data
      if registration_form.is_valid():
        user_email = registration_form.cleaned_data['email'] # get email entered in the form
        participant, _ = Participant.objects.get_or_create(email=user_email)
        # participant = registration_form.save() # this does all work of adding new participant to the database
        selected_meetup.participants.add(participant) # add new related record to meetup
        return redirect('confirm-registration', meetup_slug=meetup_slug)

    return render(request, 'meetups/meetup-detail.html',{
      'meetup_found': True,
      'meetup': selected_meetup,
      'form': registration_form,
    })
  except Exception as exception:
      logger.error(exception)
      return render(request, 'meetups/meetup-detail.html', {
        'meetup_found': False
      })

def confirm_registration(request, meetup_slug):
  meetup = Meetup.objects.get(slug=meetup_slug)
  return render(request, 'meetups/registration-success.html', {
    'organizer_email': meetup.organizer_email
  })