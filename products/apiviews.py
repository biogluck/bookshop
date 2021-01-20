from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import viewsets


from .models import Book
from reference.models import Author
from .serializers import BookSerializer, AuthorSerializer

# excel
from rest_framework.decorators import action
import json
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import csv
from docxtpl import DocxTemplate
from io import BytesIO, StringIO
import os


class BookAPIList(RetrieveAPIView):
    # authentication_classes = None
    # permission_classes = None
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookSetAPIList(viewsets.ModelViewSet):
    # authentication_classes = None
    # permission_classes = None
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorAPIList(viewsets.ModelViewSet):
    # authentication_classes = None
    # permission_classes = None
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(detail=False)
    def get_csv(self, request):
        serializer = self.get_serializer(self.queryset, many=True)
        data = json.loads(JSONRenderer().render(serializer.data))

        response = HttpResponse(content_type="text/csv")
        response.charset = 'utf-8'
        response['Content-Disposition'] = 'attachment;file=authors.csv'
        header = ('id', 'nm', 'shrt_nm')
        writer = csv.writer(response, delimiter=';')
        writer.writerow(header)
        for key in data:
            writer.writerow(
                key['pk'],
                key['name'],
                key['short_name'],
            )
        # content = response.content
        # ucontent = content.decode('utf-8').encode('cp1251)'
        return response

    @action(detail=False)
    def get_docx(self, request):
        context = {'key': 'value'}
        template_path = "template.docx"
        print(os.getcwd())
        doc = DocxTemplate(template_path)
        doc.render(context)
        temp_file = BytesIO()
        doc.save(temp_file)
        response = HttpResponse(
            temp_file.getvalue(), 
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        filename = "parsed.docx"
        content = "attachment; filename='{}'".format(filename)
        response['Content-Disposition'] = 'attachment'
        return response

    @action(detail=False)
    def s(self, request):
        s = request.GET.get('s')
        queryset = Author.objects.filter(name__icontains=s)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
