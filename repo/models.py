from django.db import models



class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    html_url = models.URLField()
    topics = models.ManyToManyField(Topic)
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    avatar_url = models.URLField()
    # address=models.CharField(max_length=100)
    userbio=models.CharField(max_length=100,null=True)
    userlocation=models.CharField(max_length=100,null=True)
    repositories = models.ManyToManyField(Repository)
    usertwitter=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username
    