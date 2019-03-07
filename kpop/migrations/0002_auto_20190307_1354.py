# Generated by Django 2.1.7 on 2019-03-07 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kpop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concerts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='kpopgroups',
            name='group_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kpop.GroupCat'),
        ),
        migrations.AlterField(
            model_name='members',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kpop.KpopGroups'),
        ),
        migrations.AlterField(
            model_name='songs',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kpop.KpopGroups'),
        ),
        migrations.AddField(
            model_name='concerts',
            name='group_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kpop.KpopGroups'),
        ),
    ]
