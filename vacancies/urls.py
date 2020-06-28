from django.urls import path

from jobs.views import CategoryVacanciesView
from jobs.views import CompaniesView
from jobs.views import CompanyView
from jobs.views import MainView
from jobs.views import VacanciesView
from jobs.views import VacancyView
from jobs.views import custom_handler404

urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view()),
    path('vacancies/cat/<str:category>/', CategoryVacanciesView.as_view()),
    path('companies/<int:company_id>/', CompanyView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view()),
    path('companies/', CompaniesView.as_view()),
]

handler404 = custom_handler404
