from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class MyAccountManager(BaseUserManager):
    def create_user(self, email,first_name, last_name,  birthday, gender, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            Email_Address=self.normalize_email(email),
            first_name=first_name,
            last_name = last_name,
            Date_of_Birth=birthday,
            gender=gender,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Email_Address, password):
        user = self.create_user(
            Email_Address=self.normalize_email(Email_Address),
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Users(AbstractBaseUser):
    username = None
    Email_Address = models.EmailField(verbose_name="email", max_length=60, unique=True, blank=True, null=True, default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Date_of_Birth = models.CharField(max_length=30, blank=True, null=True, default=None)
    gender = models.CharField(max_length=30, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'Email_Address'

    objects = MyAccountManager()

    REQUIRED_FIELDS=[]

    class Meta:
        db_table = "tbl_users"

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None): return self.is_superuser

    def has_module_perms(self, app_label): return self.is_superuser
