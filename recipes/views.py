from django.db.models import Q
from django.views.generic import ListView, DetailView

from .models import Category, Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset().select_related("category").prefetch_related("tags")

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query)
            )

        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["query"] = self.request.GET.get("q", "")
        context["active_category"] = self.request.GET.get("category", "")
        return context


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"
    slug_field = "slug"
    slug_url_kwarg = "slug"
