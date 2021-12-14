# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=50)


    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country_name
        

class Traveler(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'traveler'

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name
    



class Bucketlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    visited = models.BooleanField(default=False)
    place = models.ForeignKey('Country', to_field='id' , db_column='place_id', on_delete=models.CASCADE)
    traveler = models.ForeignKey('Traveler', to_field='id' , db_column='traveler_id', on_delete=models.CASCADE)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bucketlist'

    def __str__(self):
        return self.description