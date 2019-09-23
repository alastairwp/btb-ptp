from django.db import models
from ptpadmin.models import Course


class Category(models.Model):
    name = models.CharField("Category Name", max_length=255, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField("Sub-Category Name", max_length=255, null=False, blank=False)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Sub-categories"

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.TextField()
    number = models.PositiveIntegerField("Question number", default=0)
    subcategory = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL)


class Vote(models.Model):
    user = models.IntegerField()
    value = models.IntegerField()
    question = models.ForeignKey(Question, null=False, blank=False, on_delete=models.SET(0))
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    comment_data = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class Hint(models.Model):
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    text = models.CharField("Hint Text", max_length=255, null=False, blank=False)
    position = models.CharField("Hint Position", max_length=5, null=False, blank=False)








