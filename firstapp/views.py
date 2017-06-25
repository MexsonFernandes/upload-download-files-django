from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile, File
from django.conf import settings
import os
from django.http import HttpResponse
import csv
import codecs

# Create your views here.
#def index(request):
 #   return render(request, 'index.html')



def index(request):
    success = 0
    if success == 1:
        success = 2
    if request.POST and request.FILES:
        csvfile = request.FILES['csv_file']
        #form = UploadFileForm(request.POST, request.FILES)
        #dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
        path = default_storage.save('tmp/text.txt',ContentFile(csvfile.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        with open("tmp/text.txt", "r+b") as file:
            success = 1
            content = file.read()
            file.seek(0)
            file.write(content.upper())
        #reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)
    return render(request, "index.html", locals())


def download(request):
    path = "tmp/text.txt"
    success = 2
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise "Http404"