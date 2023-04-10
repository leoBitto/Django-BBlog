from django.contrib import admin
from .models.article import Article
from .models.categories import *


class ArticleAdmin(admin.ModelAdmin):
   
    list_display = (
        'title',
        'author',
        'date_created',
        'date_updated',
        'status',
    )
    
    fieldsets = (
        ('Content',
            {
            'fields':(
                'title',
                'paragraphs',
                ),
            'classes':(
                #'wide',
                'extrapretty',
                ),
            }
            ),
        ('MetaData',
            {
            'fields':(
                'slug',
                'author',
                'topic',
                'sub_topic',
                'category',
                'sub_category',
                'argument',
                'status',
                ),
            'classes':(
                #'wide',
                'extrapretty',
                ),
            }
            ),
        
    )
    prepopulated_fields = {"slug": ("title",)}
    


admin.site.register(Article, ArticleAdmin)
admin.site.register(Topic)
admin.site.register(Subtopic)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Argument)
