from django import forms
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField
from .models import Profile
from .models import KPI

class CaptchaLoginForm(AuthenticationForm):
    captcha = CaptchaField()

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['designation', 'department', 'faculty_id', 'profile_image']


class KPIForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = [
            'name_of_author', 'designation', 'co_authors', 'name_of_journal', 'title_of_article',
            'volume_issue', 'pages_no', 'publication_date', 'impact_factor_sjr', 'published',
            'indexed', 'sci_scopus_wos', 'doi', 'h_index', 'issn_no'
        ]
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
