from django import forms 
from .models import UserProfile

class AddUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'