from django.shortcuts import render

from .forms import TriangleForm


# Hometask 6. Django: Hypotenuse calculator
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
