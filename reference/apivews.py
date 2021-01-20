from rest_framework import viewsets


class AuthorViewSet(viewsets.ViewSet):

    model = Author
    serializer_class = AuthorSerializer