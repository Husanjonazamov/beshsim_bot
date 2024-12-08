# django import
from django.shortcuts import render
from django.views import View

# kode import
from .task import GetSim


class UcellSearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        try:
            latest_numbers = query
            sim_search = GetSim('ucell', latest_numbers)
            result = sim_search.handler()

            if not result['data']:
                context = {
                    'message': 'Afsuski, hech narsa topilmadi.',
                    'operator': 'ucell',
                    'query': query
                }
                return render(request, 'search/ucell.html', context)

            context = {
                'numbers': result['data'],
                'operator': 'ucell',
                'query': query
            }
            return render(request, 'search/ucell.html', context)
        except Exception as e:
            return render(request, 'search/ucell.html')


class BelineSearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')

        try:
            latest_numbers = query
            sim_search = GetSim('beeline', latest_numbers)
            result = sim_search.handler()

            if not result['data']:
                context = {
                    'message': 'Afsuski, hech narsa topilmadi.',
                    'operator': 'beeline',
                    'query': query
                }
                return render(request, 'search/beeline.html', context)

            context = {
                'numbers': result['data'],
                'operator': 'beeline',
                'query': query
            }
            return render(request, 'search/beeline.html', context)
        except Exception as e:
            return render(request, 'search/beeline.html', {'numbers': [], 'query': query, 'operator': 'beeline'})


class uztelecomSearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')

        try:
            latest_numbers = query
            sim_search = GetSim('uztelecom', latest_numbers)
            result = sim_search.handler()

            if not result['data']:
                context = {
                    'message': 'Afsuski, hech narsa topilmadi.',
                    'operator': 'uztelecom',
                    'query': query
                }
                return render(request, 'search/uztelecom.html', context)

            context = {
                'numbers': result['data'],
                'operator': 'uztelecom',
                'query': query
            }
            return render(request, 'search/uztelecom.html', context)
        except Exception as e:
            return render(request, 'search/uztelecom.html', {'numbers': [], 'query': query, 'operator': 'uztelecom'})


class humansSearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')

        try:
            latest_numbers = query
            sim_search = GetSim('humans', latest_numbers)
            result = sim_search.handler()

            if not result['data']:
                context = {
                    'message': 'Afsuski, hech narsa topilmadi.',
                    'operator': 'humans',
                    'query': query
                }
                return render(request, 'search/humans.html', context)

            context = {
                'numbers': result['data'],
                'operator': 'humans',
                'query': query
            }
            return render(request, 'search/humans.html', context)
        except Exception as e:
            return render(request, 'search/humans.html', {'numbers': [], 'query': query, 'operator': 'humans'})



def ucell_page(request):
    return render(request, 'search/ucell.html', {'title': 'Ucell'})


def beeline_page(request):
    return render(request, 'search/beeline.html', {'title': 'Beeline'})


def uzmobile_page(request):
    return render(request, 'search/uztelecom.html', {'title': 'Uzmobile'})


def humans_page(request):
    return render(request, 'search/humans.html', {'title': 'Humans'})


class NumberDetailView(View):
    def get(self, request, number):
        referer = request.META.get('HTTP_REFERER', None)
        return render(request, 'search/search_number_info.html', {'number': number, 'referer': referer})

