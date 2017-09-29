from django.db import models
<<<<<<< HEAD
=======
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
>>>>>>> df24d45e659265e23318ffa9b13316302bbd27af

# Create your models here.
class ClienteManager(BaseUserManager):

    def _create_user(self, username, password,
                     is_staff, 
                     is_superuser, **extra_fields):
        now = timezone.now()
        user = self.model(username=username,
                          is_staff=is_staff, 
                          is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, True, True,
                                 **extra_fields)

class Cliente(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(_('username'), max_length=50, unique=True)
	email = models.EmailField(_('email address'), max_length=254, unique=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)	
	cedula = models.CharField(max_length=10, blank=True, null=True)
	direccion = models.CharField(max_length=100, blank=True, null=True)
	telefono = models.CharField(max_length=100, blank=True, null=True)
	is_staff = models.BooleanField(_('staff status'),default=False, help_text=_('Designates whether the user can log into this admin site.'))
	is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))

	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = ClienteManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('Cliente')
		verbose_name_plural = _('Clientes')

	

	def get_absolute_url(self):
		return "/users/%s/" % urlquote(self.username)

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])

<<<<<<< HEAD
class Cliente(models.Model):
=======
	def __str__(self):              # __unicode__ on Python 2
		return self.username

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True
>>>>>>> df24d45e659265e23318ffa9b13316302bbd27af

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

<<<<<<< HEAD

	nombres =models.CharField(max_length= 200)
	apellidos =models.CharField(max_length= 200)
	cedula =models.CharField(max_length= 200)
	direccion =models.CharField(max_length= 200)
	telefono =models.CharField(max_length=30)
	

	 

	def __str__(self):
		return "%s - %s - %s - %s - %s"%(self.nombres, self.apellidos, self.cedula, self.direccion ,self.telefono)
=======
>>>>>>> df24d45e659265e23318ffa9b13316302bbd27af
