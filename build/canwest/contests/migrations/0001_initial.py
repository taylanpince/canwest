
from south.db import db
from django.db import models
from contests.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Sponsor'
        db.create_table('contests_sponsor', (
            ('id', orm['contests.Sponsor:id']),
            ('name', orm['contests.Sponsor:name']),
            ('url', orm['contests.Sponsor:url']),
            ('logo', orm['contests.Sponsor:logo']),
            ('contest', orm['contests.Sponsor:contest']),
        ))
        db.send_create_signal('contests', ['Sponsor'])
        
        # Adding model 'Contest'
        db.create_table('contests_contest', (
            ('id', orm['contests.Contest:id']),
            ('title', orm['contests.Contest:title']),
            ('slug', orm['contests.Contest:slug']),
            ('description', orm['contests.Contest:description']),
        ))
        db.send_create_signal('contests', ['Contest'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Sponsor'
        db.delete_table('contests_sponsor')
        
        # Deleting model 'Contest'
        db.delete_table('contests_contest')
        
    
    
    models = {
        'contests.contest': {
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
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
