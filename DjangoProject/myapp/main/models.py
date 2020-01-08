from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

class User(AbstractUser):
    nickname = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=100)
    sim_text = models.TextField(max_length=150, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    user_img= models.URLField(max_length=400)
    back_img= models.URLField(max_length=400)
 
class board(models.Model):
    title= models.CharField(max_length=30)
    text = models.TextField(max_length=500)
  #  def __unicode__(self):
  #      return self.user.username
    
class comment(models.Model):
    posting = models.ForeignKey(board,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=50)
    
    

"""
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    text = models.TextField(max_length=500)





class UserManage(BaseUserManager):
    def _create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('id req.')
        user = self.model(username=self.normalize_username(username), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, username, password, **kwargs):

        kwargs.setdefault('is_admin', False)
        return self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):

        kwargs.setdefault('is_admin', True)
        return self._create_user(username, password, **kwargs)


class user(AbstractBaseUser):
    email = models.EmailField(unique=True, verbose_name='이메일')
    username = models.CharField(max_length=20,unique=True, verbose_name='이름')
    nickname = models.CharField(max_length=30,verbose_name='별명')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    is_active = models.BooleanField(default=True, verbose_name='사용중')
    is_admin = models.BooleanField(default=False, verbose_name='관리자')

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['nickname']
    objects = UserManage()
class Meta:
    db_table = 'user'
    verbose_name = '유저'
    verbose_name_plural = '유저들'



class profile (AbstractUser):
   # user = models.OneToOneField(User , on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    nickname= models.CharField(max_length=50)
    user_img=models.URLField(max_length=200)
    back_img=models.URLField(max_length=200)

    def save(self, commit=True):
        # Save the provided password in hashed format
        profile = super(MyForm, self).save(commit=False)
        profile.set_password(self.cleaned_data["password"])
        if commit:
            profile.save()
        return profile

    def __str__(self):
        return self.user.username
"""
