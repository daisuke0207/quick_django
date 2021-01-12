from django.shortcuts import render
from django.http import HttpResponse

# リクエスト情報を受け取る
def index(request):
    # レスポンスを生成する
    return HttpResponse('こんにちは、世界！')