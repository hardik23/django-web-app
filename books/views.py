from django.shortcuts import render_to_response,render
from django.db.models import Q
from books.models import my_works
from .forms import to_do_list


# Create your views here.


def to_do(request):
    form=to_do_list(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
    boo_data = my_works.objects.all()

    return render(request,"home.html",{'form':form,'list':boo_data})


