from django.shortcuts import render
import requests
from django.views import View
import datetime
from dbjob.forms import AddPostForm
from dbjob.models import Graph


class FormCreate(View):
    def get(self, request):
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                print(form)
        else:
            form = AddPostForm()
        return render(request, 'form.html', {'form': form})

    my_list = list()

    def post(self, request):
        print(dir(request))


class FormCreate(View):
    def get(self, request):
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            if form.is_valid():
                print(form)
        else:
            form = AddPostForm()
        return render(request, 'form.html', {'form': form, 'title': 'Выберите число'})

    def post(self, request):
        day = []
        day.append(request.POST['digit'])
        day1 = day[0]
        try:

            vacancies = requests.get(
                f'https://api.hh.ru/vacancies?specialization=1&date_from=2022-12-{day1}T00:00:00&date_to=2022-12-{day1}T23:59:59&text=NAME:(Администратор+баз+данных+OR+oracle+OR+оператор+баз+данных+OR+базы+данных+OR+mysql+OR+data+base+OR+database+OR+dba+OR+bd+OR+бд+OR+базами+данных)&only_with_salary=true&order_by=publication_time&per_page=10').json()[
                'items']
        except:
            return render(request, 'erorr.html')

        if len(vacancies) > 0:
            jobs_list = []
            for vac in vacancies:
                jobs_list.append(requests.get(f'https://api.hh.ru/vacancies/{vac["id"]}').json())

            list_vacancies = []
            for vac in jobs_list:
                vacancies_info = {
                    'name': vac['name'],
                    'description': vac['description'],
                    'key_skills': ', '.join(skill['name'] for skill in vac['key_skills']),
                    'employer': vac['employer']['name'],
                    'salary': f"{int((int(vac['salary']['from'] or 0) + int(vac['salary']['to'] or 0))):,} {vac['salary']['currency']}",
                    'area': vac['area']['name'],
                    'published_at': datetime.datetime.strptime(vac['published_at'].replace('T', ' ')[:18],
                                                               '%Y-%m-%d %H:%M:%S'),
                    'alternate_url': vac['alternate_url'],

                }
                list_vacancies.append(vacancies_info)
            context = {"data": list_vacancies}
            return render(request, 'lastVacancies.html', context=context)

        return render(request, 'error.html')


def home(request):
    return render(request, 'index.html')


def geography(request):
    graphs = Graph.objects.all()
    return render(request, 'geography.html', {'graphs': graphs})


def skills(request):
    return render(request, 'skills.html')


def lastVacancies(request):
    return render(request, 'lastVacancies.html')


def demand(request):
    graphs = Graph.objects.all()
    return render(request, 'demand.html', {'graphs': graphs})


def error(request):
    return render(request, 'error.html')
