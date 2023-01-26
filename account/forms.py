from django import forms
from django.contrib.auth.forms import UserCreationForm 
from account.models import User

#create class when using the UserCreation form to manually 
#add the custom fields to the form 
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = "__all__"