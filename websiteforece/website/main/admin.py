from django.contrib import admin
from .models import Profile, KPI
from openpyxl import Workbook
from django.http import HttpResponse

class KPIAdmin(admin.ModelAdmin):
    list_display = ('user', 'co_authors', 'journal_name', 'article_title', 'volume_issue', 'pages', 'pub_date', 'impact_factor', 
                    'published', 'indexed', 'index_info', 'doi', 'h_index', 'issn')  # Example fields
    
    actions = ['export_to_excel']

    def export_to_excel(self, request, queryset):
        wb = Workbook()
        ws = wb.active
        ws.title = "KPIs"


        headers = ['Attribute', 'Value']
        ws.append(headers)
        
        for kpi in queryset:
            ws.append(['Faculty', str(kpi.user)])
            ws.append(['co_authors', kpi.co_authors])
            ws.append(['journal_name', kpi.journal_name])
            ws.append(['article_title', kpi.article_title])
            ws.append(['volume_issue', kpi.volume_issue])
            ws.append(['pages', kpi.pages])
            ws.append(['pub_date', kpi.pub_date])
            ws.append(['impact_factor', kpi.impact_factor])
            ws.append(['published', kpi.published])
            ws.append(['indexed', kpi.indexed])
            ws.append(['index_info', kpi.index_info])
            ws.append(['doi', kpi.doi])
            ws.append(['h_index', kpi.h_index])
            ws.append(['issn', kpi.issn])
            ws.append([])  # Add a blank row for separation

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="kpis.xlsx"'
        wb.save(response)

        return response

    export_to_excel.short_description = "Download Selected KPIs as Excel"

admin.site.register(KPI, KPIAdmin)
admin.site.register(Profile)
