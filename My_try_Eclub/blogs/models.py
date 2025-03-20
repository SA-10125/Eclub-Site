from django.db import models as m
from django.contrib.auth.models import User

# Create your models here.

class Blog(m.Model):
    title = m.CharField(max_length=100)
    desc = m.CharField(max_length=500)
    content = m.TextField(blank=False,null=False)
    date_posted = m.DateTimeField(auto_now_add=True)
    author = m.ForeignKey(User, on_delete=m.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author}"