from django import forms
from .models import Profile, KPI

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['designation', 'department', 'faculty_id']

class KPIForm(forms.ModelForm):
    class Meta:
        model = KPI
        fields = ['user','co_authors', 'journal_name', 'article_title', 'volume_issue', 'pages', 'pub_date', 'impact_factor', 
                  'published', 'indexed', 'index_info', 'doi', 'h_index', 'issn']
