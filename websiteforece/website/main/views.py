from django.shortcuts import render, redirect
from .models import Profile, KPI
from .forms import ProfileForm, KPIForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    kpis = KPI.objects.filter(user=request.user)
    return render(request, 'profile.html', {'form': form, 'kpis': kpis})

@login_required
def kpi_submission(request):
    if request.method == 'POST':
        form = KPIForm(request.POST)
        if form.is_valid():
            kpi = form.save(commit=False)
            kpi.user = request.user
            kpi.save()
            return redirect('profile')
    else:
        form = KPIForm()

    return render(request, 'kpi_submission.html', {'form': form})

@login_required
def download_kpi(request):
    import csv
    from django.http import HttpResponse

    kpis = KPI.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kpis.csv"'

    writer = csv.writer(response)
    writer.writerow(['co_authors', 'journal_name', 'article_title', 'volume_issue', 'pages', 'pub_date', 'impact_factor', 
                  'published', 'indexed', 'index_info', 'doi', 'h_index', 'issn'])

    for kpi in kpis:
        writer.writerow([kpi.co_authors, kpi.journal_name, kpi.article_title, kpi.volume_issue, kpi.pages, kpi.pub_date, kpi.impact_factor,
                         kpi.published, kpi.indexed, kpi.index_info, kpi.doi, kpi.h_index, kpi.issn])

    return response
