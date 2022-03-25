# Generated by Django 4.0.3 on 2022-03-24 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(help_text="The article's title, as displayed in list views.", max_length=160)),
                ('slug', models.SlugField(help_text="The article's URL.", unique=True)),
                ('summary', models.TextField(help_text='A summary of the content of the article.', max_length=255)),
                ('template_filename', models.CharField(help_text="The path relative to templates/blog_app/content to this article's template.", max_length=255)),
            ],
        ),
    ]
