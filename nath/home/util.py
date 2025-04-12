from datetime import timedelta, date

import os
from django.conf import settings
from django.forms import TextInput
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def link_callback(uri, rel):
    if uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    elif uri.startswith(settings.STATIC_URL):
        path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ""))
    else:
        return uri

    # Ensure the file exists
    if not os.path.isfile(path):
        raise Exception(f"Path does not exist: {path}")

    return path


def render_html_to_pdf(template_name, context={}, is_downloadable=False, file_name="arquivo"):
    template_path = "core/pdf/"
    # encode_type = "utf-8"
    file_type = "pdf"
    response = HttpResponse(content_type='application/' + file_type)
    response['Content-Disposition'] = "filename=" + file_name + "." + file_type + ";"

    # if is_downloadable:
    #     response['Content-Disposition'] += " attachment;"

    template = get_template(template_path + template_name)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def criados_n_dias(model, n_dias):
    week_dates = []
    for day_week in (date.today() - timedelta(days=days) for days in range(n_dias, 0, -1)):
        qtd = model.objects.filter(created_at__date=day_week).count()
        week_dates.append({'created_at': day_week, 'qtd': qtd})
    return week_dates


def criados_ultima_semana(model):
    today = date.today()
    weekday = today.weekday()
    start_of_week = today - timedelta(days=weekday, weeks=1)

    week_dates = []
    for day in (start_of_week + timedelta(days=day - 1) for day in range(7)):
        qtd = model.objects.filter(created_at__date=day).count()
        week_dates.append({'created_at': day, 'qtd': qtd})
    return week_dates
