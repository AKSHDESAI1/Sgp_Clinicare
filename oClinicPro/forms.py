from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django.forms import ValidationError


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        print('email', email)
        user = None
        try:
            user = User.objects.get(email=email)
        except:
            return email

        if user is not None:
            raise ValidationError(
                'Email-Id is already exists. please try with another one')


class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=50, required=True, label='Email')

    def clean(self):
        email = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = None
        try:
            user = User.objects.get(email=email)
            result = authenticate(username=user.username, password=password)
            if result is not None:
                login(self.request, result)
                return result
            else:
                raise ValidationError("Email or password invalid")
        except:
            raise ValidationError("Email or password invalid")

class UserProfileForm(UserChangeForm):
    password = None
    username = forms.CharField(widget = forms.TextInput(attrs = {'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': True}))
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class AdminProfileForm(UserChangeForm):
    Password = None
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'user_permissions', 'groups', 'date_joined', 'is_active', 'is_staff', 'is_superuser']