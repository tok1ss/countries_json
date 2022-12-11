from django.core.paginator import Paginator
from django.shortcuts import render
import json

with open('/home/student/DjangoCOUNTRIES/data/country-by-languages.json') as f:
    countries_data = json.load(f)


def about(request):
    array = {
        'title': 'main',
    }
    return render(request, 'abobus.html', array)


def countries_index(request, id_country):
    alphabet = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array1 = []
    a = []
    if id_country in alphabet:
        for i in countries_data:
            if i['country'][0] == id_country:
                array1.append(i['country'])

        paginator = Paginator(array1, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        array = {
            'title': 'countries',
            'array1': array1,
            'mas': alphabet,
            'page_object': page_obj
        }
        return render(request, 'countries.html', array)
    else:
        for i in countries_data:
            if str(i['country']) == id_country:
                a += i['languages']
                a = ", ".join(a)
            array1 = {
                'title': id_country,
                'array': a
            }
        return render(request, 'country_lang.html', array1)


def countries_list(request):
    alphabet = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array1 = []
    for i in countries_data:
        array1.append(i['country'])

    paginator = Paginator(array1, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    array = {
        'title': 'countries',
        'array1': array1,
        'mas': alphabet,
        'page_object': page_obj
    }

    return render(request, 'countries.html',array)


def languages_index(request, id_language):
    alphabet = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array3 = []
    a = ''
    if id_language in alphabet:
        for i in countries_data:
            for j in i['languages']:
                if j[0] == id_language:
                    array3.append(j)
        array3 = set(array3)
        array3 = sorted(array3)
        paginator = Paginator(array3, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        array1 = {
            'title': 'languages',
            'array': array3,
            'mas': alphabet,
            'page_object': page_obj
        }

        return render(request, 'languages.html', array1)
    else:
        for i in countries_data:
            for j in i['languages']:
                if id_language == j:
                    a += i['country']+', '
        a = a[:-2]
        array1 = {
            'title': id_language,
            'array': a
        }
        return render(request, 'lang_count.html', array1)


def languages_list(request):
    alphabet = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array3 = []
    for i in countries_data:
        for j in i['languages']:
            array3.append(j)
    array3 = set(array3)
    array3 = sorted(array3)
    paginator = Paginator(array3, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    array1 = {
        'title': 'languages',
        'array': array3,
        'mas': alphabet,
        'page_object': page_obj
    }

    return render(request, 'languages.html', array1)


