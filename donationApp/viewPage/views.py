from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Comment, Report
from .forms import ProjectForm, CommentForm, ReportForm


def home(request):
    projects = Project.objects.all().prefetch_related('pictures')
    return render(request, 'viewPage/home.html', {'projects': projects})

# views.py
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    comments = project.comments.all().prefetch_related('replies')
    comment_form = CommentForm()
    report_form = ReportForm()

    if request.method == 'POST':
        if 'comment_form' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.project = project
                new_comment.user = request.user
                new_comment.save()
                return redirect('viewPage:project_detail', project_id=project_id)
        elif 'report_form' in request.POST:
            report_form = ReportForm(request.POST)
            if report_form.is_valid():
                new_report = report_form.save(commit=False)
                new_report.user = request.user
                new_report.reported_item_id = project_id
                new_report.report_type = Report.PROJECT
                new_report.save()
                return redirect('viewPage:report_page')

    return render(request, 'viewPage/project_detail.html', {'project': project, 'comments': comments, 'comment_form': comment_form, 'report_form': report_form})
def report_page(request):
    return render(request, 'viewPage/report_page.html')
# def project_detail(request, project_id):
#     project = get_object_or_404(Project, pk=project_id)
#     comments = Comment.objects.filter(project=project)
#     comment_form = CommentForm()

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.project = project
#             comment.user = request.user
#             comment.save()
#             return redirect('project_detail', project_id=project_id)

#     return render(request, 'project_detail.html', {'project': project, 'comments': comments, 'comment_form': comment_form})

