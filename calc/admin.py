from django.contrib import admin
from .models import Post
from .models import Details
from .models import Contact
# Register your models here.
admin.site.register(Post)
admin.site.register(Details)
admin.site.register(Contact)