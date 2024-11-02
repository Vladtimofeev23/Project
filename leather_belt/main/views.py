from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def buyer(request):
    data = {
        'title': 'Покупателю',
    }
    return render(request, 'main/buyer.html', data)


def about(request):
    data = {
        'title': 'О нас',
    }
    return render(request, 'main/about.html', data)


def contacts(request):
    data = {
        'title': 'Контакты',
    }
    return render(request, 'main/contacts.html', data)


