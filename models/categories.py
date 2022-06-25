############################################################
############################################################

##     model name: Categories                    
##     superclass: Models
##     subclass:   
##     points to: 
##     abstract: No

##     description: 
"""
it contains a cateogrie of articles
"""

##     parameters:
#           category        

##       methods:
#           __str__
#           

####    Admin stuff

##    fixed CSS-Flex parameters:


##    ignored in admin param:


############################################################
############################################################
from django.db import models

class Topic(models.Model):
    topic = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.topic


class Subtopic(models.Model):
    sub_topic = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )
    
    
    def __str__(self):
        return self.sub_topic


class Category(models.Model):
    category = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category


class Subcategory(models.Model):
    sub_category = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )
    class Meta:
        verbose_name_plural = "sub_categories"
    
    def __str__(self):
        return self.sub_category


class Argument(models.Model):
    argument = models.CharField(
        max_length=40,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.argument