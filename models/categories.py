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