from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random

# リクエスト情報を受け取る
def index(request):
    # レスポンスを生成する
    return HttpResponse('こんにちは、世界！')

def temp(request):
  # ビュー変数を準備
  context = {
    'msg': 'こんにちは、世界！'
  }
  # テンプレートを呼び出す
  return render(request, 'main/temp.html', context)

def list(request):
    # すべての書籍情報を取得
    books = Book.objects.all()
    return render(request, 'main/list.html', {
        'books': books
    })

def iftag(request):
    return render(request, 'main/iftag.html', {
      # 0~100の乱数を生成
      'random': random.randint(0, 100)
    })

def yesno(request):
    return render(request, 'main/yesno.html', {
      'flag': True
    })

def firstof(request):
    return render(request, 'main/firstof.html', {
      # 'a': 'おはようございます！',
      'b': 'こんにちは！',
      # 'c': 'こんばんは！'
    })