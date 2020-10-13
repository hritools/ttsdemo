from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from core.tts_engine import tts as tts_proc


def index(rq):
    return render(rq, 'index.html')


@require_POST
@csrf_exempt
def tts(rq):
    text = rq.POST.get('text')
    if not text:
        return HttpResponse(status=400)
    try:
        url = tts_proc(text)
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
    return JsonResponse({'url': url}, safe=False)

