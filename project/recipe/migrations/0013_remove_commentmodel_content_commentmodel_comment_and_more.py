# Generated by Django 5.0.7 on 2024-07-28 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0012_alter_commentmodel_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='content',
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='recipe.recipemodel'),
        ),
    ]
