from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label = "用戶名稱", max_length=128)
    password = forms.CharField(label = "用戶密碼", max_length=256, widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label="用戶名稱", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label = "密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="確認密碼", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="電子郵件信箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    common_store = forms.CharField(label="常用取貨門市", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

