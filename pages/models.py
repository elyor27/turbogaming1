from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phones = models.CharField(max_length=14)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


