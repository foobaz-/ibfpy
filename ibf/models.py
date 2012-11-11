# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=300, unique=True)
    password = models.CharField(max_length=300)
    class Meta:
        db_table = u'users'

    def __unicode__(self):
        return self.email
