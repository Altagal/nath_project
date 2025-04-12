from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from home.util import render_html_to_pdf


@login_required
def index(request):
    context = {

    }
    return render(request, 'home/index.html', context)


@login_required
def page_404(request, exception):
    context = {

    }
    return render(request, 'home/404.html', context)


# FORMULARIO
@login_required
def to_pdf(request, template_name):
    context = {
        "var1": "teste string variavel 1",
    }
    return render_html_to_pdf(template_name, context, is_downloadable=False)
    # return render(request, 'pdf\\' + template_name + '.html', context)
