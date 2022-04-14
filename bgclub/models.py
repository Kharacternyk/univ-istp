# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authors(models.Model):
    name = models.TextField(unique=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Authorship(models.Model):
    author = models.ForeignKey(Authors, models.DO_NOTHING)
    game = models.ForeignKey('Games', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authorship'


class Categories(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'categories'


class ClubMembers(models.Model):
    phone = models.IntegerField(unique=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club_members'


class Countries(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'countries'


class GameLocalizations(models.Model):
    barcode = models.IntegerField(primary_key=True)
    publishing_date = models.DateField(blank=True, null=True)
    in_catalog_since_date = models.DateField(blank=True, null=True)
    in_catalog_count = models.IntegerField()
    language = models.ForeignKey('Languages', models.DO_NOTHING, blank=True, null=True)
    publisher = models.ForeignKey('Publishers', models.DO_NOTHING, blank=True, null=True)
    game = models.ForeignKey('Games', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'game_localizations'


class Games(models.Model):
    playtime = models.IntegerField(blank=True, null=True)
    min_players = models.IntegerField(blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Languages(models.Model):
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'languages'


class PlaySessionItems(models.Model):
    play_session = models.ForeignKey('PlaySessions', models.DO_NOTHING)
    barcode = models.ForeignKey(GameLocalizations, models.DO_NOTHING, db_column='barcode')
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'play_session_items'


class PlaySessions(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'play_sessions'


class Players(models.Model):
    club_member = models.ForeignKey(ClubMembers, models.DO_NOTHING)
    play_session = models.ForeignKey(PlaySessions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'players'


class Publishers(models.Model):
    name = models.TextField(unique=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publishers'
