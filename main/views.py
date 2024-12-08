# django import
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# kode import
from .models import Sim, Category, PhoneNumber





def sim_list(request):
    sims = Sim.objects.all()

    context = {
        'sims':sims
    }
    
    return render(request, 'sim.html', context)
    



def category_list(request, sim_id):
    categorys = Sim.objects.get(pk=sim_id).category.all()

    context = {
        'categorys':categorys,
        'sim_id': sim_id
    }
    
    return render(request, 'categorys.html', context)
    
    
    
    
def number_list(request, sim_id, category_id):
    query = request.GET.get('query', '')
    numbers = PhoneNumber.objects.filter(company=sim_id, category=category_id)

    if query:
        numbers = numbers.filter(number__icontains=query)

    paginator = Paginator(numbers, 10)  # 10 tadan bo'linadi
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Sahifalar sonini cheklash uchun maxsus paginator yaratish
    def get_paginator_range(page_obj, num_pages_display=3):
        current = page_obj.number
        last = paginator.num_pages
        start_range = max(current - num_pages_display // 2, 1)
        end_range = min(current + num_pages_display // 2, last)
        return range(start_range, end_range + 1), last

    page_range, last_page = get_paginator_range(page_obj)

    context = {
        'page_obj': page_obj,
        'page_range': page_range,
        'last_page': last_page,
        'sim_id': sim_id,
        'category_id': category_id,
        'query': query,
    }
    
    return render(request, 'numbers.html', context)


def search_numbers(request, sim_id, category_id):
    query = request.GET.get('query', '')
    numbers = PhoneNumber.objects.filter(
        company=sim_id,
        category=category_id,
        number__icontains=query  # To'rt raqamni qidirish
    )

    context = {
        'numbers': numbers,
        'sim_id': sim_id,
        'category_id': category_id,  # Bu joyni qo'shing
    }
    
    return render(request, 'numbers.html', context)




def previous_page(request, sim_id):
    # Ortga qaytish uchun sahifani belgilash
    return redirect('categories', sim_id=sim_id)  # sim_id orqali category_list'ga qaytish





def number_detail(request, number_id):
    number = get_object_or_404(PhoneNumber, id=number_id)
    
    # Sim va kategoriya ID larini olish
    sim_id = number.company.id  # Bu yerda company atributidan foydalanamiz
    category_id = number.category.id  # Bu yerda category atributidan foydalanamiz
    
    context = {
        'number': number,
        'sim_id': sim_id,
        'category_id': category_id,
    }
    return render(request, 'numbers_info.html', context)





def add_number(request):
    if request.method == 'POST':
        category_id = request.POST.get('category', None)
        sim_id = request.POST.get('sim', None)

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return redirect('/admin/main/phonenumber/') 

        try:
            sim = Sim.objects.get(id=sim_id)
        except Sim.DoesNotExist:
            return redirect('/admin/main/phonenumber/')  
        numbers = request.POST.get('numbers', '')  
        number_list = [num.strip() for num in numbers.replace(',', ' ').split() if num.strip()]

        phone_number_objects = [PhoneNumber(number=number, category=category, company=sim) for number in number_list]

        PhoneNumber.objects.bulk_create(phone_number_objects)

        return redirect('/admin/main/phonenumber/')  

    categories = Category.objects.all()
    sims = Sim.objects.all()
    return render(request, 'add_raqam.html', {'categories': categories, 'sims': sims})






@login_required
def is_admin(user):
    return user.is_superuser

