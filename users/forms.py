from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserRegisterForm(UserCreationForm):

    # modify the email fild
    email = forms.EmailField()

# this is how we can modify the password2 lable
    # password2 = forms.CharField(label="Confirm Password (again)")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = ['username', 'email'] #this is also current becauue pass1 and pass2 is comming form usercreation foms so isko fields me add krni ki jarurat nhi he

        # --> is tarah se hum lable ko change kr skte he
        # labels = {'email': 'Email'}


# --> ish tarah se hum multiple field add kr skte he
# fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']


class UserUpdatefrom(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
