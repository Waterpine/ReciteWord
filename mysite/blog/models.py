from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    number_four = models.IntegerField(default=0)
    number_six = models.IntegerField(default=0)
    number_toefl = models.IntegerField(default=0)
    test_four = models.IntegerField(default=0)
    test_six = models.IntegerField(default=0)
    test_toefl = models.IntegerField(default=0)
    review_four = models.IntegerField(default=0)
    review_six = models.IntegerField(default=0)
    review_toefl = models.IntegerField(default=0)
    already_in = models.IntegerField(default=0)
    note_now = models.IntegerField(default=0)
    note_number = models.IntegerField(default=0)
    test_number = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Four(models.Model):
    id_num = models.IntegerField(default=0)
    vocabularys = models.CharField(max_length=100)
    paraphrases = models.CharField(max_length=300)


class Six(models.Model):
    id_num = models.IntegerField(default=0)
    vocabularys = models.CharField(max_length=100)
    paraphrases = models.CharField(max_length=300)


class Toefl(models.Model):
    id_num = models.IntegerField(default=0)
    vocabularys = models.CharField(max_length=100)
    paraphrases = models.CharField(max_length=300)


class Vocabularysnote(models.Model):
    username = models.CharField(max_length=50)
    vocabularys = models.CharField(max_length=100)
    paraphrases = models.CharField(max_length=300)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    #create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

