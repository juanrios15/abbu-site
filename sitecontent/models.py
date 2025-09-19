from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField


class HomePage(SingletonModel):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    body = RichTextField(blank=True)

    class Meta:
        verbose_name = "Homepage (Accueil)"
        verbose_name_plural = "Homepage (Accueil)"

    def __str__(self):
        return "Homepage (Accueil)"


class HomePageImage(models.Model):
    homepage = models.ForeignKey(
        HomePage, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="site/home/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Homepage image"
        verbose_name_plural = "Homepage images"

    def __str__(self):
        return f"Accueil image #{self.pk}"


class ServicesPage(SingletonModel):
    section1_title = models.CharField(max_length=200, blank=True)
    section1_body = RichTextField(blank=True)
    section2_title = models.CharField(max_length=200, blank=True)
    section2_body = RichTextField(blank=True)

    class Meta:
        verbose_name = "Prestations"
        verbose_name_plural = "Prestations"

    def __str__(self):
        return "Services (Prestations)"


class AboutPage(SingletonModel):
    title = models.CharField(max_length=200, blank=True)
    body = RichTextField(blank=True)
    image = models.ImageField(upload_to="site/", blank=True, null=True)

    class Meta:
        verbose_name = "Bureau"
        verbose_name_plural = "Bureau"

    def __str__(self):
        return "About (Bureau)"
