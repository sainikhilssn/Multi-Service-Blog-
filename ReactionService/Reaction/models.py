from django.db import models

# Create your models here.
# ○ Reaction: [ Long: id, ReactionType: type, TargetType: targetType, Long: targetId ]


class Reaction(models.Model) : 
    TargetType = [('blog' , 'blog') , ('comment' , 'comment')]
    ReactionType = [('like' , 'like') , ('dislike' , 'dislike')]
    id = models.AutoField(primary_key= True)
    typeId = models.BigIntegerField()
    targetType = models.CharField(max_length = 8, choices = TargetType)
    reactionType = models.CharField(max_length = 8 , choices = ReactionType)

    class Meta:
        unique_together = (('targetType', 'typeId'),)

    def __str__(self) : 
        return str(self.id) + " : " + self.reactionType + " " + self.targetType
    
