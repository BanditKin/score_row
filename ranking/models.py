from django.db import models

# Create your models here.


class RankingInfo(models.Model):
    client = models.CharField(max_length=15, verbose_name='名称', unique=True)
    score = models.IntegerField(default=0, verbose_name='分数')

    class Meta:
        db_table = 'USER_SCORE'

    def __str__(self):
        return ('%s:%s')%(self.client, self.score)
