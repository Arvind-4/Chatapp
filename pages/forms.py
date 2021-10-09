from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring',
        'placeholder': 'Enter your Name ...',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring',
        'placeholder': 'Enter your Email ...',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'block w-full h-40 px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-500 dark:focus:border-blue-500 focus:outline-none focus:ring',
        'placeholder': 'Your Message ...',
    }))
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message'
        )

    def clean_name(self, *args, **kwargs):
        form_name = self.cleaned_data.get('name')
        qs = Contact.objects.filter(name=form_name)
        if qs.exists():
            information = 'You have Already filled the Form. Please wait we will Respond as soon as Possible. Thanks'
            raise forms.ValidationError(information)
        return form_name

    def clean_email(self, *args, **kwargs):
        form_email = self.cleaned_data.get('email')
        qs = Contact.objects.filter(email=form_email)
        if qs.exists():
            information = 'You have Already filled the Form. Please wait we will Respond as soon as Possible. Thanks'
            raise forms.ValidationError(information)
        return form_email