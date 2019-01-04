from django.contrib import admin

# Register your models here.
from .models import Option,Pool,Vote

admin.site.register(Pool)
admin.site.register(Option)
admin.site.register(Vote)


