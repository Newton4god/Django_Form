# Generated by Django 4.2.4 on 2024-06-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_remove_student_course_code_student_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default='+2347000000000', max_length=15),
            preserve_default=False,
        ),
    ]
