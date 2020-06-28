from django.db.models import Count
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from jobs.models import Company
from jobs.models import Speciality
from jobs.models import Vacancy


class MainView(View):
    def get(self, request):
        specialities = Speciality.objects.all(). \
            annotate(count=Count('vacancies'))
        companies = Company.objects.all(). \
            annotate(count=Count('vacancies'))
        return render(
            request, 'index.html', context={
                'specialities': specialities,
                'companies': companies
            }
        )


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        word_for_vacancies = vacancies_ending(len(vacancies))
        return render(
            request, 'vacancies.html', context={
                'vacancies': vacancies,
                'title': 'Все вакансии',
                'word_for_vacancies': word_for_vacancies
            }
        )


class CategoryVacanciesView(View):
    def get(self, request, category):
        try:
            speciality = Speciality.objects.get(code=category)
        except Speciality.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        vacancies = Vacancy.objects.filter(speciality=speciality)
        word_for_vacancies = vacancies_ending(len(vacancies))
        return render(
            request, 'vacancies.html', context={
                'vacancies': vacancies,
                'title': speciality.title,
                'word_for_vacancies': word_for_vacancies
            }
        )


class CompanyView(View):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        vacancies = Vacancy.objects.filter(company=company)
        word_for_vacancies = vacancies_ending(len(vacancies))
        return render(
            request, 'company.html', context={
                'company': company,
                'vacancies': vacancies,
                'word_for_vacancies': word_for_vacancies
            }
        )


class VacancyView(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist:
            return render(
                request, '404.html', context={
                }
            )
        company = Company.objects.get(id=vacancy.company.id)
        return render(
            request, 'vacancy.html', context={
                'vacancy': vacancy,
                'company': company
            }
        )


class CompaniesView(View):
    def get(self, request):
        companies = Company.objects.all()
        return render(
            request, 'companies.html', context={
                'companies': companies
            }
        )


def custom_handler404(request, exception):
    return render(
        request, '404.html', context={
        }
    )


def vacancies_ending(number_of_vacancies):
    if (number_of_vacancies == 1) or \
            (number_of_vacancies > 20 and number_of_vacancies % 10 == 1):
        return 'вакансия'
    elif (number_of_vacancies in (2, 3, 4)) or \
            (number_of_vacancies > 20 and
             number_of_vacancies % 10 in (2, 3, 4)):
        return 'вакансии'
    else:
        return 'вакансий'
