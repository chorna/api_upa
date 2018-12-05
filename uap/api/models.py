# coding:utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager, PermissionsMixin, UserManager
from django.conf import settings

# Create your models here.


class MyUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()
    username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    register_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'username'

    def __unicode__(self):
        if self.username:
            return self.username
        return 'Anónimo'

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return "%s" % self.username

    def get_short_name(self):
        "Returns the short name for the user."
        return self.username

    #def email_user(self, subject, message, from_email=None, **kwargs):
        #"""
        #Sends an email to this User.
        #"""
        #send_mail(subject, message, from_email, [self.email], **kwargs)


    class Meta:
        ordering = 'username',
        verbose_name = 'Usuario'


class Seccion(models.Model):
    codseccion = models.CharField(max_length=20)


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(blank=True, null=True)
    foto = models.BinaryField(blank=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    seccion = models.ForeignKey(Seccion, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class Alumno(Persona):
    pass


class Nota(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.FloatField()
    motivo = models.CharField(max_length=200, blank=True, null=True)
    evaluacion = models.CharField(max_length=200, blank=True, null=True)


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codecurso = models.CharField(max_length=20)
    cicloacademico = models.CharField(max_length=20)


class Profesor(Persona):
    pass
