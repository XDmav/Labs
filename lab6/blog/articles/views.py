from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                if Article.objects.filter(title=form["title"]):
                    # если название статьи не уникально
                    form['errors'] = u"Название статьи не уникально"
                else:
                    article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('get_article', article_id=article.id)
                    # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'create_post.html', {})
    raise Http404


def registration(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'login': request.POST["login"],
                'email': request.POST["email"],
                'password': request.POST["password"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["login"] and form["email"] and form["password"]:
                # если поля заполнены без ошибок
                try:
                    User.objects.get(username=form["login"])
                    # если логин уже существует
                    form['errors'] = u"Логин уже существует"
                except User.DoesNotExist:
                    User.objects.create_user(form["login"], form["email"], form["password"])
                    return redirect('archive')
                    # перейти на страницу архива
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'register.html', {})
    return redirect('archive')


def auth(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'login': request.POST["login"],
                'password': request.POST["password"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["login"] and form["password"]:
                # если поля заполнены без ошибок
                user = authenticate(username=form["login"], password=form["password"])
                if user is not None:
                    login(request, user)
                    return redirect('archive')
                    # перейти на страницу архива
                form['errors'] = u"Не правильный логин или пароль"
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'login.html', {})
    return redirect('archive')
