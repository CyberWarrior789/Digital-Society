# Generated by Django 3.2.7 on 2021-09-25 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MemberApp', '0014_complain_event_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family_member',
            name='member_id',
        ),
    ]
