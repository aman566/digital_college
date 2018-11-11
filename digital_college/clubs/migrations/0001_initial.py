# Generated by Django 2.1.1 on 2018-11-08 17:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('subject', models.CharField(max_length=500)),
                ('content', models.TextField(default='')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Registered_User')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(default='')),
                ('comId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.Comment')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Registered_User')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_User'),
        ),
        migrations.AddField(
            model_name='images',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Registered_User'),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('postId', 'userId')},
        ),
    ]
