# Generated by Django 5.1.1 on 2024-09-29 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NSWSchool',
            fields=[
                ('acara_id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=10)),
                ('school_type', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('parent_school_id', models.IntegerField(blank=True, null=True)),
                ('age_id', models.IntegerField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('globalid', models.CharField(max_length=255)),
                ('cadid', models.CharField(max_length=255)),
                ('createdate', models.DateTimeField(blank=True, null=True)),
                ('modifieddate', models.DateTimeField(blank=True, null=True)),
                ('lganame', models.CharField(blank=True, max_length=255, null=True)),
                ('councilname', models.CharField(blank=True, max_length=255, null=True)),
                ('abscode', models.CharField(blank=True, max_length=100, null=True)),
                ('ltocode', models.CharField(blank=True, max_length=100, null=True)),
                ('vgcode', models.CharField(blank=True, max_length=100, null=True)),
                ('wbcode', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nsw_schools_table',
            },
        ),
    ]
