# Generated by Django 4.0.6 on 2022-07-31 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic_app', '0004_mail_file_name_mailmerge_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailmerge',
            name='zip_pdf',
            field=models.FileField(default='', upload_to='submodels/MailMerge/zip_docx/'),
            preserve_default=False,
        ),
    ]