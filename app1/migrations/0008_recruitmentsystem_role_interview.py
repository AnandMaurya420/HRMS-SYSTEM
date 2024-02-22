# Generated by Django 4.1.7 on 2024-02-16 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_recruitmentsystem_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitmentsystem',
            name='role',
            field=models.CharField(choices=[('HR_Manager', 'HR Manager'), ('Junior HR', 'Junior HR'), ('Senior HR', 'Senior HR'), ('Senior Manage', 'Senior Manager'), ('Project manager', 'Project manager'), ('Team Leader', 'Team Leader'), ('Software Developer', 'Software Developer'), ('Web developer', 'Web developer'), ('App Developer', 'App Developer'), ('Intern/Trainee', 'Intern/Trainee')], max_length=30, null=True),
        ),
        migrations.CreateModel(
            name='interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviewRound', models.CharField(choices=[('round-1', 'round-1'), ('round-2', 'round-2'), ('round-3', 'round-3')], max_length=10, null=True)),
                ('designation', models.CharField(choices=[('HR_Manager', 'HR Manager'), ('Junior HR', 'Junior HR'), ('Senior HR', 'Senior HR'), ('Senior Manage', 'Senior Manager'), ('Project manager', 'Project manager'), ('Team Leader', 'Team Leader'), ('Software Developer', 'Software Developer'), ('Web developer', 'Web developer'), ('App Developer', 'App Developer'), ('Intern/Trainee', 'Intern/Trainee')], max_length=30, null=True)),
                ('scheduledTime', models.DateField(null=True)),
                ('from_time', models.TimeField(null=True)),
                ('to_time', models.TimeField(null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('under review', 'under review'), ('cleared', 'cleared'), ('rejected', 'rejected')], max_length=20, null=True)),
                ('job_applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.recruitmentsystem', to_field='email')),
            ],
        ),
    ]
