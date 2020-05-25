from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser, Doctor, Patient

class Register(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ['full_name', 'username', 'email', 'password1', 'password2', 'is_doctor', 'is_patient']


class DoctorProfile(forms.ModelForm):

    expertise = forms.CharField()

    class Meta:
        model = Doctor
        fields = ['expertise']

class DoctorInfo(forms.ModelForm):

    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = NewUser
        fields = ['username', 'email']


class PatientProfile(forms.ModelForm):

    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = NewUser
        fields = ['username', 'email']


class PatientSymptoms(forms.ModelForm):

    symptoms = forms.CharField()
    
    class Meta:
        model = Patient
        fields = ['symptoms']
