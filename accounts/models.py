from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now
from django.contrib.auth.models import BaseUserManager
from datetime import timedelta
from base.models import Position, BankNames ,IdentityChoice
# Create your models here.
MARITAL_STATUS_CHOICE = (('single','Single'),('married' ,'Married'),('widow','Widow'))
DEPENDENT_CHOICE = (('Mother','Mother'),('Father','Father'),('Sister','Sister'),('Brother','Brother'),('Spouse','Spouse'),('Son','Son'),('Daughter','Daughter'))

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin ):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    pan_number = models.CharField(max_length=10)
    date_of_birth = models.DateField(null=True,blank=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'  # Use email instead of username
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username

class CommonFields(models.Model):
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())
    deleted_at = models.DateTimeField(default=now())
    is_deleted = models.BooleanField(default=False)
    is_updated = models.BooleanField(default=False)
    created_by = models.ForeignKey(CustomUser , on_delete=models.CASCADE, related_name='created_%(class)s_set')
    updated_by = models.ForeignKey(CustomUser , on_delete=models.CASCADE, related_name='updated_%(class)s_set')
    deleted_by = models.ForeignKey(CustomUser , on_delete=models.CASCADE, related_name='deleted_%(class)s_set')
    class Meta:
        abstract =True

class UserProfile(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='custom_user_reverse')
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICE ,max_length=20)
    reporting_manager = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='manager_reverse')
    position = models.ForeignKey(Position ,on_delete=models.CASCADE)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.user.username


class ContactDetails(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='contact_reverse')
    contact_number = models.PositiveBigIntegerField()
    emergency_contact = models.PositiveBigIntegerField()
    personal_email = models.EmailField(max_length=50)

    def __str__(self):
        # return str(self.contact_number)
        return self.contact_number


class AddressDetails(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='address_reverse')
    type = models.CharField(choices=(('Temporary','Temporary'),('Permanent' ,'Permanent')) , max_length=10 )
    house_no = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.type} : {self.house_no} , {self.city} , {self.state} , {self.pin_code}'


class AccountDetail(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='account_reverse')
    account_number = models.BigIntegerField()
    account_holder_name = models.CharField(max_length=100)
    bank_name = models.ForeignKey(BankNames , on_delete=models.CASCADE,related_name='bank_reverse')
    ifsc_code = models.CharField(max_length=20)
    bank_address = models.CharField(max_length=100)
    cheque = models.FileField(upload_to='media/cancel_cheque')
    customer_id = models.BigIntegerField()

    def __str__(self):
        return f'{self.account_holder_name} : {self.account_number}'


class EducationDetail(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='education_reverse')
    qualification = models.CharField(max_length=100)
    grade = models.CharField(max_length=20)
    year_of_passing = models.CharField(max_length=4)
    year_of_enrolment = models.CharField(max_length=4)
    university = models.CharField(max_length=100)
    collage = models.CharField(max_length=100)

    def __str__(self):
        return self.qualification

class InsuranceInfo(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='insurance_reverse')
    insurer = models.CharField(max_length=100 , verbose_name='Policy Provider')
    insured = models.CharField(choices=(('self','self'),('dependent','dependent ')),max_length=100)
    # policy_holder_name = models.ForeignKey(DependentDetail ,models.CASCADE)
    type_of_insurance = models.CharField(choices=(('individual','Individual'),('Family Floater','Family Floater'),('Group','Group')),max_length=20)
    sum_insured = models.BigIntegerField()
    policy_type = models.CharField(choices=(('health insurance','health insurance'),('life insurance','life insurance'),('general insurance','general insurance')) ,max_length = 50)
    policy_number = models.BigIntegerField()
    valid_from  = models.DateField(default=now)
    valid_till  = models.DateField()
    documentation  = models.FileField()
    card = models.FileField()

    def valid_till_method(self):
        if self.valid_from and self.valid_till is None:
            return  self.valid_from + timedelta(days=365)

    def save(self,*args,**kwargs):
        self.valid_till = self.valid_till_method()

    def __str__(self):
        return  f'{self.policy_holder_name} : {self.policy_number}'


class DependentDetail(CommonFields):
    dependent = models.ForeignKey(InsuranceInfo,on_delete=models.CASCADE,related_name='insurance_info')
    relationship = models.CharField(choices=DEPENDENT_CHOICE,max_length=30)
    dependent_name = models.CharField(max_length=100)
    dependent_DOB = models.DateField()

    def __str__(self):
        return f'{self.relationship} : {self.dependent_name}'


class IdentityDetail(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='identity_name')
    identity_name = models.ForeignKey(IdentityChoice , on_delete = models.CASCADE)
    identity_number = models.CharField(max_length=100)
    front_image = models.ImageField(upload_to='media/identity_cards')
    back_image = models.ImageField(upload_to='media/identity_cards')

    def __str__(self):
        return f' {self.identity_name}: {self.identity_number} '


class ProficiencyCertification(CommonFields):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='proficiency_certification')
    name = models.CharField(max_length=200)
    since = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='media/proficiency_certification')
    grade = models.CharField(max_length=20)

    def __str__(self):
        return f' {self.name}: {self.grade} '


