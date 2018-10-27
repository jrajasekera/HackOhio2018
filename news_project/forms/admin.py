from django.contrib import admin
from .models import Source
from .models import Sort
from .models import Category
from .models import Language
from .models import Country

#Register models here

admin.site.register(Source)

admin.site.register(Sort)

admin.site.register(Category)

admin.site.register(Language)

admin.site.register(Country)
