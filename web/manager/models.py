# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Analysis(models.Model):
    article_id = models.AutoField(primary_key=True)
    keywords = models.TextField()  # This field type is a guess.
    comments = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Analysis'


class Article(models.Model):
    type = models.IntegerField()
    journal = models.IntegerField()
    reporters = models.CharField(max_length=30, blank=True, null=True)
    published_at = models.DateTimeField()
    title = models.CharField(max_length=300)
    raw_contents = models.TextField()
    contents = models.TextField(blank=True, null=True)
    journal_article_id = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=500)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Article'


class Celebrity(models.Model):
    name = models.CharField(max_length=20)
    profile_img = models.TextField(blank=True, null=True)
    current_title = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Celebrity'


class Comment(models.Model):
    article_id = models.IntegerField(unique=True)
    type = models.IntegerField()
    contents = models.CharField(max_length=500)
    celebrity_id = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Comment'


class Keyword(models.Model):
    celebrity_id = models.IntegerField()
    text = models.CharField(max_length=30)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Keyword'


class Taskchain(models.Model):
    chain = models.TextField()
    created_at = models.DateTimeField()
    last_used_at = models.DateTimeField()
    example_url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TaskChain'


class Work(models.Model):
    taskchain_id = models.IntegerField()
    celebrity_id = models.IntegerField()
    known_article_count = models.IntegerField()
    parsed_article_count = models.IntegerField()
    analysed_article_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Work'
