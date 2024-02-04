from django.db import models

# Create your models here.
# ○ Comment: [ Long: id, String: text ]

class Comment(models.Model) : 
    id = models.AutoField(primary_key= True)
    blogId = models.BigIntegerField()
    text = models.CharField(max_length = 500)

    def __str__(self) : 
        return str(self.id) + " : " + self.text[:20]
    