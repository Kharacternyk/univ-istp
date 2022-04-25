from django.db import models


class Authors(models.Model):
    name = models.TextField(unique=True)
    country = models.ForeignKey("Countries", models.DO_NOTHING, blank=True, null=True)
    games = models.ManyToManyField("Games", through="Authorship")

    def __str__(self):
        return f"{self.name} ({self.country})"

    class Meta:
        managed = False
        verbose_name_plural = db_table = "authors"


class Categories(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = db_table = "categories"


class ClubMembers(models.Model):
    phone = models.BigIntegerField(unique=True)
    name = models.TextField(blank=True, null=True)
    play_sessions = models.ManyToManyField("PlaySessions", through="Players")

    def __str__(self):
        return f"{self.name} ({self.phone})"

    class Meta:
        managed = False
        verbose_name_plural = "club members"
        db_table = "club_members"


class Countries(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = db_table = "countries"


class GameLocalizations(models.Model):
    barcode = models.BigIntegerField(primary_key=True)
    game = models.ForeignKey("Games", models.DO_NOTHING)
    name = models.TextField()
    publishing_date = models.DateField(blank=True, null=True)
    in_catalog_since_date = models.DateField(blank=True, null=True)
    in_catalog_count = models.IntegerField()
    language = models.ForeignKey("Languages", models.DO_NOTHING, blank=True, null=True)
    publisher = models.ForeignKey(
        "Publishers", models.DO_NOTHING, blank=True, null=True
    )
    play_sessions = models.ManyToManyField("PlaySessions", through="PlaySessionItems")

    def __str__(self):
        return f"{self.name} ({self.barcode})"

    class Meta:
        managed = False
        verbose_name_plural = "game localization"
        db_table = "game_localizations"


class Games(models.Model):
    name = models.TextField()
    playtime = models.IntegerField(blank=True, null=True)
    min_players = models.IntegerField(blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = db_table = "games"


class Languages(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = db_table = "languages"


class PlaySessions(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.id} ({self.start_time} - {self.end_time})"

    class Meta:
        managed = False
        verbose_name_plural = "play sessions"
        db_table = "play_sessions"


class Publishers(models.Model):
    name = models.TextField(unique=True)
    country = models.ForeignKey(Countries, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.country})"

    class Meta:
        managed = False
        verbose_name_plural = db_table = "publishers"


class Authorship(models.Model):
    author = models.ForeignKey(Authors, models.DO_NOTHING)
    game = models.ForeignKey("Games", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "authorship"


class PlaySessionItems(models.Model):
    play_session = models.ForeignKey("PlaySessions", models.DO_NOTHING)
    game = models.ForeignKey(GameLocalizations, models.DO_NOTHING, db_column="barcode")
    count = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = "play_session_items"


class Players(models.Model):
    club_member = models.ForeignKey(ClubMembers, models.DO_NOTHING)
    play_session = models.ForeignKey(PlaySessions, models.DO_NOTHING)

    class Meta:
        managed = False
        verbose_name_plural = db_table = "players"
