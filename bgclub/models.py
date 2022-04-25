from django.db import models


class Author(models.Model):
    name = models.TextField("ім'я", unique=True)
    country = models.ForeignKey(
        "Country", models.CASCADE, blank=True, null=True, verbose_name="країна"
    )
    games = models.ManyToManyField("Game", through="Authorship", verbose_name="ігри")

    def __str__(self):
        return f"{self.name} [{self.country}]"

    class Meta:
        managed = False
        verbose_name_plural = "автори"
        verbose_name = "автор"
        db_table = "authors"


class Category(models.Model):
    name = models.TextField("ім'я", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = "категорії"
        verbose_name = "категорія"
        db_table = "categories"


class ClubMember(models.Model):
    phone = models.PositiveBigIntegerField("телефон", unique=True)
    name = models.TextField("ім'я", blank=True, null=True)
    play_sessions = models.ManyToManyField(
        "PlaySession", through="Player", verbose_name="ігрові сеанси"
    )

    def __str__(self):
        return f"{self.name} [{self.phone}]"

    class Meta:
        managed = False
        verbose_name_plural = "гравці клубу"
        verbose_name = "гравець клубу"
        db_table = "club_members"


class Country(models.Model):
    name = models.TextField("ім'я", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = "країни"
        verbose_name = "країна"
        db_table = "countries"


class GameLocalization(models.Model):
    barcode = models.PositiveBigIntegerField("штрих-код", primary_key=True)
    game = models.ForeignKey("Game", models.CASCADE, verbose_name="гра")
    name = models.TextField("ім'я")
    publishing_date = models.DateField("дата видання", blank=True, null=True)
    in_catalog_since_date = models.DateField(
        "дата появи у каталозі", blank=True, null=True
    )
    in_catalog_count = models.PositiveIntegerField("наявна кількість у каталозі")
    language = models.ForeignKey(
        "Language", models.CASCADE, blank=True, null=True, verbose_name="мова"
    )
    publisher = models.ForeignKey(
        "Publisher", models.CASCADE, blank=True, null=True, verbose_name="видавець"
    )
    play_sessions = models.ManyToManyField(
        "PlaySession", through="PlaySessionItem", verbose_name="ігрові сеанси"
    )

    def __str__(self):
        return f"{self.name} [{self.barcode}]"

    class Meta:
        managed = False
        verbose_name_plural = "локалізації ігор"
        verbose_name = "локалізація гри"
        db_table = "game_localizations"


class Game(models.Model):
    name = models.TextField("ім'я")
    playtime = models.PositiveIntegerField("орієнтовний час гри", blank=True, null=True)
    min_players = models.PositiveIntegerField(
        "мінімальна кількість гравців", blank=True, null=True
    )
    max_players = models.PositiveIntegerField(
        "максимальна кількість гравців", blank=True, null=True
    )
    category = models.ForeignKey(
        Category, models.CASCADE, blank=True, null=True, verbose_name="категорія"
    )
    authors = models.ManyToManyField(
        "Author", through="Authorship", verbose_name="автори"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = "ігри"
        verbose_name = "гра"
        db_table = "games"


class Language(models.Model):
    name = models.TextField("ім'я", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        managed = False
        verbose_name_plural = "мови"
        verbose_name = "мова"
        db_table = "languages"


class PlaySession(models.Model):
    start_time = models.DateTimeField("час початку")
    end_time = models.DateTimeField("час кінця")

    def __str__(self):
        return f"{self.id} [{self.start_time} — {self.end_time}]"

    class Meta:
        managed = False
        verbose_name_plural = "ігрові сеанси"
        verbose_name = "ігровий сеанс"
        db_table = "play_sessions"


class Publisher(models.Model):
    name = models.TextField("ім'я", unique=True)
    country = models.ForeignKey(
        Country, models.CASCADE, blank=True, null=True, verbose_name="країна"
    )

    def __str__(self):
        return f"{self.name} [{self.country}]"

    class Meta:
        managed = False
        verbose_name_plural = "видавці"
        verbose_name = "видавець"
        db_table = "publishers"


class Authorship(models.Model):
    author = models.ForeignKey(Author, models.CASCADE)
    game = models.ForeignKey("Game", models.CASCADE)

    def __str__(self):
        return "Гра/Сеанс"

    class Meta:
        managed = False
        verbose_name = "авторство"
        verbose_name_plural = "авторство"
        db_table = "authorship"


class PlaySessionItem(models.Model):
    play_session = models.ForeignKey("PlaySession", models.CASCADE)
    game = models.ForeignKey(GameLocalization, models.CASCADE, db_column="barcode")
    count = models.PositiveIntegerField("кількість", default=1)

    def __str__(self):
        return "Зв'язок"

    class Meta:
        managed = False
        verbose_name = "гра в сеансі"
        verbose_name_plural = "ігри в сеансі"
        db_table = "play_session_items"


class Player(models.Model):
    club_member = models.ForeignKey(ClubMember, models.CASCADE)
    play_session = models.ForeignKey(PlaySession, models.CASCADE)

    def __str__(self):
        return "Зв'язок"

    class Meta:
        managed = False
        verbose_name = "гравець у сеансі"
        verbose_name_plural = "гравці в сеансі"
        db_table = "players"
