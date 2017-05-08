from django.contrib import admin
from .models import Post

# Registering makes model visible on admin page.

admin.site.register(Post)
