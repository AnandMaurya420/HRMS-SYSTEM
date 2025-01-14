# Generated by Django 4.1.7 on 2024-02-09 05:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('Department', models.CharField(max_length=20)),
                ('check_in', models.DateTimeField(null=True)),
                ('check_out', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('Department', models.CharField(choices=[('Python', 'Python'), ('React', 'React'), ('Php', 'Php'), ('IOS', 'IOS'), ('Flutter', 'flutter'), ('HR', 'HR')], max_length=100)),
                ('employee_role', models.CharField(choices=[('HR_Manager', 'HR Manager'), ('Junior HR', 'Junior HR'), ('Senior HR', 'Senior HR'), ('Senior Manage', 'Senior Manager'), ('Project manager', 'Project manager'), ('Team Leader', 'Team Leader'), ('Software Developer', 'Software Developer'), ('Web develope', 'Web developer'), ('App Developer', 'App Developer'), ('Intern/Trainee', 'Intern/Trainee')], max_length=100)),
                ('experience', models.CharField(choices=[('0 - Year', '0 - Year'), ('0-6 Month', '0-6 Month'), ('1-2 Year', '1-2 Year'), ('2-3 Year', '2-3 Year')], max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Leave_Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('reason', models.CharField(max_length=200, null=True)),
                ('leave_type', models.CharField(choices=[('Custom Festival Leave', 'Custom Festival Leave'), ('Leave Without Pay', 'Leave Without Pay'), ('Privilege Leave', 'Privilege Leave'), ('Bereavement Leave', 'Bereavement Leave')], max_length=100, null=True)),
                ('total_days', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveType_with_LeaveBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Custom_Festival_Leave', models.CharField(default=10, max_length=10, null=True)),
                ('Leave_Without_Pay', models.CharField(default=10, max_length=10, null=True)),
                ('Privilege_Leave', models.CharField(default=10, max_length=10, null=True)),
                ('Bereavement_Leave', models.CharField(default=10, max_length=10, null=True)),
                ('username', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('check_in', models.TimeField(null=True)),
                ('check_out', models.TimeField(null=True)),
                ('total_hour', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='multiple_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('check_in', models.TimeField(null=True)),
                ('check_out', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
