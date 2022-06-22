from django.db import models

class Image(models.Model):
    use_in_migrations = True
    imageid = models.CharField(primary_key=True, max_length=10)
    regDate = models.DateField()

    class Meta:
        db_table="images"

    def __str__(self):
        return f'{self.pk} {self.imageid}'