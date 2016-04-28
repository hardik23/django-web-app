from django.contrib import admin
from .models import my_works
# Register your models here.
from .forms import to_do_list

class to_do_admin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    form=to_do_list


admin.site.register(my_works,to_do_admin)



