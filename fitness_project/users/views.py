from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
        else:
            # Выводим ошибки в консоль
            print("Форма невалидна. Ошибки:", form.errors.as_json())
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})