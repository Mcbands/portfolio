from django.contrib import admin
from .models import *
from .forms import *

class TotalBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'total')


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('title', 'percentage')


class MydetailsAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phone')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','filter',)

class CategoryTitleAdmin(admin.ModelAdmin):
    list_display = ('title','filter',)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title','name',)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('email',)

admin.site.register(Total, TotalBlogAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Mydetails, MydetailsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(CategoryTitle, CategoryTitleAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(About, AboutAdmin)
# admin.site.register(Contact, ContactAdmin)

