
from south.db import db
from django.db import models
from shows.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Show'
        db.create_table('shows_show', (
            ('id', orm['shows.Show:id']),
            ('title', orm['shows.Show:title']),
            ('slug', orm['shows.Show:slug']),
            ('blurb', orm['shows.Show:blurb']),
            ('description', orm['shows.Show:description']),
            ('logo', orm['shows.Show:logo']),
            ('photo', orm['shows.Show:photo']),
            ('category', orm['shows.Show:category']),
        ))
        db.send_create_signal('shows', ['Show'])
        
        # Adding model 'ShowCategory'
        db.create_table('shows_showcategory', (
            ('id', orm['shows.ShowCategory:id']),
            ('title', orm['shows.ShowCategory:title']),
            ('slug', orm['shows.ShowCategory:slug']),
            ('global_template', orm['shows.ShowCategory:global_template']),
        ))
        db.send_create_signal('shows', ['ShowCategory'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Show'
        db.delete_table('shows_show')
        
        # Deleting model 'ShowCategory'
        db.delete_table('shows_showcategory')
        
    
    
    models = {
        'shows.show': {
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shows'", 'to': "orm['shows.ShowCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shows.showcategory': {
            'global_template': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['shows']
