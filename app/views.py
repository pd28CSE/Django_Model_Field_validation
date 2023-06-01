from django.shortcuts import render

# Create your views here.

from . models import UserFile

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    elif request.method == 'POST':
        file = request.FILES.get('file')
        title = request.POST.get('title')

        userFile = UserFile(name=title, file=file)

        try:
            userFile.full_clean()
        except Exception as e:
            print(e)
        else:
            print('Success')
            userFile.save()
        return render(request, 'index.html')
        

