from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# CustomUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # This hashes the password
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
    
# User Class
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def __str__(self):
        return self.email

# Serivce Class
class Service(models.Model):
    
    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='requested_services'
    )
    
    fulfiller = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='fulfullied_services'
    )
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    
    Status_Choices = [
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    ]
    
    status = models.CharField(
        max_length=15,
        choices=Status_Choices,
        default='pending'
    )
    
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    

# ServiceProposal class
class ServiceProposal(models.Model):
    
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='proposals'
    )
    
    responder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='service_proposals'
    )
    
    message = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
# Message Class
class Message(models.Model):
    
    service = models.ForeignKey(
            Service,
            on_delete=models.CASCADE,
            related_name='messages'
        )
        
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender.email}: {self.content[:50]}"