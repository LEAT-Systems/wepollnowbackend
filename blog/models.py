from django.db import models
from user.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_pics", default="Account-user.png")
    date_posted = models.DateTimeField(auto_now_add='True')

    def __str__(self):
        return self.title
