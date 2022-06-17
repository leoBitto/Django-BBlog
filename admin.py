from django.contrib import admin
from .models.article import Article
from .models.categories import Category



class ArticleAdmin(admin.ModelAdmin):
   
    list_display = (
        'title',
        'author',
        'date_created',
        'date_updated',
        
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
                ),
            'classes':(
                #'wide',
                'extrapretty',
                ),
            }
            ),
        
    )
    prepopulated_fields = {"slug": ("title",)}

 

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category'
    ]
    fieldsets = (
        ('Content',
            {
            'fields':(
                'category',
                ),
            'classes':(
                'wide',
                'extrapretty',
                ),
            }
            ),   
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)