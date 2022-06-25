from django.contrib import admin
from .models.article import Article
from .models.categories import *


class TopicAdmin(admin.TabularInline):
    model = Topic


class SubtopicAdmin(admin.TabularInline):
    model = Subtopic


class CategoryAdmin(admin.TabularInline):
    model = Category


class SubcategoryAdmin(admin.TabularInline):
    model = Subcategory


class ArgumentAdmin(admin.TabularInline):
    model = Argument



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
    inlines = [
        TopicAdmin,
        SubtopicAdmin,
        CategoryAdmin,
        SubcategoryAdmin,
        ArgumentAdmin,

    ]






admin.site.register(Article, ArticleAdmin)