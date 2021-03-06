# Generated by Django 3.2.8 on 2021-12-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_user_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='section',
            field=models.CharField(choices=[('UNDP Head Office', 'UNDP Head Office'), ('UN Women', 'UN Women'), ('IFAD office', 'IFAD office'), ('UNDSS office', 'UNDSS office'), ('WFP', 'WFP'), ('WHO', 'WHO'), ('World bank', 'World bank'), ('FAO office', 'FAO office'), ('SPGS office', 'SPGS office'), ('UNHCR new offices', 'UNHCR new offices'), ('UNHCR Extension', 'UNHCR Extension'), ('I.C.C field offices', 'IFAD office'), ('UNFPA', 'UNFPA'), ('I.O.M head office', 'I.O.M head office'), ('I.O.M Transit Centre', 'I.O.M Transit Centre'), ('UNOHCHR office', 'UNOHCHR office'), ('EADB', 'EADB'), ('UNDP', 'UNDP'), ('UNDP Gulu', 'UNDP Gulu'), ('UNDP Moroto', 'UNDP Moroto'), ('UNICEF office', 'UNICEF office'), ('UNDP Arua', 'UNDP Arua')], max_length=32),
        ),
    ]
