from django.shortcuts import render, redirect
from .forms import OnlineFoodForm
from .models import OnlineFood


def food_view(request):
    template_name = "curd_app/food_info.html"
    form = OnlineFoodForm()
    if request.method == "POST":
        form = OnlineFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show_info.html"
    order = OnlineFood.objects.all()
    context = {"order": order}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = OnlineFood.objects.get(id=pk)
    form = OnlineFoodForm(instance=obj)
    if request.method == "POST":
        form = OnlineFoodForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = 'curd_app/food_info.html'
    context = {'form': form}
    return render(request, template_name, context)


def cancel_view(request,  pk):
    obj = OnlineFood.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, 'curd_app/confirm.html')
