# Generated by Django 3.2.8 on 2021-11-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20211106_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battallion_two',
            name='armed',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='department',
            field=models.CharField(choices=[('Embassy', 'Embassy'), ('Consolate', 'Consolate'), ('High commission', 'High commission'), ('Other diplomats', 'Other diplomats'), ('Administration', 'Administration')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='education_level',
            field=models.CharField(choices=[('PLE', 'PLE'), ('UCE', 'UCE'), ('UACE', 'UACE'), ('Diploma', 'DIPLOMA'), ('Bachelors', 'BACHELORS'), ('Masters', 'MASTERS'), ('Doctorate', 'DOCTORATE(PhD)'), ('Other', 'OTHER')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='on_leave',
            field=models.CharField(choices=[('Pass leave', 'Pass leave'), ('Maternity leave', 'Maternity leave'), ('Sick leave', 'Sick leave'), ('Study leave', 'Study leave'), ('Annual leave', 'Annual leave'), ('Not no leave', 'Not no leave')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='shift',
            field=models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Long night', 'Long night'), ('None', 'None(not applicable)')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Absent', 'Absent(AWOL)'), ('Transfered', 'Transfered'), ('Sick', 'Sick'), ('Dead', 'Dead'), ('Suspended', 'Suspended'), ('Dismissed', 'Dismissed'), ('In court', 'In court'), ('Deserted', 'Deserted'), ('On course', 'On course'), ('On mission', 'On mission')], max_length=32),
        ),
        migrations.AlterField(
            model_name='battallion_two',
            name='title',
            field=models.CharField(choices=[('Commandant', 'Commandant'), ('Deputy commandant', 'Deputy commandant'), ('Staff officer', 'Staff officer'), ('Head of operations', 'Head of operations'), ('Head of armoury', 'Head of armoury'), ('Supervisor', 'Supervisor'), ('In Charge', 'In Charge'), ('2nd In Charge', '2nd In Charge'), ('Driver', 'Driver')], max_length=32),
        ),
    ]