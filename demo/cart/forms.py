from django import forms


class CartAddProductForm(forms.Form):
    CHOICES = [(i, str(i)) for i in range(1, 21)]
    數量 = forms.TypedChoiceField(choices=CHOICES, coerce=int)
    更新 = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)




