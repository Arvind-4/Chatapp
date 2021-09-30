from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm

from .models import Profile

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(min_length=6, max_length=20,
                               widget=forms.TextInput(attrs={
                                   'class': 'bg-gray-200 border-2 border-gray-100 focus:outline-none bg-gray-100 block w-full py-2 px-4 rounded-lg focus:border-gray-700',
                                   'placeholder': 'Enter your Username...',
                                   'label': ''
                               }))
    password = forms.CharField(min_length=8, max_length=20,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'bg-gray-200 border-2 border-gray-100 focus:outline-none bg-gray-100 block w-full py-2 px-4 rounded-lg focus:border-gray-700',
                                   'placeholder': 'Enter your Password...',
                                   'label': '',
                               }))

    def clean_username(self, *args, **kwargs):
        username_form = self.cleaned_data.get('username')
        obj = User.objects.filter(username__iexact=username_form)
        if not obj.exists():
            information = "The Username does't Exists!"
            raise forms.ValidationError(information)
        # if not request.user.is_authenticated:
        #     information = 'The Username is Registered. Please Register to Continue.'
        #     raise forms.ValidationError(information)
        return username_form


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(min_length=8, max_length=20,
                               widget=forms.TextInput(attrs={
                                   'class': 'bg-gray-200 border-2 border-gray-100 focus:outline-none bg-gray-100 block w-full py-2 px-4 rounded-lg focus:border-gray-700',
                                   'placeholder': 'Enter your Username...',
                               }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'bg-gray-200 border-2 border-gray-100 focus:outline-none bg-gray-100 block w-full py-2 px-4 rounded-lg focus:border-gray-700',
        'placeholder': 'Enter your Email...'
    }))
    password1 = forms.CharField(min_length=8, max_length=20,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'bg-gray-200 border-2 border-gray-100 focus:outline-none bg-gray-100 block w-full py-2 px-4 rounded-lg focus:border-gray-700',
                                    'placeholder': 'Enter a Password...'
                                }))
    password2 = forms.CharField(min_length=8, max_length=20,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'bg-gray-200 border-2 border-gray-100 focus:outline-none bg-gray-100 block w-full py-2 px-4 rounded-lg focus:border-gray-700',
                                    'placeholder': 'Re-Enter your Password...',
                                }))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    def clean_username(self):
        username_form = self.cleaned_data.get('username')
        obj = User.objects.all().filter(username__iexact=username_form)
        if obj.exists():
            information = 'The Username Already Exists!'
            raise forms.ValidationError(information)
        return username_form

    def clean_email(self):
        email_form = self.cleaned_data.get('email')
        obj = User.objects.all().filter(email=email_form)
        if obj.exists():
            information = 'The Email Already Exists!. Try Logging In.'
            raise forms.ValidationError(information)
        return email_form

    def clean_password2(self):
        password1_form = self.cleaned_data.get('password1')
        password2_form = self.cleaned_data.get('password2')
        if password1_form != password2_form:
            information = "The Passwords didn't Match!"
            raise forms.ValidationError(information)
        return password2_form


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent',
        'placeholder': 'Enter you Registered Email ...',
        }))

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-5 py-1 text-gray-700 bg-gray-300 rounded focus:outline-none focus:bg-white',
        'placeholder': 'Enter your Old Password ...'
    }))
    new_password1 = forms.CharField(min_length=6, max_length=20,
                                    widget=forms.PasswordInput(
                                        attrs={
                                            'class': 'w-full px-5 py-1 text-gray-700 bg-gray-300 rounded focus:outline-none focus:bg-white',
                                            'placeholder': 'Enter your New Password ...'

                                        }))
    new_password2 = forms.CharField(min_length=6, max_length=20,
                                    widget=forms.PasswordInput(
                                        attrs={
                                            'class': 'w-full px-5 py-1 text-gray-700 bg-gray-300 rounded focus:outline-none focus:bg-white',
                                            'placeholder': 'Enter your New Password Again ...'

                                        }))

    class Meta:
        model = User,
        fields = (
            'old_password',
            'new_password1',
            'new_password2',
        )

class EditProfileForm(forms.ModelForm):
    user_image = forms.ImageField(label='Profile Image', required=False, widget=forms.FileInput(attrs={
        # 'placeholder': 'Add your Profile Image',
        'onchange': "loadFile(event)",
    }))
    user_banner = forms.ImageField(label='Banner Image', required=False, widget=forms.FileInput(
        attrs={
        'onchange': "loadFile_banner(event)",
    }
    ))
    bio = forms.CharField(label='Bio', widget=forms.Textarea(attrs={
        'placeholder': 'Enter an Awesome Bio ...',
        'rows': '2',
    }))
    instagram_url = forms.URLField(label='Insta Url', required=False, widget=forms.URLInput(attrs={
        'placeholder': 'Enter your Instagram url ...',
    }))
    linkedin_url = forms.URLField(label='Linkedin Url', required=False, widget=forms.URLInput(attrs={
        'placeholder': 'Enter your Linkedin url ...',
    }))
    github_url = forms.URLField(label='Github Url', required=False, widget=forms.URLInput(attrs={
        'placeholder': 'Enter your Github url ...',
    }))

    class Meta:
        model = Profile
        fields = (
            'user_image',
            'user_banner',
            'bio',
            'instagram_url',
            'linkedin_url',
            'github_url',
        )

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'flex-1 py-2 border-b-2 border-gray-400 focus:border-green-400 text-gray-600 placeholder-gray-400 outline-none'