from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import PersonModelForm
from .forms import TriangleForm
from .models import Person


# Home task 6. Django: Hypotenuse calculator
def triangle(request):
    if request.method == "POST":
        triangle_form = TriangleForm(request.POST)
        if triangle_form.is_valid():
            leg1 = triangle_form.cleaned_data["first_leg"]
            leg2 = triangle_form.cleaned_data["second_leg"]
            hyp = round(((leg1 ** 2 + leg2 ** 2) ** 0.5), 3)
            return render(request, "triangle.html", context={"hyp": hyp})
    else:
        triangle_form = TriangleForm()
    return render(request, "triangle.html", context={"form": triangle_form})


# Home task 7. Create view for creating Person
def create_person(request):
    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Person successfully created!')
            return redirect(instance.get_absolute_url())
            # return redirect(reverse('update-person', args=(instance.pk,)))
        else:
            messages.error(request, 'Person not created!')
    else:
        form = PersonModelForm()
    return render(request, 'person_create.html', context={'form': form})


def update_person(request, pk):
    instance = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated successfully!')
            return redirect(reverse('update-person', args=[pk]))
    else:
        form = PersonModelForm(instance=instance)
    return render(request, 'person_update.html', context={'form': form, 'person_inst': instance})
