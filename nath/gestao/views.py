from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gestao.models import Laboratorio
from gestao.forms import LaboratorioForm


# Laboratorio
@login_required
def laboratorio_list(request):
    pre_context = {
        "card_title": "Laboratórios",
    }

    context = {
        "laboratorio_list": Laboratorio.objects.all(),
    }
    return render(
        request, "gestao/laboratorio_list.html", {**pre_context, **context}
    )


@login_required
def laboratorio_create(request):

    pre_context = {
        "card_title": "Laboratorio",
    }

    if request.method == "GET":
        context = {
            "form": LaboratorioForm(),
        }

    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.custom_save(request)
            return redirect("laboratorio_list")
        else:
            context = {
                "form": form,
            }

    return render(request, "gestao/laboratorio.html", {**pre_context, **context})
