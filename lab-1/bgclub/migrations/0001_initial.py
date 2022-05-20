# Generated by Django 3.2.12 on 2022-04-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Authors",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
            ],
            options={
                "verbose_name_plural": "authors",
                "db_table": "authors",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Authorship",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "authorship",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
            ],
            options={
                "verbose_name_plural": "categories",
                "db_table": "categories",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ClubMembers",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone", models.BigIntegerField(unique=True)),
                ("name", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "club members",
                "db_table": "club_members",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Countries",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
            ],
            options={
                "verbose_name_plural": "countries",
                "db_table": "countries",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="GameLocalizations",
            fields=[
                ("barcode", models.BigIntegerField(primary_key=True, serialize=False)),
                ("name", models.TextField()),
                ("publishing_date", models.DateField(blank=True, null=True)),
                ("in_catalog_since_date", models.DateField(blank=True, null=True)),
                ("in_catalog_count", models.IntegerField()),
            ],
            options={
                "verbose_name_plural": "game localization",
                "db_table": "game_localizations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Games",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("playtime", models.IntegerField(blank=True, null=True)),
                ("min_players", models.IntegerField(blank=True, null=True)),
                ("max_players", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "games",
                "db_table": "games",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Languages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
            ],
            options={
                "verbose_name_plural": "languages",
                "db_table": "languages",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Players",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "players",
                "db_table": "players",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PlaySessionItems",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("count", models.IntegerField(default=1)),
            ],
            options={
                "db_table": "play_session_items",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="PlaySessions",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField()),
                ("end_time", models.DateTimeField()),
            ],
            options={
                "verbose_name_plural": "play sessions",
                "db_table": "play_sessions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Publishers",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(unique=True)),
            ],
            options={
                "verbose_name_plural": "publishers",
                "db_table": "publishers",
                "managed": False,
            },
        ),
    ]