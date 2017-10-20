# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
from Doparti.models import MyRegistrationForm
from django.contrib.auth import authenticate, login

'''
# Create your views here.
#def register(request):
#    if request.method =='POST':
#        form = MyRegistrationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('registration_complete.html')

#    else:
#        form = MyRegistrationForm()

#        args = {'form':form}
#        return render(request, 'accounts/registration_form.html', args)
'''

def base(request):
    return render(request, 'main.html')


def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_complete.html')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    print args
    return render(request, 'accounts/registration_form.html', args)

"""
def login_funcion(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect(request,'main.html')
    else:
        # Return an 'invalid login' error message.
        message.error(request, 'Error')






def login(request, user, backend=None):
    session_auth_hash = ''
    if user is None:
        user = request.user
    if hasattr(user, 'get_session_auth_hash'):
        session_auth_hash = user.get_session_auth_hash()

    if SESSION_KEY in request.session:
        if _get_user_session_key(request) != user.pk or (
                session_auth_hash and
                not constant_time_compare(request.session.get(HASH_SESSION_KEY, ''), session_auth_hash)):
            # To avoid reusing another user's session, create a new, empty
            # session if the existing session corresponds to a different
            # authenticated user.
            request.session.flush()
    else:
        request.session.cycle_key()

    try:
        backend = backend or user.backend
    except AttributeError:
        backends = _get_backends(return_tuples=True)
        if len(backends) == 1:
            _, backend = backends[0]
        else:
            raise ValueError(
                'You have multiple authentication backends configured and '
                'therefore must provide the `backend` argument or set the '
                '`backend` attribute on the user.'
            )

    request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
    request.session[BACKEND_SESSION_KEY] = backend
    request.session[HASH_SESSION_KEY] = session_auth_hash
    if hasattr(request, 'user'):
        request.user = user
    rotate_token(request)
    user_logged_in.send(sender=user.__class__, request=request, user=user)
        
"""
