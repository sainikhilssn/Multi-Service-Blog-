from django.db import models

# Create your models here.
# ○ Blog: [ Long: id, String: title, String: content ]

class Blog(models.Model) : 
    id = models.AutoField(primary_key= True)
    title = models.CharField(max_length = 300)
    content  = models.TextField() 
    def __str__(self) : 
        return str(self.id) + " : " + self.title
    
   