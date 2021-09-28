from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Family_member)
admin.site.register(Notice)
admin.site.register(Event)
admin.site.register(Complain)