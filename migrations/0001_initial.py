# Generated by Django 3.2.5 on 2022-04-12 15:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ColLabels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab', models.CharField(max_length=32)),
                ('col', models.CharField(max_length=32)),
                ('label', models.CharField(blank=True, max_length=255, null=True)),
                ('label_sv', models.CharField(blank=True, max_length=255, null=True)),
                ('ftab', models.CharField(blank=True, max_length=32, null=True)),
                ('fcol', models.CharField(blank=True, max_length=32, null=True)),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('hidden', models.PositiveIntegerField()),
                ('readonly', models.PositiveIntegerField()),
                ('searchable', models.PositiveIntegerField()),
                ('help', models.CharField(max_length=256)),
                ('help_sv', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'col_labels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bild', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.image.image')),
                ('bildfil', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.image.image_file')),
            ],
            options={
                'verbose_name': 'iconographia.image.meta.singular_name',
                'verbose_name_plural': 'iconographia.image.meta.plural_name',
                'db_table': 'image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Motive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motive', models.CharField(blank=True, max_length=175, null=True, verbose_name='iconographia.motive.motif')),
            ],
            options={
                'verbose_name': 'iconographia.motive.meta.singular_name',
                'verbose_name_plural': 'iconographia.motive.meta.plural_name',
                'db_table': 'motive',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objektid', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.object_id')),
                ('museum', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.museum')),
                ('inventarienummer', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.inventory_nr')),
                ('undernummer', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.sub_nr')),
                ('invnr', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.inv_nr')),
                ('landskap', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.county')),
                ('ort', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.town')),
                ('sakord', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.topic')),
                ('typ', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.type')),
                ('undertyp', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.subtype')),
                ('cdh_category', models.CharField(max_length=16, verbose_name='iconographia.object.cdh_category')),
                ('objekt', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.object')),
                ('namntyp', models.PositiveIntegerField(blank=True, null=True, verbose_name='iconographia.object.name_type')),
                ('upphovsman', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.author')),
                ('tid', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.time')),
                ('lk_tid', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.time_lk')),
                ('dat_min', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='iconographia.object.dat_min')),
                ('dat_max', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='iconographia.object.dat_max')),
                ('hojd', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.height')),
                ('bredd', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.width')),
                ('material', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.material')),
                ('delar', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.parts')),
                ('urtappning', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.urtappning')),
                ('inskrift', models.CharField(blank=True, max_length=256, null=True, verbose_name='iconographia.object.inscription')),
                ('kondition', models.CharField(blank=True, max_length=512, null=True, verbose_name='iconographia.object.condition')),
                ('farg', models.CharField(blank=True, max_length=256, null=True, verbose_name='iconographia.object.color')),
                ('ovrigt', models.TextField(blank=True, null=True, verbose_name='iconographia.object.miscellaneous')),
                ('sokord', models.CharField(blank=True, max_length=512, null=True, verbose_name='iconographia.object.query')),
                ('motiv', models.TextField(blank=True, null=True, verbose_name='iconographia.object.motif')),
                ('litteratur', models.TextField(blank=True, null=True, verbose_name='iconographia.object.literature')),
                ('status', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.status')),
                ('titel', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.object.title')),
            ],
            options={
                'verbose_name': 'iconographia.object.meta.singular_name',
                'verbose_name_plural': 'iconographia.object.meta.plural_name',
                'db_table': 'object',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='iconographia.parish.name')),
                ('variants', models.CharField(blank=True, max_length=256, null=True, verbose_name='iconographia.parish.variants')),
                ('province', models.CharField(blank=True, max_length=255, null=True, verbose_name='iconographia.parish.province')),
                ('diocese', models.CharField(blank=True, max_length=255, null=True, verbose_name='iconographia.parish.diocese')),
                ('diocese_med', models.CharField(blank=True, max_length=255, null=True, verbose_name='iconographia.parish.diocese_med')),
                ('county', models.CharField(blank=True, max_length=255, null=True, verbose_name='iconographia.parish.county')),
                ('notbefore', models.CharField(blank=True, max_length=16, null=True, verbose_name='iconographia.parish.not_before')),
                ('notafter', models.CharField(blank=True, max_length=16, null=True, verbose_name='iconographia.parish.not_after')),
                ('note_year', models.CharField(blank=True, max_length=128, null=True, verbose_name='iconographia.parish.note_year')),
                ('snid_4', models.PositiveIntegerField(blank=True, null=True, verbose_name='iconographia.parish.snid_4')),
                ('wikidata', models.CharField(blank=True, max_length=64, null=True, verbose_name='iconographia.parish.wikidata')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='iconographia.parish.notes')),
            ],
            options={
                'verbose_name': 'iconographia.parish.meta.singular_name',
                'verbose_name_plural': 'iconographia.parish.meta.plural_name',
                'db_table': 'parish',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='iconographia.place.name')),
                ('type', models.PositiveIntegerField(verbose_name='iconographia.place.type')),
                ('certainty_type', models.CharField(max_length=9, verbose_name='iconographia.place.certainty_type')),
                ('certainty', models.CharField(max_length=9, verbose_name='iconographia.place.certainty')),
                ('date_bebr', models.CharField(max_length=64, verbose_name='iconographia.place.date_bebr')),
                ('notbefore', models.CharField(max_length=32, verbose_name='iconographia.place.not_before')),
                ('notafter', models.CharField(max_length=32, verbose_name='iconographia.place.not_after')),
                ('type_indication', models.CharField(max_length=8, verbose_name='iconographia.place.type_indication')),
                ('note_year', models.CharField(max_length=128, verbose_name='iconographia.place.note_year')),
                ('wikidata', models.CharField(blank=True, max_length=64, null=True, verbose_name='iconographia.place.wikidata')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326, verbose_name='iconographia.place.geom')),
                ('municipality', models.CharField(blank=True, max_length=256, null=True, verbose_name='iconographia.place.municipality')),
                ('county', models.CharField(blank=True, max_length=256, null=True, verbose_name='iconographia.place.county')),
                ('country', models.CharField(blank=True, max_length=32, null=True, verbose_name='iconographia.place.country')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='iconographia.place.notes')),
                ('exclude', models.CharField(blank=True, max_length=3, null=True, verbose_name='iconographia.place.exclude')),
            ],
            options={
                'verbose_name': 'iconographia.place.meta.singular_name',
                'verbose_name_plural': 'iconographia.place.meta.plural_name',
                'db_table': 'place',
                'managed': False,
            },
        ),
    ]
