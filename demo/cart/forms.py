from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    數量 = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    更新 = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

