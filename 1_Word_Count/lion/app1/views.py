from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.POST['text']
    text_count = len(text)
    words = text.replace(".", "").split()
    word_count = len(words)
    without_space = len(text.replace("",""))
    sentences = text.split('.') 
    sen_count = len(sentences) - 1
    word_dict = {}

    for word in words:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    context = {
        "count": text_count,
        "word_count" : word_count,
        "without_space" : without_space,
        "sen_count" : sen_count,
        "word_dict" : word_dict.items()
    }

    return render(request, 'result.html', context)