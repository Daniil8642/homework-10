from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user_profile = request.user.userprofile
            author.save()
            return redirect('home')  # Перенаправлення на домашню сторінку після додавання автора
    else:
        form = AuthorForm()

    return render(request, 'add_author.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()
            return redirect('home')  # Перенаправлення на домашню сторінку після додавання цитати
    else:
        form = QuoteForm()

    return render(request, 'add_quote.html', {'form': form})
