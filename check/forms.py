from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from .models import Profile, Event


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',
                          widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                        widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')





class UserProfileForm(forms.ModelForm):
    first_name = forms.RegexField(required = True,  regex = "^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z0-9\s]{0,}$",
                               error_messages = {"invalid":"Please Enter Valid Name.","required":"Please Enter Name."})
    last_name = forms.RegexField(required = True,  regex = "^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$",
                               error_messages = {"invalid":"Please Enter Valid Name.","required":"Please Enter Name."})
    mobile=forms.RegexField(regex=r'^\+?1?\d{9,18}$',
                            error_messages = {"invalid":"Please Enter Valid Mobile Number.","required":"Please Enter Mobile Number."})
    city = forms.RegexField(required = True,  regex = "^[A-Za-z\s]{3,10}$",
                               error_messages = {"invalid":"Please Enter Valid City Name.","required":"Please Enter City Name."})
    state = forms.RegexField(required = True,  regex = "^[A-Za-z\s]{3,50}$",
                               error_messages = {"invalid":"Please Enter Valid State Name.","required":"Please Enter State Name."})
    country = forms.RegexField(required = True,  regex = "^[A-Za-z\s]{3,50}$",
                               error_messages = {"invalid":"Please Enter Valid Country Name.","required":"Please Enter Country Name."})
    Profile_Image =forms.ImageField(required=False, error_messages = {"invalid":"please upload profile image.","required":"Please upload profile image."})
    class Meta:
      model = Profile
      fields=('first_name', 'last_name', 'mobile', 'city', 'state', 'country','Profile_Image')



class EventForm(forms.ModelForm):
    # date_time = DateTimeField(widget=forms.widgets.DateTimeInput(format="%m %d %y %H:%M"))
    # event_date=forms.DateField(widget = AdminDateWidget)
    # image =forms.ImageField(required=False, error_messages = {"invalid":"please upload profile image.","required":"Please upload profile image."})
    class Meta:
       model = Event
       fields=('event_name','event_date', 'address', 'image')

# class EventAttndiesForm(forms.ModelForm):
#     # date_time = DateTimeField(widget=forms.widgets.DateTimeInput(format="%m %d %y %H:%M"))
#     # event_date=forms.DateField(widget = AdminDateWidget)
#     # image =forms.ImageField(required=False, error_messages = {"invalid":"please upload profile image.","required":"Please upload profile image."})
#     class Meta:
#        model = Event
#       fields=('')
