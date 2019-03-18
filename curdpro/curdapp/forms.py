from django import forms
from .models import Productdata

class insertingdataform(forms.ModelForm):
    # product_number = forms.IntegerField(
    #     label="enter product number",
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'productnumber'
    #         }
    #     )
    # )
    class Meta:
        model=Productdata
        fields="__all__"
class updatingdataform(forms.Form):
    product_number=forms.IntegerField(
        label="enter product number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'productnumber'
            }
        )
    )
    product_cost=forms.IntegerField(
        label="enter product cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'productcost'
            }
        )
    )

class deletingdataform(forms.Form):
    product_number = forms.IntegerField(
        label="enter product number",
    widget = forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'productnumber'
        }
    )
    )