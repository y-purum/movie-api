from django.contrib import admin

from . import models

@admin.register(models.MovieInfo)
class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'create_date', 'update_date')


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')


@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')