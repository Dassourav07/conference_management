def handle_uploaded_file(f):  
    with open('/static/media/paper/Candidate'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 