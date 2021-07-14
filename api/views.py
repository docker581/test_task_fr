from django.shortcuts import render, HttpResponse


def index(request):
    if not request.session.session_key:
        request.session.save()
    session_key = request.session.session_key # getting session_key
    session_id = int.from_bytes(
        session_key.encode('utf-8'), byteorder='big',
    ) # encoding
    new_key = int.to_bytes(
        session_id, length=len(session_key), byteorder='big',
    ).decode('utf-8') # decoding
    print(session_key, new_key)
    return HttpResponse(new_key) 
