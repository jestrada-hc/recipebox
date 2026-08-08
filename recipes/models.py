from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    DIFFICULTY_CHOICES = [
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (HARD, "Hard"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="recipes")
    tags = models.ManyToManyField(Tag, blank=True, related_name="recipes")
    description = models.TextField(help_text="A short one or two sentence teaser.")
    ingredients = models.TextField(help_text="One ingredient per line.")
    instructions = models.TextField(help_text="One step per line.")
    prep_minutes = models.PositiveIntegerField()
    cook_minutes = models.PositiveIntegerField()
    servings = models.PositiveIntegerField(default=4)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=EASY)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe_detail", kwargs={"slug": self.slug})

    @property
    def total_minutes(self):
        return self.prep_minutes + self.cook_minutes

    @property
    def ingredient_list(self):
        return [line.strip() for line in self.ingredients.splitlines() if line.strip()]

    @property
    def instruction_list(self):
        return [line.strip() for line in self.instructions.splitlines() if line.strip()]
