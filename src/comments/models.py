from django.db import models


class AbstractComment(models.Model):
    """abstract model of comments"""
    text = models.TextField("Мessage", max_length=512)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        abstract = True
