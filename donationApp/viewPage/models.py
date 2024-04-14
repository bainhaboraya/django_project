from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_pictures')
    path = models.ImageField(upload_to='images')

    class Meta:
        app_label = 'viewPage'

    def __str__(self):
        return self.path.name

class Project(models.Model):
    pictures = models.ManyToManyField(Picture, blank=True, related_name='projects')
    title = models.CharField(max_length=255, default="Untitled Project")
    details = models.CharField(max_length=255, default="")
    current_fund = models.BigIntegerField(default=0)
    total_target = models.BigIntegerField(default=0)
    start_date = models.DateField(default=None)  
    end_date = models.DateField(default=None)    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  
    is_deleted = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], default='no')

    class Meta:
        app_label = 'viewPage'

    def __str__(self):
        return self.title

class Comment(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'viewPage'

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'viewPage'

class Report(models.Model):
    PROJECT = 'PR'
    COMMENT = 'CM'
    REPORT_CHOICES = [
        (PROJECT, 'Project'),
        (COMMENT, 'Comment')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_item_id = models.PositiveIntegerField()
    report_type = models.CharField(max_length=2, choices=REPORT_CHOICES)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'viewPage'