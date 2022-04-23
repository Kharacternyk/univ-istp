from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db.models import TextField
from bgclub import models

class NarrowTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 80})},
    }

class InlineAuthorship(admin.TabularInline):
    model = models.Authorship
    extra = 1

class InlinePlayers(admin.TabularInline):
    model = models.Players
    extra = 2

class InlineItems(admin.TabularInline):
    model = models.PlaySessionItems
    extra = 1

class AuthorshipAdmin(NarrowTextAdmin):
    inlines = tuple([InlineAuthorship])

class PlaySessionsAdmin(NarrowTextAdmin):
    inlines = (InlineItems, InlinePlayers)

admin.site.register(models.Authors, AuthorshipAdmin)
admin.site.register(models.Categories, NarrowTextAdmin)
admin.site.register(models.ClubMembers, NarrowTextAdmin)
admin.site.register(models.Countries, NarrowTextAdmin)
admin.site.register(models.GameLocalizations, NarrowTextAdmin)
admin.site.register(models.Games, AuthorshipAdmin)
admin.site.register(models.Languages, NarrowTextAdmin)
admin.site.register(models.PlaySessions, PlaySessionsAdmin)
admin.site.register(models.Publishers, NarrowTextAdmin)

