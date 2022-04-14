# Generated by Django 3.2.8 on 2022-01-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_battallion_three'),
    ]

    operations = [
        migrations.AddField(
            model_name='battallion_three',
            name='notify_special_duty',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='battallion_three',
            name='department',
            field=models.CharField(choices=[('Anti-corruption & War Crime division', 'Anti-corruption & War Crime division'), ('Buganda Road Court', 'Buganda Road Court'), ('Commercial Court', 'Commercial Court'), ('Supreme Court', 'Supreme Court'), ('High Court Offices Kampala', 'High Court Offices Kampala'), ('High Court Residence', 'High Court Residence'), ('Family Court Division Makindye', 'Family Court Division Makindye'), ('Court of Appeal', 'Court of Appeal'), ('Residence of Justice of Court Appeal', 'Residence of Justice of Court Appeal'), ('DPP Office', 'DPP Office'), ('IGG', 'IGG'), ('Police Establishment', 'Police Establishment')], max_length=150),
        ),
    ]