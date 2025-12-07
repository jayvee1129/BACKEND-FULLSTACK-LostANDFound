from django.db import models

class Item(models.Model):
    STATUS_CHOICES = [('LOST', 'Lost'), ('FOUND', 'Found')]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True, db_index=True)
    contact_info = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='items/', null=True, blank=True)

    class Meta:
        ordering = ['-date_posted']
        indexes = [
            models.Index(fields=['-date_posted']),
        ]

    def __str__(self):
        return self.title