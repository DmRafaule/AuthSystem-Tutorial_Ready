from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Users(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(type, kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Users, self).save(*args, **kwargs)
