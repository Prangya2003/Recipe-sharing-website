# Generated by Django 5.0.7 on 2024-07-25 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_remove_savedrecipemodel_recipes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savedrecipemodel',
            name='saved_recipes',
        ),
        migrations.RemoveField(
            model_name='savedrecipemodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='ReviewModel',
        ),
        migrations.DeleteModel(
            name='SavedRecipeModel',
        ),
    ]
