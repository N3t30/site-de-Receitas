from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from slugify import slugify

from authors.forms.recipe_forms import AuthorRecipeForm
from recipes.models import Recipe

from .forms import LoginForm, RegisterForm


def generate_unique_slug(title):
    base_slug = slugify(title)
    unique_slug = base_slug
    counter = 1

    while Recipe.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{base_slug}-{counter}"
        counter += 1

    return unique_slug


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('authors:register_create'),
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    # validação
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'your user is created, please login.')

        del (request.session['register_form_data'])
        return redirect(reverse('authors:login'))
    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user:
            messages.success(request, 'your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'invalid credentials')
    else:
        messages.error(request, 'Error to validate form data')

    return redirect(reverse('authors:dashboard'))

# login required pode ser olocada em viewa fechadas


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        messages.error(request, 'invalid logout request')
        return redirect(reverse('authors:login'))

    if request.POST.get('username') != request.user.username:
        messages.error(request, 'invalid logout user')
        return redirect(reverse('authors:login'))

    messages.success(request, 'logged out successfully')
    logout(request)
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    recipes = Recipe.objects.filter(
        is_published=False,
        author=request.user
    )
    return render(request, 'authors/pages/dashboard.html',
                  {
                      'recipes': recipes,
                  })


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_recipe_edit(request, id):
    recipe = Recipe.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()

    if not recipe:
        raise Http404()

    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=recipe
    )

    if form.is_valid():
        # Agora, o form é valido e eu posso tentar salvar.
        # Cria o formulário finge que vai salvar os dados, mas não salva
        recipe = form.save(commit=False)

        # Garantir que o usuario esta vendo o formulário dele
        recipe.author = request.user
        # Nunca vou permitir que esse form receba html
        recipe.preparation_steps_is_html = False
        # Sempre que salvar nunca será puclicada
        recipe.is_published = False

        recipe.save()

        messages.success(request, 'Sua receita foi salva com sucesso!')
        return redirect(reverse("authors:dashboard_recipe_edit", args=(id,)))

    return render(
        request,
        'authors/pages/dashboard_recipe.html',
        context={
            'form': form
        }
    )


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_recipe_new(request):
    form = AuthorRecipeForm(
        data=request.POST or None,
        files=request.FILES or None
    )

    if form.is_valid():
        # Agora, o form é valido e eu posso tentar salvar.
        # Cria o formulário finge que vai salvar os dados, mas não salva
        recipe: Recipe = form.save(commit=False)

        # Garantir que o usuario esta vendo o formulário dele
        recipe.author = request.user
        # Nunca vou permitir que esse form receba html
        recipe.preparation_steps_is_html = False
        # Sempre que salvar nunca será puclicada
        recipe.is_published = False
        recipe.slug = generate_unique_slug(recipe.title)

        recipe.save()

        messages.success(request, 'Sua receita foi salva com sucesso!')
        return redirect(reverse("authors:dashboard_recipe_edit", args=(
            recipe.id,))
        )

    return render(
        request,
        'authors/pages/dashboard_recipe.html',
        context={
            'form': form,
            'form_action': reverse('authors:dashboard_recipe_new')
        }
    )
