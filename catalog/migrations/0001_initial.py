# Generated by Django 3.2.15 on 2022-09-27 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Enter authors name', max_length=100, verbose_name='Authors name')),
                ('last_name', models.CharField(help_text='Enter authors last name', max_length=100, verbose_name='Authors last name')),
                ('date_of_birth', models.DateField(blank=True, help_text='Enter authors date of birth', null=True, verbose_name='Date of birth')),
                ('date_of_death', models.DateField(blank=True, help_text='Enter authors date of death', null=True, verbose_name='Date of death')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter books title', max_length=200, verbose_name='Book title')),
                ('summary', models.TextField(help_text='Enter a short description about this book', max_length=1000, verbose_name='A summary')),
                ('isbn', models.CharField(help_text='Enter a thirteen-place symbol index', max_length=13, verbose_name='ISBN of book')),
                ('author', models.ManyToManyField(help_text='Book author', to='catalog.Author', verbose_name='Book author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Please enter genre', max_length=200, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(help_text='Enter book language', max_length=20, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(help_text='Enter the status of a copy of the book', max_length=20, verbose_name='Status of a copy of the book')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_num', models.CharField(help_text='Enter stock number of a copy of the book', max_length=20)),
                ('imprint', models.CharField(help_text='Enter the publishing house and year of a book', max_length=200, verbose_name='Publishing house')),
                ('due_back', models.DateField(blank=True, help_text='Enter date the status change', null=True, verbose_name='Date of change the status')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('status', models.ForeignKey(help_text='Enter a status of a copy of the book', on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Status of a copy of the book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Book genre', to='catalog.Genre', verbose_name='Book genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(help_text='Book language', to='catalog.Language', verbose_name='Book language'),
        ),
    ]
