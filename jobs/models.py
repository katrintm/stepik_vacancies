from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.CharField(max_length=64)
    description = models.TextField()
    employee_count = models.IntegerField()


class Speciality(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.CharField(max_length=64)


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    speciality = models.ForeignKey(
        Speciality,
        related_name='vacancies',
        on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company,
        related_name='vacancies',
        on_delete=models.CASCADE)
    skills = models.CharField(max_length=256)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
