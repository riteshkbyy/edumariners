from django import forms


class ContactForm(forms.Form):
    # Name = forms.CharField(label='Name', required=True , max_length=100)
    from_email = forms.EmailField(label='Your Email', required=True)
    subject = forms.CharField(label='Subject', required=True)
    # country = forms.CharField(label='Country')
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)
    class Meta:

        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }


