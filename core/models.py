from django.db import models
import random

import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

import uuid
import os

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# from .brother import print_text, get_label_context

# Create your models here.


def profile_image_file_path(instance, filename):
    # Generate file path for new recipe image
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user/', filename)

def image_file_path(instance, filename):
    # Generate file path for new recipe image
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/images/', filename)

class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        # Creates and save a new user
        if not email:
            raise ValueError('Users must have an email address!')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # Creates and save a new superuser
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(PermissionsMixin, AbstractBaseUser):
    # Custom user model supports email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to=profile_image_file_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Office(models.Model):
    name = models.CharField(max_length=100, default='Main Office')

    def __str__(self):
        return self.name

class Department(models.Model):
    id = models.SmallIntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=30)
    office = models.ForeignKey('Office', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.office.name})'
        # return self.name

class Employee(models.Model):
    employee_id = models.SmallIntegerField(null=True,blank=True,unique=True)
    department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)
    office = models.ForeignKey('Office', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class AssetType(models.Model):
    unique_id = models.IntegerField(unique=True,null=True,blank=True)
    name = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Asset(models.Model):

    CONDITION_CHOICES = (
        ('new', 'NEW'),
        ('used', 'USED'),
        ('refurbished', 'REFURBISHED'),
        ('broken', 'BROKEN'),
    )

    code = models.CharField(max_length=10,blank=True,null=True)
    type = models.ForeignKey('AssetType', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    department = models.ForeignKey('Department', null=True, on_delete=models.SET_NULL)
    office = models.ForeignKey('Office', null=True, on_delete=models.SET_NULL)
    employee = models.ForeignKey('Employee', null=True, on_delete=models.SET_NULL)
    description = models.TextField(null=True,blank=True)
    condition = models.CharField(max_length=12,default='new',choices=CONDITION_CHOICES)
    barcode = models.ImageField(null=True, blank=True, upload_to=profile_image_file_path)
    image = models.ImageField(null=True, blank=True, upload_to=image_file_path)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        code = self.code
        z_code = code.zfill(5)
        # rand_num = str(random.randint(0,200)).zfill(4)
        rand_num = str(self.type.unique_id).zfill(5)

        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f'{self.office.id}{z_code}{rand_num}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f'{uuid.uuid4()}.png', File(buffer), save=False)
        print('DONE')
        # print_text(self.barcode)
        return super().save(*args,**kwargs)

class AssetHistory(models.Model):
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.asset.code} - {self.asset.name} - {self.created}'