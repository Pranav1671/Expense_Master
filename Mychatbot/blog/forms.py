from django import forms
from .models import UserProfile1

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile1
        fields = ['name', 'gender', 'dob', 'phone', 'email', 'profile_pic', 'logpass']
