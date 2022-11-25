from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_pics", default="Account-user.png")
    date_posted = models.DateTimeField(auto_now_add='True')

    def __str__(self):
        return self.title
