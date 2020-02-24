from django.db import models

# Create your models here.
from SnippetSpaceBackend import settings

LANGUAGE_CHOICES = (
    ('python', 'Python'),
    # ('c++', 'C++'),
    # ('javascript', 'Javascript')

)


class Snippet(models.Model):
    snippet_id = models.AutoField(primary_key=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='snippets')
    code_quality = models.FloatField(null=True)

    def is_owner(self, user):
        return self.author == user
