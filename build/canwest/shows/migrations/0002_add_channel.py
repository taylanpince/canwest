
from south.db import db
from django.db import models
from shows.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Channel'
        db.create_table('shows_channel', (
            ('id', orm['shows.channel:id']),
            ('title', orm['shows.channel:title']),
            ('slug', orm['shows.channel:slug']),
            ('logo', orm['shows.channel:logo']),
            ('category', orm['shows.channel:category']),
        ))
        db.send_create_signal('shows', ['Channel'])
        
        # Adding field 'Show.channel'
        db.add_column('shows_show', 'channel', orm['shows.show:channel'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Channel'
        db.delete_table('shows_channel')
        
        # Deleting field 'Show.channel'
        db.delete_column('shows_show', 'channel_id')
        
    
    
    models = {
        'shows.channel': {
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'channels'", 'to': "orm['shows.ShowCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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
