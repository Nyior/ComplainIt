from django.contrib import admin
from .models import (Post, 
                     MinedData, 
                     State, 
                     Lga, 
                     Agencies, 
                     Category, 
                     Status,
                      Complain
)

# Register your models here.
admin.site.register(Post)
admin.site.register(MinedData)
admin.site.register(State)
admin.site.register(Lga)
admin.site.register(Agencies)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Complain)
