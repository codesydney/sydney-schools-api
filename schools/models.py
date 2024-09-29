from django.db import models

class NSWSchool(models.Model):
    acara_id = models.IntegerField(primary_key=True)
    school_name = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    school_type = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    parent_school_id = models.IntegerField(null=True, blank=True)
    age_id = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    globalid = models.CharField(max_length=255)
    cadid = models.CharField(max_length=255)
    createdate = models.DateTimeField(null=True, blank=True)  # Allow NULLs
    modifieddate = models.DateTimeField(null=True, blank=True)  # Allow NULLs
    lganame = models.CharField(max_length=255, null=True, blank=True)
    councilname = models.CharField(max_length=255, null=True, blank=True)
    abscode = models.CharField(max_length=100, null=True, blank=True)
    ltocode = models.CharField(max_length=100, null=True, blank=True)
    vgcode = models.CharField(max_length=100, null=True, blank=True)
    wbcode = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'nsw_schools_table'