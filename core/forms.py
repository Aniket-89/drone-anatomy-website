from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your Name'})
        
    )
    email = forms.EmailField(
        label='Email',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Your Email'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'})
    )


class SubscriberForm(forms.Form):
    email = forms.EmailField()