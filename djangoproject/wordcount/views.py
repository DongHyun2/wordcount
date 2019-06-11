from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') #render 3개의 인자, (req, 템플릿이름, 선택적으로 사전형객체)

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext'] # 'fulltext'home 원문, 글 전체를 text라는 변수에 문자열로서 담는다.
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] =+ 1
        else:
            word_dictionary[word] = 1
    
    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary' : word_dictionary.items()}) # {'full': text}로 fulltext값을 찍어 보낸다.