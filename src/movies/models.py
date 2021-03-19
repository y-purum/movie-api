from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title or ''
        

class Genre(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title or ''


class Director(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=8, null=True)

    def __str__(self):
        return self.name or ''


class Actor(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=8)

    def __str__(self):
        return self.name or ''


class MovieInfo(models.Model):
    RATING_CHOICES = (
        ('G', 'General Audiences'),
        ('PG', 'Parental Guidance'),
        ('PG-13', 'Parents Strongly Cautioned'),
        ('R', 'Restricted'),
        ('NC-17', 'No One 17 And  Under Admitted')
    )

    title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING_CHOICES, max_length=8)
    genre = models.ManyToManyField(Genre, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor, blank=True)
    release_year = models.IntegerField()
    runtime = models.CharField(max_length=8)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-create_date', )

    def __str__(self):
        return str(self.title)