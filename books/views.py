from django.shortcuts import render
from .models import Books
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.views import Response

def books(request):
    context = {
        'books' : Books.objects.all()
    }
    return render(request, 'dist/index.html', context)

class GetBooksAPI(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Books.objects.all()
    # def get(self,request):
    #     return Response({'test':'pass'})

    