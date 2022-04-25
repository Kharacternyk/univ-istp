from django.contrib import admin
from django.forms import Textarea
from django.db.models import TextField
from django.forms import ModelForm, ValidationError
from bgclub import models


class PlaySessionForm(ModelForm):
    def clean(self):
        start_time = self.cleaned_data["start_time"]
        end_time = self.cleaned_data["end_time"]

        if end_time < start_time:
            raise ValidationError({"end_time": "Must be after the start time"})


class NarrowTextAdmin(admin.ModelAdmin):
    formfield_overrides = {
        TextField: {"widget": Textarea(attrs={"rows": 1, "cols": 80})},
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
    form = PlaySessionForm
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
