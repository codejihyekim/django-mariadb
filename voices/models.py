from django.db import models

class Voice(models.Model):
    use_in_migrations = True
    voiceid = models.CharField(primary_key=True, max_length=10)
    regDate = models.DateField()

    class Meta:
        db_table="voices"

    def __str__(self):
        return f'{self.pk} {self.voiceid}'