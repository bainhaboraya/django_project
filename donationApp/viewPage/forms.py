from django import forms
from .models import  Picture, Project, Comment, Report
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Project

class ProjectForm(forms.ModelForm):
    pictures = forms.ModelMultipleChoiceField(
        queryset=Picture.objects.all(),
        widget=FilteredSelectMultiple('Pictures', is_stacked=False)
    )

    class Meta:
        model = Project
        fields = '__all__'
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason']
