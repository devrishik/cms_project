# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'core_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'core', ['User'])

        # Adding model 'Genus'
        db.create_table(u'core_genus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('src', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dest', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['Genus'])

        # Adding M2M table for field users on 'Genus'
        m2m_table_name = db.shorten_name(u'core_genus_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('genus', models.ForeignKey(orm[u'core.genus'], null=False)),
            ('user', models.ForeignKey(orm[u'core.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['genus_id', 'user_id'])

        # Adding model 'Location'
        db.create_table(u'core_location', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=2)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=2)),
            ('genus', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Genus'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Location'])

        # Adding model 'Channel'
        db.create_table(u'core_channel', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('genus', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.Genus'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Channel'])

        # Adding model 'Message'
        db.create_table(u'core_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.User'])),
            ('channel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Channel'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'core', ['Message'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'core_user')

        # Deleting model 'Genus'
        db.delete_table(u'core_genus')

        # Removing M2M table for field users on 'Genus'
        db.delete_table(db.shorten_name(u'core_genus_users'))

        # Deleting model 'Location'
        db.delete_table(u'core_location')

        # Deleting model 'Channel'
        db.delete_table(u'core_channel')

        # Deleting model 'Message'
        db.delete_table(u'core_message')


    models = {
        u'core.channel': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Channel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'genus': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Genus']", 'unique': 'True', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        u'core.genus': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Genus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dest': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'src': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.User']", 'symmetrical': 'False'})
        },
        u'core.location': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Location'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'genus': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Genus']", 'unique': 'True', 'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.message': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Message'},
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Channel']"}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.User']"})
        },
        u'core.user': {
            'Meta': {'object_name': 'User'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['core']