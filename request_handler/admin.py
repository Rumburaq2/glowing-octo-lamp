from django.contrib import admin

# Register your models here.

from django.contrib import admin
# Register your models here.
from .models import items
from .models import loans
admin.site.register(items)
admin.site.register(loans)
