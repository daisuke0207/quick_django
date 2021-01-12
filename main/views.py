from django.shortcuts import render
from django.http import HttpResponse

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