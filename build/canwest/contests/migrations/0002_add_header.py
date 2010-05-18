
from south.db import db
from django.db import models
from contests.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Contest.header'
        db.add_column('contests_contest', 'header', orm['contests.contest:header'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Contest.header'
        db.delete_column('contests_contest', 'header')
        
    
    
    models = {
        'contests.contest': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'header': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contests.sponsor': {
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sponsors'", 'to': "orm['contests.Contest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }
    
    complete_apps = ['contests']
