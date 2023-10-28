from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField
from froala_editor.fields import FroalaField
from django.core.mail import send_mail


class Testimonials(models.Model):
    image = models.ImageField(upload_to='Testimonial_images/')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    def __str__(self):
        return self.name

class Total(models.Model):
    title = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Total Count"
        verbose_name_plural = "Total Counts"

class Skills(models.Model):
    title = models.CharField(max_length=100)
    percentage = models.IntegerField()
    value = models.IntegerField()
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class Mydetails(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Details"

# class Contact(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     subject = models.CharField(max_length=255)
#     message = models.TextField()
#     class Meta:
#         verbose_name = "Contact"
#         verbose_name_plural = "Contact Me"

class Services(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description =  models.TextField(max_length=100)
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class Portfolio(models.Model):
    media_file = models.ImageField()
    title = models.CharField(max_length=100)
    alt = models.CharField(max_length=100)
    filter = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.title


class CategoryTitle(models.Model):
    title = models.CharField(max_length=100)
    filter = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Portfolio Categories"


class Resume(models.Model):
    title = models.CharField(blank=True, null=True, max_length=100)
    name = models.CharField(blank=True, null=True, max_length=100)
    body = models.TextField(blank=True, null=True, max_length=2000)
    list1 = models.CharField(blank=True, null=True, max_length=100)
    list2 = models.CharField(blank=True, null=True, max_length=100)
    list3 = models.CharField(blank=True, null=True, max_length=100)
    list4 = models.CharField(blank=True, null=True, max_length=100)
    list5 = models.CharField(blank=True, null=True, max_length=100)
    list6 = models.CharField(blank=True, null=True, max_length=100)
    list7 = models.CharField(blank=True, null=True, max_length=100)
    list8 = models.CharField(blank=True, null=True, max_length=100)
    list9 = models.CharField(blank=True, null=True, max_length=100)
    list10 = models.CharField(blank=True, null=True, max_length=100)
    list11 = models.CharField(blank=True, null=True, max_length=100)
    list12 = models.CharField(blank=True, null=True, max_length=100)
    year_start = models.DateField(blank=True, null=True)
    year_end = models.DateField(blank=True, null=True)
    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume"

    def __str__(self):
        return self.title



class About(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='Profile_images/')
    title = models.CharField(blank=True, null=True, max_length=100)
    body = models.TextField(blank=True, null=True, max_length=2000)
    point1 = models.CharField(blank=True, null=True, max_length=2000)
    point2 = models.CharField(blank=True, null=True, max_length=2000)
    point3 = models.CharField(blank=True, null=True, max_length=2000)
    point4 = models.CharField(blank=True, null=True, max_length=2000)
    point5 = models.CharField(blank=True, null=True, max_length=2000)
    point6 = models.CharField(blank=True, null=True, max_length=2000)
    point7 = models.CharField(blank=True, null=True, max_length=2000)
    point8 = models.CharField(blank=True, null=True, max_length=2000)
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Me"