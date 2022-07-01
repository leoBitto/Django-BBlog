############################################################
############################################################

##     model name: Article                    
##     superclass: Models
##     subclass:   
##     points to: Container
##     abstract: No

##     description: 
"""
it contains an article, a series of images and text. 
it is an extension of the base.html
it refer to a general topic so it can be filtered.
"""

##     parameters:
#           author
#           date_created
#           date_updated
#           url 
#           title
#           paragraphs         

##       methods:
#           __str__
#           orderedContent

####    Admin stuff

##    fixed CSS-Flex parameters:


##    ignored in admin param:


############################################################
############################################################
from django.db import models
from .categories import *
from django_quill.fields import QuillField

class Article(models.Model):

    # Meta
    author = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True, 
        editable=False,
        )
    date_updated = models.DateTimeField(
        auto_now=True,
        )

    topic = models.ForeignKey(
        Topic, models.SET_NULL, blank=True, null=True
    )
    sub_topic = models.ForeignKey(
        Subtopic, models.SET_NULL, blank=True, null=True
    )
    category = models.ForeignKey(
        Category, models.SET_NULL, blank=True, null=True
    )
    sub_category = models.ForeignKey(
        Subcategory, models.SET_NULL, blank=True, null=True
    )
    argument = models.ForeignKey(
        Argument, models.SET_NULL, blank=True, null=True
    )
    
    # every page is pointed by an url that must be set 
    # in the url patterns when the object is saved
    # the url setted is:
    slug = models.SlugField(
        max_length=120,
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    paragraphs = QuillField(default=None)
       
    
    def __str__(self):
        return self.title

