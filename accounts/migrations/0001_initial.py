# Generated by Django 5.1.3 on 2024-12-16 08:56

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('pan_number', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccountDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('account_number', models.BigIntegerField()),
                ('account_holder_name', models.CharField(max_length=100)),
                ('ifsc_code', models.CharField(max_length=20)),
                ('bank_address', models.CharField(max_length=100)),
                ('cheque', models.FileField(upload_to='media/cancel_cheque')),
                ('customer_id', models.BigIntegerField()),
                ('bank_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_reverse', to='base.banknames')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_reverse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('Temporary', 'Temporary'), ('Permanent', 'Permanent')], max_length=10)),
                ('house_no', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin_code', models.PositiveIntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address_reverse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('contact_number', models.PositiveBigIntegerField()),
                ('emergency_contact', models.PositiveBigIntegerField()),
                ('personal_email', models.EmailField(max_length=50)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_reverse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EducationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('qualification', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=20)),
                ('year_of_passing', models.CharField(max_length=4)),
                ('year_of_enrolment', models.CharField(max_length=4)),
                ('university', models.CharField(max_length=100)),
                ('collage', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_reverse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IdentityDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('identity_number', models.CharField(max_length=100)),
                ('front_image', models.ImageField(upload_to='media/identity_cards')),
                ('back_image', models.ImageField(upload_to='media/identity_cards')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('identity_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.identitychoice')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identity_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InsuranceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('insurer', models.CharField(max_length=100, verbose_name='Policy Provider')),
                ('insured', models.CharField(choices=[('self', 'self'), ('dependent', 'dependent ')], max_length=100)),
                ('type_of_insurance', models.CharField(choices=[('individual', 'Individual'), ('Family Floater', 'Family Floater'), ('Group', 'Group')], max_length=20)),
                ('sum_insured', models.BigIntegerField()),
                ('policy_type', models.CharField(choices=[('health insurance', 'health insurance'), ('life insurance', 'life insurance'), ('general insurance', 'general insurance')], max_length=50)),
                ('policy_number', models.BigIntegerField()),
                ('valid_from', models.DateField(default=django.utils.timezone.now)),
                ('valid_till', models.DateField()),
                ('documentation', models.FileField(upload_to='')),
                ('card', models.FileField(upload_to='')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_reverse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DependentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('relationship', models.CharField(choices=[('Mother', 'Mother'), ('Father', 'Father'), ('Sister', 'Sister'), ('Brother', 'Brother'), ('Spouse', 'Spouse'), ('Son', 'Son'), ('Daughter', 'Daughter')], max_length=30)),
                ('dependent_name', models.CharField(max_length=100)),
                ('dependent_DOB', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('dependent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurance_info', to='accounts.insuranceinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProficiencyCertification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=200)),
                ('since', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='media/proficiency_certification')),
                ('grade', models.CharField(max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proficiency_certification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('deleted_at', models.DateTimeField(default=datetime.datetime(2024, 12, 16, 8, 56, 9, 152675, tzinfo=datetime.timezone.utc))),
                ('is_deleted', models.BooleanField(default=False)),
                ('is_updated', models.BooleanField(default=False)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widow', 'Widow')], max_length=20)),
                ('date_of_joining', models.DateField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deleted_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.position')),
                ('reporting_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager_reverse', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated_%(class)s_set', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user_reverse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
