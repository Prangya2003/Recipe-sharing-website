# Generated by Django 5.0.7 on 2024-07-25 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_remove_savedrecipemodel_saved_recipes_and_more'),
        ('userprofile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilemodel',
            name='saved_recipes',
            field=models.ManyToManyField(blank=True, related_name='saved_by_users', to='recipe.recipemodel'),
        ),
        migrations.AlterField(
            model_name='userprofilemodel',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
