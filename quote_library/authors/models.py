from django.db import models
from django.urls import reverse


class Author(models.Model):

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    prefix = models.CharField(max_length=150, blank=True)
    first_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150)
    suffix = models.CharField(max_length=150, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    birth_date_year = models.BooleanField(default=False)
    death_date_year = models.BooleanField(default=False)
    profession = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.full_name()

    def short_name(self):
        name = ""
        if self.first_name != "":
            name = name + self.first_name + " "
        return name + self.last_name

    def full_name(self):
        name = ""
        if self.prefix != "":
            name = self.prefix + " "
        if self.first_name != "":
            name = name + self.first_name + " "
        if self.middle_name != "":
            name = name + self.middle_name + " "

        post_name = ""
        if self.suffix != "":
            post_name = " " + self.suffix

        return name + self.last_name + post_name

    def get_absolute_url(self):
        return reverse('authors:detail', args=[str(self.id)])
