# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from editor.models import Article

class ArticleAdmin(admin.ModelAdmin):
	class Media:
		js = (
			'/static/js/jquery-2.2.4.min.js',
			'/static/ckeditor/ckeditor.js',
			'/static/js/custom.js',
		)
		css = {
            'all': ('/static/css/custom.css',)
        }

admin.site.register(Article, ArticleAdmin)
