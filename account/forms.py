from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 255, widget = forms.TextInput(attrs = {
		'class':'form-control',
		'placeholder':'enter your name'
		}))
	password = forms.CharField(max_length = 255, widget = forms.PasswordInput(attrs = {
		'class':'form-control',
		'placeholder':'enter your password'
		}))

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'})
    )