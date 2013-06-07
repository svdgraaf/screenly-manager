# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'screenlymanager_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('last_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, blank=True)),
            ('last_active', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(max_length=1024)),
        ))
        db.send_create_signal(u'screenlymanager', ['Client'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'screenlymanager_client')


    models = {
        u'screenlymanager.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_active': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'last_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['screenlymanager']