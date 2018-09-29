from django.http import JsonResponse

def returnResponse(data={}, code=200, info=''):
    return JsonResponse({
        'code': code,
        'data': data,
        'info': info
    }, safe=False)