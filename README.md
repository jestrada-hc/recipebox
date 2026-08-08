# The Recipe Box

A home-cooking recipe collection built with Django. Browse recipes by category,
search by title/ingredient, and view full ingredient lists and step-by-step
instructions on a per-recipe page.

## Stack / patterns

- Django 6.1, class-based views (`ListView`, `DetailView`)
- Models: `Category`, `Tag` (many-to-many with `Recipe`), `Recipe`
- Search (`?q=`) and category filtering (`?category=`) combined in one queryset
- Pagination (9 recipes per page)
- Plain CSS, no frontend framework or build step

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata seed_data
python manage.py createsuperuser   # optional, for /admin/
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Project layout

- `recipes/models.py` — `Category`, `Tag`, `Recipe`
- `recipes/views.py` — `RecipeListView`, `RecipeDetailView`
- `recipes/templates/recipes/` — `base.html`, `recipe_list.html`, `recipe_detail.html`
- `recipes/static/recipes/css/style.css` — all styling
- `recipes/fixtures/seed_data.json` — sample categories, tags, and recipes
