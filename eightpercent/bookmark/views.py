from django.shortcuts import render
from django.views import View
from bookmark.models import Bookmark
from django.http import JsonResponse

# Create your views here.

class BookmarkView(View):
    def get(self,request):
        bookmark=Bookmark.objects.create(title= "Adfadf", asda="zcvx")
        return JsonResponse(data= {"id":bookmark.id})