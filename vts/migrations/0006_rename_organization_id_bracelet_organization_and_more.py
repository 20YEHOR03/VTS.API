# Generated by Django 4.2.1 on 2023-05-30 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vts', '0005_bracelet_organization_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bracelet',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='bracelet',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='gender_id',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='organization_id',
            new_name='organization',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='zone_id',
            new_name='zone',
        ),
        migrations.RenameField(
            model_name='zone',
            old_name='organization_id',
            new_name='organization',
        ),
    ]
