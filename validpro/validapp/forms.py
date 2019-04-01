from django import forms
from .models import regddata

class regd_form(forms.Form):
    username=forms.CharField(
        label="enter username",
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'username'
            }
        )
    )

    email=forms.EmailField(
        label="enter email",
        widget=forms.EmailInput(
            attrs={
            'class':'form-control',
            'placeholder':'email'
            }
        )
    )

    mobile=forms.IntegerField(
        label="enter mobile number",
        widget=forms.NumberInput(
            attrs={
            'class':'form-control',
            'placeholder':'mobile'
            }
        )
    )

    def clean_username(self):
        user_name=self.cleaned_data.get("username")
        g=regddata.objects.filter(username=user_name)
        if g.exists():
            raise forms.ValidationError("username already available")
        return user_name

    def clean_email(self):
        email_id=self.cleaned_data.get("email")
        e=regddata.objects.filter(email=email_id)
        if e.exists():
            raise forms.ValidationError("email already available")
        return email_id

    def clean_mobile(self):
        mobile_number=self.cleaned_data.get("mobile")
        m=regddata.objects.filter(mobile=mobile_number)
        if m.exists():
            raise forms.ValidationError("mobile number already registered")
        elif len(str(mobile_number)) != 10:
            raise forms.ValidationError("please enter valid mobile number")
        return mobile_number







