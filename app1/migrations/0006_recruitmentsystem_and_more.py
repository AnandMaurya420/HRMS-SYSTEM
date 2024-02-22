# Generated by Django 4.1.7 on 2024-02-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_leave_request_selectleave'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('phone_no', models.PositiveIntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True)),
                ('applying_for', models.CharField(choices=[('Python', 'Python'), ('React', 'React'), ('Php', 'Php'), ('IOS', 'IOS'), ('Flutter', 'flutter'), ('HR', 'HR')], max_length=100, null=True)),
                ('experience', models.CharField(choices=[('Fresher', 'Fresher'), ('6 Month', '6 Month'), ('1 Year', '1 Year'), ('2 Year', '2 Year'), ('More than 2 year', 'More than 2 year')], max_length=100, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='leavetype_with_leavebalance',
            name='Custom_Festival_Leave',
            field=models.FloatField(default=10, null=True),
        ),
    ]