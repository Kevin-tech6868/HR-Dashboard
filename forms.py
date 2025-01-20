# myapp/forms.py
from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job_title', 'location', 'about_role', 'requirements']
additional_fields = forms.CharField(widget=forms.HiddenInput(), required=False) 