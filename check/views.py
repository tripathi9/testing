from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from check.forms import *
from .models import Profile
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotAllowed
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

# Create your views here.


def main(request):
    context={

    "title":"WELCOME"
    }

    return render(request, 'check/base.html', context)


def account(request):
       user=request.user
       userid=user.id
       event_list=Event.objects.filter(userid=userid)
    #    event_lis=Event.objects.all()
    #    print (event_lis)
       context={"event_list":event_list,
       "title":"Your Events List",
       "request":request}
       return render(request, 'check/profile.html', context)

def create_profile(request):

    form = UserProfileForm(request.POST or None, request.FILES or None)

    if form.is_valid():

        instance=form.save(commit=False)
        print (form.cleaned_data.get("first_name"))
        instance.userid=request.user
        instance.save()
        return HttpResponseRedirect('/accounts/profile')
    else:
        print("invalid form")

    context = {
    "form":form,

    }

    return render(request, 'check/user_profile.html', context)




def profile_update(request, id=None):


    user=request.user
    userid=user.id
    profile_list=get_object_or_404(Profile, userid=userid)
    print("hello1")
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None, request.FILES or None, instance = profile_list)
        print("hello2")
        if form.is_valid():
            profile_list=form.save(commit=False)
            print (form.cleaned_data.get("first_name"))
            profile_list.save()
            context={
            "profile_list":profile_list,
            "title":profile_list.first_name,
            "form":form,
        }
    else:
        print("hello3")
        form = UserProfileForm(request.POST or None, instance = profile_list)
        print("hello4")
        context={
        "profile_list":profile_list,
        "title":profile_list.first_name,
        "form":form,
    }
        return render(request, 'check/user_profile.html', context)
    return render(request, 'check/user_profile.html', context)


def event_create(request):
    print (request.POST)
    form = EventForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        print (form.cleaned_data.get("event_name"))

        instance.userid=request.user
        instance.save()
        # messages.success(request,"Succesfuly create")
        return HttpResponseRedirect('/accounts/profile')
        # return render(request, 'check/profile.html', context)

    else:
        print("invalid form")
        print(form.errors)
        # messages.error(request, "Not able to  create")
    context = {
        "form":form,
        }
    return render(request, 'check/event.html', context)

def event_update(request, id=None):

    instance=get_object_or_404(Event, id=id)

    form = EventForm(request.POST or None, instance = instance)

    if form.is_valid():
        instance=form.save(commit=False)
        print (form.cleaned_data.get("event_name"))
        instance.save()
        return HttpResponseRedirect('/accounts/profile')
    context={
       "instance":instance,
       "title":instance.event_name,
       "form":form,

    }
    
    return render(request, 'check/event.html', context)



def event_list(request):
    user=request.user
    userid=user.id
    event_list=Event.objects.exclude(userid=userid)
    context={"event_list":event_list,
    "title":"Event List"}
    return render(request, 'check/events_list.html', context)





def logout_page(request):
    print("logout")
    logout(request)
    return HttpResponseRedirect('/')

@csrf_exempt
def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect('/register/userprofile')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('check/register.html',variables)
