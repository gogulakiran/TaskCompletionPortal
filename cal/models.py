from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Task(models.Model):
    eid=models.IntegerField()
    task_name=models.CharField(max_length=200)
    date=models.DateField()
    status=models.CharField(max_length=100)
    duration=models.IntegerField()
