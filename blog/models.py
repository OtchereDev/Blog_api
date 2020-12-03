from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(choices=(('draft','draft'),
                                ('published','published'),), default='published',max_length=100)

    objects=models.Manager
    postobjects=PostObject

    class Meta:
        ordering=('-published',)    

    def __str__(self):
        return self.title