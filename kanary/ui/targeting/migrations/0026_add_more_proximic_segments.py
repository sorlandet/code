# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SegmentProximicPagePlacement'
        db.create_table(u'targeting_segmentproximicpageplacement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=900, db_index=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['targeting.SegmentProximicPagePlacement'])),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'targeting', ['SegmentProximicPagePlacement'])

        # Adding model 'SegmentProximicPageLanguage'
        db.create_table(u'targeting_segmentproximicpagelanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=900, db_index=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['targeting.SegmentProximicPageLanguage'])),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'targeting', ['SegmentProximicPageLanguage'])

        # Adding model 'SegmentProximicContextual'
        db.create_table(u'targeting_segmentproximiccontextual', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=900, db_index=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['targeting.SegmentProximicContextual'])),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'targeting', ['SegmentProximicContextual'])

        # Adding model 'SegmentProximicPageQuality'
        db.create_table(u'targeting_segmentproximicpagequality', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=900, db_index=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['targeting.SegmentProximicPageQuality'])),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'targeting', ['SegmentProximicPageQuality'])

        # Adding model 'SegmentProximicPageNoticeability'
        db.create_table(u'targeting_segmentproximicpagenoticeability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=900, db_index=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['targeting.SegmentProximicPageNoticeability'])),
            ('appnexus_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'targeting', ['SegmentProximicPageNoticeability'])


    def backwards(self, orm):
        # Deleting model 'SegmentProximicPagePlacement'
        db.delete_table(u'targeting_segmentproximicpageplacement')

        # Deleting model 'SegmentProximicPageLanguage'
        db.delete_table(u'targeting_segmentproximicpagelanguage')

        # Deleting model 'SegmentProximicContextual'
        db.delete_table(u'targeting_segmentproximiccontextual')

        # Deleting model 'SegmentProximicPageQuality'
        db.delete_table(u'targeting_segmentproximicpagequality')

        # Deleting model 'SegmentProximicPageNoticeability'
        db.delete_table(u'targeting_segmentproximicpagenoticeability')


    models = {
        'targeting.appnexusbrand': {
            'Meta': {'object_name': 'AppNexusBrand'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'num_creatives': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'urls': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        'targeting.appnexusbrowser': {
            'Meta': {'object_name': 'AppNexusBrowser'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'platform_type': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'targeting.appnexuscarrier': {
            'Meta': {'object_name': 'AppNexusCarrier'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexuscontentcategory': {
            'Meta': {'object_name': 'AppNexusContentCategory'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_system': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['targeting.AppNexusContentCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'targeting.appnexusdevicemake': {
            'Meta': {'object_name': 'AppNexusDeviceMake'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexusdevicemodel': {
            'Meta': {'unique_together': "(('name', 'make_appnexus_id'),)", 'object_name': 'AppNexusDeviceModel'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'device_type': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'make_appnexus_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'screen_height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'screen_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'})
        },
        'targeting.appnexusinventoryattr': {
            'Meta': {'object_name': 'AppNexusInventoryAttr'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexuslanguage': {
            'Meta': {'object_name': 'AppNexusLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexusos': {
            'Meta': {'object_name': 'AppNexusOS'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'}),
            'platform_type': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        'targeting.appnexussegment': {
            'Meta': {'object_name': 'AppNexusSegment'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        'targeting.appnexustechnicalattr': {
            'Meta': {'object_name': 'AppNexusTechnicalAttr'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '511'})
        },
        u'targeting.contentcategory': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('name', 'parent')]", 'object_name': 'ContentCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.ContentCategory']"})
        },
        u'targeting.contentcategoryvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('name', 'exchange', 'representant')]", 'object_name': 'ContentCategoryValue'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.ContentCategory']"})
        },
        u'targeting.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '160'})
        },
        u'targeting.publishertargetvalue': {
            'Meta': {'ordering': "('id',)", 'object_name': 'PublisherTargetValue', '_ormbases': [u'targeting.TargetValue']},
            '_positions': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            '_sizes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'segments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['targeting.AppNexusSegment']", 'symmetrical': 'False'}),
            u'targetvalue_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['targeting.TargetValue']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'targeting.segmentproximiccontextual': {
            'Meta': {'object_name': 'SegmentProximicContextual'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicContextual']"})
        },
        u'targeting.segmentproximicmaturityrating': {
            'Meta': {'object_name': 'SegmentProximicMaturityRating'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.segmentproximicpagelanguage': {
            'Meta': {'object_name': 'SegmentProximicPageLanguage'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageLanguage']"})
        },
        u'targeting.segmentproximicpagenoticeability': {
            'Meta': {'object_name': 'SegmentProximicPageNoticeability'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageNoticeability']"})
        },
        u'targeting.segmentproximicpageplacement': {
            'Meta': {'object_name': 'SegmentProximicPagePlacement'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPagePlacement']"})
        },
        u'targeting.segmentproximicpagequality': {
            'Meta': {'object_name': 'SegmentProximicPageQuality'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['targeting.SegmentProximicPageQuality']"})
        },
        u'targeting.segmentproximicsafetylevel': {
            'Meta': {'object_name': 'SegmentProximicSafetyLevel'},
            'appnexus_id': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'targeting.targetvalue': {
            'Meta': {'ordering': "('id',)", 'unique_together': "[('exchange', 'category', 'value')]", 'object_name': 'TargetValue'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['targeting.Exchange']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'representant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'represented'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['targeting.TargetValue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '900', 'db_index': 'True'})
        }
    }

    complete_apps = ['targeting']