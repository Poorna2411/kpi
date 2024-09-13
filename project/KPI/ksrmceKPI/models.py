from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_images/', default='default_profile.jpg')  # Add this field

    def __str__(self):
        return self.user.username

class KPI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name_of_author = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    co_authors = models.CharField(max_length=100)  # Yes/No field
    name_of_journal = models.CharField(max_length=200)
    title_of_article = models.CharField(max_length=200)
    volume_issue = models.CharField(max_length=50)  # Vol. No., Issue No.
    pages_no = models.CharField(max_length=50)
    publication_date = models.DateField()
    impact_factor_sjr = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    published = models.BooleanField(default=False)  # Yes/No field
    indexed = models.BooleanField(default=False)  # Yes/No field
    sci_scopus_wos = models.CharField(max_length=100, blank=True, null=True)  # For SCI/SCOPUS/WOS
    doi = models.CharField(max_length=100, blank=True, null=True)
    h_index = models.IntegerField(blank=True, null=True)
    issn_no = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.name_of_author} - {self.title_of_article}'

