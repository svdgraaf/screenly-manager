# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Client.last_active'
        db.alter_column(u'screenlymanager_client', 'last_active', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Client.notes'
        db.alter_column(u'screenlymanager_client', 'notes', self.gf('django.db.models.fields.TextField')(max_length=1024, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Client.last_active'
        raise RuntimeError("Cannot reverse this migration. 'Client.last_active' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Client.notes'
        raise RuntimeError("Cannot reverse this migration. 'Client.notes' and its values cannot be restored.")

    models = {
        u'screenlymanager.client': {
            'Meta': {'object_name': 'Client'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_active': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['screenlymanager']