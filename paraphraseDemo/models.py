from django.db import models

# Create your models here.
class PromptText(models.Model):
    prompt=models.TextField(max_length=2000)
    


    def __str__(self):
        return self.prompt