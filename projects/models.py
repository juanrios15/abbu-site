from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    summary = models.TextField(blank=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    content = RichTextField(blank=True)
    before_text = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:220]
        super().save(*args, **kwargs)
    
    @property
    def has_before(self) -> bool:
        return bool(self.before_text or self.before_images.exists())


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.project.title} - Image {self.pk}"

class ProjectBeforeImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="before_images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="projects/before/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
    def __str__(self):
        return f"{self.project.title} - Before Image {self.pk}"