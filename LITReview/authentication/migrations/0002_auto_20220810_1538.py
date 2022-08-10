# Generated by Django 4.0.6 on 2022-08-10 15:38

from django.db import migrations


def create_groups(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')

    creators = Group(name='creators')
    creators.save()
    
    for user in User.objects.all():
        creators.user_set.add(user)



class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_groups)
    ]