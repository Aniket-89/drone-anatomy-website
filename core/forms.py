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


class CareerForm(forms.Form):
    name = forms.CharField(
        label='Name',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name...'})
        
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email...'})
    )
    position = forms.CharField(
        label='Position', 
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Applying For Position...'})
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'})
    )
    resume = forms.FileField(
        required=True,
        label='Resume',
        # widget=forms.ClearableFileInput(attrs={'multiple': False})
        )
    
    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if not resume.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
            if resume.size > 2 * 1024 * 1024:  # 2 MB limit
                raise forms.ValidationError("The file size should not exceed 2 MB.")
        return resume