from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goals = models.TextField()
    progress = models.IntegerField(default=0)

    class Meta:
        app_label = 'storymanagerdjango'


class Character(models.Model):
    name = models.CharField(max_length=100)
    attributes = models.JSONField()
    description = models.TextField()
    background = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='characters')

    class Meta:
        app_label = 'storymanagerdjango'

class Scenario(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='scenarios')

    class Meta:
        app_label = 'storymanagerdjango'


class PlotPoint(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='plot_points')

    class Meta:
        app_label = 'storymanagerdjango'


class Scene(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='scenes')

    class Meta:
        app_label = 'storymanagerdjango'


class Note(models.Model):
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='notes')

    class Meta:
        app_label = 'storymanagerdjango'
