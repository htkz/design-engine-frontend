# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

# Create your models here.
class Element(models.Model):
    nodeId = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    prev = models.CharField(max_length=64, null=True, blank=True)
    next = models.CharField(max_length=64, null=True, blank=True)
    fanout = models.CharField(max_length=64, null=True, blank=True)
    fanoutFixedValue = models.IntegerField(null=True, blank=True)
    fanoutFunction = models.CharField(max_length=64, null=True, blank=True)
    partitioning = models.CharField(max_length=64, null=True, blank=True)
    partitioningFunction = models.CharField(max_length=64, null=True, blank=True)
    filtersPerLevel = models.CharField(max_length=64, null=True, blank=True)
    filtersPerRun = models.CharField(max_length=64, null=True, blank=True)
    initialRunSize = models.IntegerField(null=True, blank=True)
    maxRunsPerLevel = models.IntegerField(null=True, blank=True)
    mergeFactor = models.IntegerField(null=True, blank=True)
    sorted = models.CharField(max_length=64, null=True, blank=True)
    directAddressing = models.CharField(max_length=64, null=True, blank=True)
    head = models.CharField(max_length=64, null=True, blank=True)
    tail = models.CharField(max_length=64, null=True, blank=True)
    prevLinks = models.CharField(max_length=64, null=True, blank=True)
    nextLinks = models.CharField(max_length=64, null=True, blank=True)
    skiplinks = models.CharField(max_length=64, null=True, blank=True)
    skiplinksProbability = models.IntegerField(null=True, blank=True)
    zoneMapMax = models.CharField(max_length=64, null=True, blank=True)
    zoneMapMin = models.CharField(max_length=64, null=True, blank=True)
    bloomFilters = models.CharField(max_length=64, null=True, blank=True)
    HashFunctionsNum = models.IntegerField(null=True, blank=True)
    NumOfBits = models.IntegerField(null=True, blank=True)
    keyRetention = models.CharField(max_length=64, null=True, blank=True)
    keyRetentionCompression = models.CharField(max_length=64, null=True, blank=True)
    keyRetentionFunction = models.CharField(max_length=64, null=True, blank=True)
    valueRetention = models.CharField(max_length=64, null=True, blank=True)
    valueRetentionCompression = models.CharField(max_length=64, null=True, blank=True)
    valueRetentionFunction = models.CharField(max_length=64, null=True, blank=True)
    capacity = models.CharField(max_length=64, null=True, blank=True)
    capacityValue = models.IntegerField(null=True, blank=True)
    capacityFunction = models.CharField(max_length=64, null=True, blank=True)
    Utilization = models.CharField(max_length=64, null=True, blank=True)
    UtilizationFunction = models.CharField(max_length=64, null=True, blank=True)
    linksLayout = models.CharField(max_length=64, null=True, blank=True)
    filtersLayout = models.CharField(max_length=64, null=True, blank=True)
    keyValueLayout = models.CharField(max_length=64, null=True, blank=True)
    accessPartitions = models.CharField(max_length=64, null=True, blank=True)
    color= models.CharField(max_length=64, null=True)
    shortName = models.CharField(max_length=2, null=True)
    def __str__(self):
        return self.name

class DataStructure(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    value = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to = 'app/static/img/data_structure_img/',
        default = 'app/static/img/data-structure-img/no-img.jpg')
    def __str__(self):
        return self.name
