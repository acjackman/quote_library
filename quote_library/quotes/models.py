from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel

from ..authors.models import Author


class Quote(TimeStampedModel):

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    text = models.TextField()
    author = models.ForeignKey(Author)
    added = models.DateTimeField()
    date = models.DateTimeField(null=True, blank=True)
    source = models.TextField(blank=True)
    reference = models.TextField(blank=True)
    verified = models.BooleanField(default=False)  # reference has been verified
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0, "ratings shouldn't be negative"),
            MaxValueValidator(10, "the maximum rating is 10"),
        ],
    )

    def __str__(self):
        return '"%s"' % (' '.join(self.text.split()[1:5]))

    def get_absolute_url(self):
        return reverse('quotes:detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.id and self.added is None:
            self.added = timezone.now()  # Set added if not set manually
        super(Quote, self).save()
