from datetime import timedelta, date

import os
from django.conf import settings
from django.forms import TextInput
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

import webbrowser
from datetime import datetime
import json
import os
import msal


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


def render_html_to_pdf(
    template_name, context={}, is_downloadable=False, file_name="arquivo"
):
    template_path = "core/pdf/"
    # encode_type = "utf-8"
    file_type = "pdf"
    response = HttpResponse(content_type="application/" + file_type)
    response["Content-Disposition"] = "filename=" + file_name + "." + file_type + ";"

    # if is_downloadable:
    #     response['Content-Disposition'] += " attachment;"

    template = get_template(template_path + template_name)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


def criados_n_dias(model, n_dias):
    week_dates = []
    for day_week in (
        date.today() - timedelta(days=days) for days in range(n_dias, 0, -1)
    ):
        qtd = model.objects.filter(created_at__date=day_week).count()
        week_dates.append({"created_at": day_week, "qtd": qtd})
    return week_dates


def criados_ultima_semana(model):
    today = date.today()
    weekday = today.weekday()
    start_of_week = today - timedelta(days=weekday, weeks=1)

    week_dates = []
    for day in (start_of_week + timedelta(days=day - 1) for day in range(7)):
        qtd = model.objects.filter(created_at__date=day).count()
        week_dates.append({"created_at": day, "qtd": qtd})
    return week_dates

# Microsoft Graph API Methods and Configurations

def generate_access_token(app_id, scopes):
    # Save Session Token as a token file
    access_token_cache = msal.SerializableTokenCache()
    print(access_token_cache)

    # read the token file
    if os.path.exists('ms_graph_api_token.json'):
        access_token_cache.deserialize(open("ms_graph_api_token.json", "r").read())
        token_detail = json.load(open('ms_graph_api_token.json',))
        token_detail_key = list(token_detail['AccessToken'].keys())[0]
        token_expiration = datetime.fromtimestamp(int(token_detail['AccessToken'][token_detail_key]['expires_on']))
        if datetime.now() > token_expiration:
            os.remove('ms_graph_api_token.json')
            access_token_cache = msal.SerializableTokenCache()

    # assign a SerializableTokenCache object to the client instance
    client = msal.PublicClientApplication(client_id=app_id, token_cache=access_token_cache)

    accounts = client.get_accounts()
    if accounts:
        # load the session
        token_response = client.acquire_token_silent(scopes, accounts[0])
    else:
        # authetnicate your accoutn as usual
        flow = client.initiate_device_flow(scopes=scopes)
        print('user_code: ' + flow['user_code'])
        webbrowser.open('https://microsoft.com/devicelogin')
        token_response = client.acquire_token_by_device_flow(flow)

    with open('ms_graph_api_token.json', 'w') as _f:
        _f.write(access_token_cache.serialize())

    return token_response


