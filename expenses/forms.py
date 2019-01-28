from django import forms
#from expenses.models import UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Product

"""class UserForm(forms.Form):
 username = forms.CharField(max_length=25)
 password = forms.CharField(widget=forms.PasswordInput())

class Meta():
  model = User
  fields = "__all__"

class UserProfileInfoForm(forms.ModelForm):
 
 class Meta():
  model = UserProfileInfo
  fields = "__all__" """


 
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ExpenseUploadForm(forms.ModelForm):
    item = forms.CharField(max_length=30)
    price = forms.DecimalField()
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ('item','price','image', )
