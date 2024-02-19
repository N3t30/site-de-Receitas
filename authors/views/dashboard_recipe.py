from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from authors.forms.recipe_forms import AuthorRecipeForm
from recipes.models import Recipe


# Quando trabalhamos com Class Based views precisamos herdar de algo
@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipe(View):
    def get_recipe(self, id=None):
        recipe = None

        if id is not None:
            recipe = Recipe.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
            ).first()

            if not recipe:
                raise Http404()

        return recipe

    def render_recipe(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_recipe.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):
        recipe = self.get_recipe(id)
        form = AuthorRecipeForm(instance=recipe)
        return self.render_recipe(form)

    def post(self, request, id=None):
        recipe = self.get_recipe(id)

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
            return redirect(
                reverse(
                    "authors:dashboard_recipe_edit", args=(
                        recipe.id,
                    )
                )
            )

        return self.render_recipe(form)
