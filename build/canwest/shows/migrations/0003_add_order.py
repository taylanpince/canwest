
from south.db import db
from django.db import models
from shows.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Channel.order'
        db.add_column('shows_channel', 'order', orm['shows.channel:order'])
        
        # Adding field 'Show.order'
        db.add_column('shows_show', 'order', orm['shows.show:order'])
        
        # Adding field 'ShowCategory.order'
        db.add_column('shows_showcategory', 'order', orm['shows.showcategory:order'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Channel.order'
        db.delete_column('shows_channel', 'order')
        
        # Deleting field 'Show.order'
        db.delete_column('shows_show', 'order')
        
        # Deleting field 'ShowCategory.order'
        db.delete_column('shows_showcategory', 'order')
        
    
    
    models = {
        'shows.channel': {
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'channels'", 'to': "orm['shows.ShowCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shows.show': {
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shows'", 'to': "orm['shows.ShowCategory']"}),
            'channel': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shows'", 'blank': 'True', 'null': 'True', 'to': "orm['shows.Channel']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'shows.showcategory': {
            'global_template': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['shows']
