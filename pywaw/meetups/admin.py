#-*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from . import models


class ExternalLinkInline(admin.TabularInline):
    model = models.ExternalLink
    extra = 1


class TalkInline(admin.StackedInline):
    model = models.Talk
    filter_horizontal = ('speakers',)
    extra = 1


class MeetupAdmin(admin.ModelAdmin):
    inlines = (TalkInline, ExternalLinkInline)
    readonly_fields = ('date_modified',)


class TalkProposalAdmin(admin.ModelAdmin):
    readonly_fields = ('talk', 'message', 'date_submitted')
    list_display = ('talk', 'message', 'date_submitted', 'get_meetup')

    def get_meetup(self, obj):
        return obj.talk.meetup

    get_meetup.short_description = 'Meetup'


class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'meetup')


class ContactInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('default'):
                count += 1
            if count > 1:
                raise forms.ValidationError(
                    'Można wybrac tylko jedną wartość domyślną')


class ContactInline(admin.TabularInline):
    model = models.Contact
    readonly_fields = ('first_name', 'last_name', 'email')
    fields = ('first_name', 'last_name', 'email', 'default')
    extra = 0
    formset = ContactInlineFormset

    def has_add_permission(self, request, obj=None):
        return False


class SponsorsAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


class VenueAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'sponsor',
                    'venue', 'get_default')

    def get_default(self, obj):
        if obj.default and obj.sponsor:
            response = "Domyślny dla sponsora {}".format(obj.sponsor)
        elif obj.default and obj.venue:
            response = "Domyślny dla miejsca spotkania {}".format(obj.venue)
        else:
            response = "---"
        return response


admin.site.register(models.Meetup, MeetupAdmin)
admin.site.register(models.Speaker)
admin.site.register(models.Talk, TalkAdmin)
admin.site.register(models.Sponsor, SponsorsAdmin)
admin.site.register(models.Venue, VenueAdmin)
admin.site.register(models.TalkProposal, TalkProposalAdmin)
admin.site.register(models.Contact, ContactAdmin)
