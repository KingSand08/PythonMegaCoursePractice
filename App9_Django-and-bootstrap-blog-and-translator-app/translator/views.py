from django.shortcuts import render
from . import translate

# Create your views here.
def translator_view(request): # In background url is passed as request when user visits the website
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        lang_selected = request.POST['language']
        output = translate.translate(original_text, lang_selected)
        return render(request, 'translator.html', {'original_text' : original_text, 'output_text' : output})
    else:
        return render(request, 'translator.html')
    