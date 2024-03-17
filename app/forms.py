from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email', 'phone_number') # specify the fields to be included in the form

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user