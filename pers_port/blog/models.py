from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=250)
    pub_time = models.DateField()

    def __str__(self):
        return self.title + " " + self.desc[:10] + "..."
