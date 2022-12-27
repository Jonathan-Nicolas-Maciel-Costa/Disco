from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db.models import signals


class UserManager(BaseUserManager):
    #

    def _create_user(self, username, matricula, email, password, **extra_fields):
        """ if not email:
            raise ValueError("O e-mail é obrigatório") """
        email = self.normalize_email(email)
        """ username = seusername
        matricula = seemail """
        
        user = self.model(email=email, matricula=matricula,username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, matricula, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(username, matricula,email, password, **extra_fields)

    def create_superuser(self, username, matricula, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_user(username, matricula, email, password, **extra_fields)


class CustomUser(AbstractUser):

    #email = models.EmailField("E-mail", unique=True)
    matricula = models.CharField("Matricula", max_length=150, unique=True)
    phone = models.CharField("Telefone", max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    username = models.CharField(("Nome"), max_length=50, unique=False, primary_key=None)
    image = models.ImageField(('Image de perfil'), upload_to='imagens', default = None)

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['first_name', 'email' ,'username', 'phone']

    def __str__(self):
        return self.username

    objects = UserManager()


#def user_pre_save(signal, instance, sender, **kwargs):
#    instance.username = instance.email


#signals.pre_save.connect(user_pre_save, sender=CustomUser)
