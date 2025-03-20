from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test #this is used to restrict pages that need login or a certain login.

@login_required(login_url='login') #must be logged in to access events.
def render_temp_events(request):
    if request.user.is_authenticated: #precautionary even though we have the login_required decorator.
        return HttpResponse("Events will come here.")
    else:
        return redirect('login')

#get the notify buttonw working.
#load blogs like we did events in dajango_try and get the timer working for each.
# each event should be a get send to a pk page. (simple like in dajango) 
#get the social media links working