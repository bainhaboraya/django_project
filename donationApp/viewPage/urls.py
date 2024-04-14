from django.urls import path
from .views import home, project_detail,report_page

app_name = 'viewPage'

urlpatterns = [
    path('', home, name='home'),
    path('project/<int:project_id>/', project_detail, name='project_detail'),
    path('report/', report_page, name='report_page'),
    
]
