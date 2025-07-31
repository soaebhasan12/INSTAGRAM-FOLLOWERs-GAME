from django.shortcuts import render, redirect
from django.contrib import admin
from .models import Upload
import random

# Create your views here.

def home(request):
    return render(request, 'gameApp/home.html')


def gamePlay(request):
    message = None
    is_correct = False

    if 'restart' in request.GET:
        keys = ['account_a', 'account_b', 'score']
        for key in keys:
            if key in request.session:
                del request.session[key]
        request.session['score'] = 0

    if 'score' not in request.session:
        request.session['score'] = 0

    score = request.session['score']

    if 'account_a' in request.session and 'account_b' in request.session:
        account_a = Upload.objects.get(id=request.session['account_a'])
        account_b = Upload.objects.get(id=request.session['account_b'])
    else:
        account_a = Upload.objects.order_by("?").first()
        account_b = Upload.objects.order_by("?").first()

        while account_a == account_b:
            account_b = Upload.objects.order_by("?").first()

        request.session['account_a'] = account_a.id
        request.session['account_b'] = account_b.id

    if 'user_choice' in request.GET:
        guess = request.GET.get('user_choice')
        is_correct = check_answer(guess, account_a.follower_count, account_b.follower_count)

        if is_correct:
            score += 1
            request.session['score'] = score
            message = f"You're right! Current Score: {score}"

            account_a = account_b
            account_b = Upload.objects.order_by("?").first()

            while account_a == account_b:
                account_b = Upload.objects.order_by("?").first()

            request.session['account_a'] = account_a.id
            request.session['account_b'] = account_b.id
        else:
            message = f"Sorry, that's wrong. Final Score: {score}."
            request.session['score'] = 0  # Game reset

    context = {
        'message': message,
        'account_a_name': account_a.name,
        'account_b_name': account_b.name,
        'account_a_from': account_a.country,
        'account_b_from': account_b.country,
        'account_a_description': account_a.description,
        'account_b_description': account_b.description,
        'account_a_image': account_a.image.url,  
        'account_b_image': account_b.image.url,  
        'account_a_follower': account_a.follower_count,
        'account_b_follower': account_b.follower_count,
    }
    return render(request, 'gameApp/play.html', context)


def check_answer(guess, account_a_follower, account_b_follower):
    """Check if the user's guess is correct."""
    if account_a_follower > account_b_follower:
        return guess.lower() == "a"
    elif account_a_follower < account_b_follower:
        return guess.lower() == "b"
    return False


def about(request):
    return render(request, 'gameApp/about.html')

def contact(request):
    return render(request, 'gameApp/contact.html')

def LogIn(request):
    return redirect('/admin/login/')