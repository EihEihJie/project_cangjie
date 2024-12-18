from django.contrib import admin

# Register your models here.
from my_test_app.models import Book,Person
#注册模型类
admin.site.register(Book)
admin.site.register(Person)