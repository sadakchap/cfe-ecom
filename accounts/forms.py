from django import forms
from django.contrib.auth import authenticate,get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    unm     = forms.CharField(
                label='Username',
                widget=forms.TextInput(attrs={'class':'form-control','autofocus':'on',})
    )
    pwrd    = forms.CharField(
                label='Password',
                widget=forms.PasswordInput(attrs={'class':'form-control'})
                )

    def clean(self,*args,**kwargs):
        unm     = self.cleaned_data.get('unm')
        pwrd    = self.cleaned_data.get('pwrd')

        if unm and pwrd:
            user = authenticate(username=unm,password=pwrd)
            if not user:
                raise forms.ValidationError('this username is not registered!')
            if not user.check_password(pwrd):
                raise forms.ValidationError('Incorrect Password!')
            if not user.is_active:
                raise forms.ValidationError('User Not active!')
        return super(UserLoginForm,self).clean(*args,**kwargs)


class UserSignUpForm(forms.ModelForm):
    username = forms.CharField(
                label='Username',
                widget=forms.TextInput(attrs={'class':'form-control','autofocus':'on'})
                )
    email   = forms.CharField(
                label='email',
                widget=forms.EmailInput(attrs={'class':'form-control'})
                )
    pwrd1   = forms.CharField(
                label='password',
                widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    pwrd2   = forms.CharField(
                label='password Confirm',
                widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ('username','email',)

    def clean_unm(self):
        unm     = self.cleaned_data.get('username')
        qs      = User.objects.filter(unm=unm)
        if qs.exists():
            raise forms.ValidationError('Username already exists!')
        return unm

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs    = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already Taken!')
        return email

    def clean_pwrd2(self):
        pwrd1 = self.cleaned_data.get('pwrd1')
        pwrd2 = self.cleaned_data.get('pwrd2')
        if pwrd1 and pwrd2 and pwrd1!=pwrd2:
            raise forms.ValidationError('Passwords dont match!')
        return pwrd2
