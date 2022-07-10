from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User

from lit.form.follow import Follow
from lit.form.register import RegisterForm
from lit.form.ticket_add import TicketAdd
from lit.form.unfollow import Unfollow
from lit.models import Ticket, UserFollows


@login_required
def index(request):
    return redirect("flux/")

def register(request: WSGIRequest):
    if request.method == 'POST':
        register = RegisterForm(request.POST)
        if register.is_valid():
            register.save()
            return redirect("/")

    return render(request, "registration/register.html", context={"form":RegisterForm})

@login_required
def follow(request: WSGIRequest):
    error = None
    success = None
    if request.method == "POST":
        form_follow = Follow(request.POST)
        form_unfollow = Unfollow(request.POST)
        if form_follow.is_valid():
            try:
                user = User.objects.get(username=form_follow.cleaned_data["follow"])
                follow = UserFollows(user=user, followed_user=request.user)
                follow.save()
                success = f"Vous suivez désormais {form_follow.cleaned_data['follow']}"
            except:
                error = f"L'utilisateur {form_follow.cleaned_data['follow']} n'existe pas"
        elif form_unfollow.is_valid():
            try:
                user = User.objects.get(username=form_unfollow.cleaned_data["unfollow"])
                follow_relation = UserFollows.objects.get(user=user, followed_user=request.user)
                follow_relation.delete()
                success = f"Vous ne suivez plus {user}"
            except:
                error = f"L'utilisateur {form_follow.cleaned_data['follow']} n'existe pas"

    followers = UserFollows.objects.filter(user=request.user)
    follows = UserFollows.objects.filter(followed_user=request.user)
    return render(request, "lit/follow.html", context={
        "form_follow": Follow,
        "form_unfollow": Unfollow,
        "followers": followers,
        "follows": follows,
        "error": error,
        "success": success
    })

@login_required
def flux(request: WSGIRequest):
    followers = UserFollows.objects.filter(user=request.user)
    follows = UserFollows.objects.filter(followed_user=request.user)
    print(follows.query)
    return render(request, "lit/flux.html", context={
        # "posts": posts
    })

@login_required
def ticket_add(request: WSGIRequest):
    if request.method == "POST":
        form = TicketAdd(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save(request)

    return render(request, "lit/ticket/ticket_add.html", context={
        "form_ticket_add": TicketAdd
    })