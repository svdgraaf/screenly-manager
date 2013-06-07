# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.port'
        db.add_column(u'screenlymanager_client', 'port',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default='8080'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.port'
        db.delete_column(u'screenlymanager_client', 'port')


    models = {
        u'screenlymanager.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_active': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'port': ('django.db.models.fields.PositiveIntegerField', [], {'default': "'8080'"})
        }
    }

    complete_apps = ['screenlymanager']