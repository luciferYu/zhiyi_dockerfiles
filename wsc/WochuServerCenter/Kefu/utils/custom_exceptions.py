from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status'] = 'fail'
        response.data['code'] = response.status_code
        response.data['message'] = response.data['detail']  # 增加message这个key
        del response.data['detail']  # 删掉原来的detail
        response.status_code = 200

    return response
