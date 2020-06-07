from django.contrib import admin
from .models import Post #.models(같은 폴더에 있는..)
# Register your models here.
admin.site.register(Post)
"myapp/admin.py models.py -> myapp/models.py (=> .models)"