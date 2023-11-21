def visitor_ip(view_request):
    x_forwarded_for = view_request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = view_request.META.get('REMOTE_ADDR')
    return ip
