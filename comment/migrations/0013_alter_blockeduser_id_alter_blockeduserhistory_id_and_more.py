# Generated by Django 4.2.3 on 2023-11-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0012_blockeduser_blockeduserhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockeduser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='blockeduserhistory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flag',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flaginstance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='flaginstance',
            name='reason',
            field=models.SmallIntegerField(choices=[(1, 'گزارش اسپم'), (2, 'متن نامناسب یا فحاشی'), (3, 'پیام نامربوط'), (4, 'توهین به شخص دیگر'), (100, 'Something else')], default=1),
        ),
        migrations.AlterField(
            model_name='follower',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='reactioninstance',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]