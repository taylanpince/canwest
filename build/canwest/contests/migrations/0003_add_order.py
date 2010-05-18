
from south.db import db
from django.db import models
from contests.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Contest.order'
        db.add_column('contests_contest', 'order', orm['contests.contest:order'])
        
        # Adding field 'Sponsor.order'
        db.add_column('contests_sponsor', 'order', orm['contests.sponsor:order'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Contest.order'
        db.delete_column('contests_contest', 'order')
        
        # Deleting field 'Sponsor.order'
        db.delete_column('contests_sponsor', 'order')
        
    
    
    models = {
        'contests.contest': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'header': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contests.sponsor': {
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': "orm['contests.Contest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }
    
    complete_apps = ['contests']
