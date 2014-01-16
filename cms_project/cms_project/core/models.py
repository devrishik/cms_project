from django.contrib.auth.models import AbstractBaseUser
from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.utils.translation import ugettext as _


class User(AbstractBaseUser):

    ''' User Model '''

    email = models.EmailField(_('Email Address'), unique=True)
    # TODO
    # Implement Email Verification
    @property
    def name(self):
        return self.get_full_name()

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Genus(TimeStampedModel):

    ''' Genus Model to bring people together '''

    name = models.CharField(_('Name'), max_length=100)
    src = models.CharField(_('Source'), max_length=100)
    dest = models.CharField(_('Destination'), max_length=100)
    start_time = models.DateTimeField(_('StartTime'))
    end_time = models.DateTimeField(_('EndTime'))

    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name


class Location(TimeStampedModel):

    ''' Location Model to track Genus location 
    Saving just the name'''

    name = models.CharField(_('Name'), max_length=100)

    longitude = models.DecimalField(
        _('Longitude'), max_digits=4, decimal_places=2, default=0.0)
    latitude = models.DecimalField(
        _('Latitude'), max_digits=4, decimal_places=2, default=0.0)
    # radius = models.DecimalField(_('Radius'), max_digits=4, decimal_places=2, default=0.0)

    genus = models.OneToOneField(Genus, primary_key=True)

    def __unicode__(self):
        return self.name


class Channel(TimeStampedModel):

    ''' Channel for a particular Genus '''

    genus = models.OneToOneField(Genus, primary_key=True)


class Message(TimeStampedModel):

    ''' Message on a Channel '''

    user = models.ForeignKey(User)
    channel = models.ForeignKey(Channel)

    content = models.CharField(_("Message"), max_length=60, blank=False,
                               help_text='Write a message to convey to all')
