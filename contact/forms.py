from django import forms

class ContactForm(forms.Form):
    name  = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','autofocus':'on',}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    msg   = forms.CharField(label='Message',
                                widget=forms.Textarea(
                                    attrs={'class':'form-control',}),
                                required=True
                                )
