from django.db import models

# Create your models here.

# Service Model
class Service(models.Model):
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('completed', 'Completed'),
    ]
    
    requester = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='requested_services'
    )
    
    fulfiller = models.ForeignKey(
        User,
        null = True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='fulfilled_services'
    )
    
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    

# ServiceProposal Model
class ServiceProposal(models.Model):
    
    service_id = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='proposals'
    )
    
    responder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='service_proposals'
    )
    messsage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)