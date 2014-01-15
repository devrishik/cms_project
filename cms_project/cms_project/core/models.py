from django.contrib.auth.models import AbstractUser
from django_extensions.db.models import TimeStampedModel
from django.db import models


class User(AbstractUser):
	''' User Model '''

	@property
    def name(self):
        return self.get_full_name()

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

class Group(TimeStampedModel):
	''' Group Model to bring people together '''

    name = models.CharField(_('Name'), max_length=100)
    src = models.CharField(_('Source'), max_length=100)
    dest = models.CharField(_('Destination'), max_length=100)
	users = models.ManyToManyField('User', verbose_name=_("Users"),
                                        related_name='groups', blank=True)

	def __unicode__(self):
        return self.name

class Location(TimeStampedModel):
	''' Location Model to track Group location '''

	name = models.CharField(_('Name'), max_length=100)
	longitude = models.DecimalField(_('Longitude'), max_digits=4, decimal_places=2, default=0.0)
	latitude = models.DecimalField(_('Latitude'), max_digits=4, decimal_places=2, default=0.0)
	radius = models.DecimalField(_('Radius'), max_digits=4, decimal_places=2, default=0.0)
	
	group = models.OneToOneField(Group, primary_key = True)

	def __unicode__(self):
        return self.name

class Channel(TimeStampedModel):
	''' Channel for a particular Group '''

	group = models.OneToOneField(Group, primary_key = True)

class Message(TimeStampedModel):
	''' Message on a Channel '''

	user = models.ForeignKey(User)
	channel = models.ForeignKey(Channel)

	content = models.CharField(_("Message"), max_length=60, blank=False,
                        help_text='Write a message to convey to all')
