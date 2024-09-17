from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class KPI(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    co_authors = models.BooleanField(default=False)
    journal_name = models.CharField(max_length=200)
    article_title = models.CharField(max_length=200)
    volume_issue = models.CharField(max_length=50)
    pages = models.CharField(max_length=50)
    pub_date = models.DateField()
    impact_factor = models.FloatField(null=True, blank=True)
    published = models.BooleanField(default=False)
    indexed = models.BooleanField(default=False)
    index_info = models.CharField(max_length=200, blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)
    h_index = models.IntegerField(null=True, blank=True)
    issn = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.article_title} by {self.user.username}"
