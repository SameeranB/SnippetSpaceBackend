from django.db import models

# Create your models here.
from Accounts.models import User
from SnippetSpaceBackend import settings

LANGUAGE_CHOICES = (
    ('Python', 'Python'),
    ['Django', 'Django']
    # ('c++', 'C++'),
    # ('javascript', 'Javascript')

)


class Snippet(models.Model):
    snippet_id = models.AutoField(primary_key=True)
    framework = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='snippets')
    instructions = models.TextField()
    code = models.TextField()

    def is_owner(self, user):
        return self.author == user

    @property
    def author_name(self):
        username = self.author.username
        return username

