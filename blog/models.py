from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.models import (BaseUserManager,
                                        PermissionsMixin,
                                        AbstractBaseUser)

class CustomUserManager(BaseUserManager):
    
    def create_superuser(self,email,user_name,first_name,
                        last_name,password,**other_fields):
        
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True ')
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True ')

        return self.create_user(email,user_name,first_name,last_name,password,**other_fields)

    def create_user(self,email,user_name,first_name,
                        last_name,password,**other_fields):
        
        if not email:
            raise ValueError('Emails are required !')
        
        email=self.normalize_email(email)
        user= self.model(email=email,user_name=user_name,first_name=first_name,
                        last_name=last_name,**other_fields)
        user.set_password(password)
        
        user.save()

        return user

class Author(AbstractBaseUser,PermissionsMixin):
    user_name=models.CharField(max_length=255,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=350,unique=True)
    about=models.TextField()
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    start_date=models.DateTimeField(default=timezone.now)


    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['last_name','first_name','user_name']



class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObject(models.Manager):

        def get_queryset(self, *args, **kwargs):
            return super().get_queryset().filter(status='published')

    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='post_category',default=1)
    title = models.CharField(max_length=150)
    excerpt=models.TextField()
    content=models.TextField()
    slug = models.SlugField(max_length=100,unique=True)
    published=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    status = models.CharField(choices=(('draft','draft'),
                                ('published','published'),), default='published',max_length=100)

    objects=models.Manager
    postobjects=PostObject

    class Meta:
        ordering=('-published',)    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)