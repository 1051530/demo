from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['姓', '名', 'email', '地址',
                  '郵遞區號', '城市']
