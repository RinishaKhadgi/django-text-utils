from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def analyze(request):
    text = request.POST.get('text')
    removepuncs = request.POST.get('removepuncs')
    removenumbers = request.POST.get('removenumbers')
    fullcaps = request.POST.get('fullcaps')
    charcount = request.POST.get('charcount')

    context = {
        'info': '',
        'purpose': [],
        'result': ''
    }

    if text == '':
        context['info'] = "Please don't pass an empty sentence!"

    else:
        if removepuncs:
            result = ''
            punctuations = '''!"#$%&'()*+,-./:;<=>?@[]^_`{|}~'''
            for char in text:
                if char not in punctuations:
                    result += char
            context['purpose'].append('Removed Punctuation')
            context['result'] = result
            context['info'] = 'Your text has been analyzed!'
            text = result

        if removenumbers:
            result = ''
            numbers = '0123456789'
            for char in text:
                if char not in numbers:
                    result += char
            context['purpose'].append('Removed Numbers')
            context['result'] = result
            context['info'] = 'Your text has been analyzed!'
            text = result

        if fullcaps:
            result = ''
            result = text.upper()
            context['purpose'].append('Changed to Uppercase')
            context['result'] = result
            context['info'] = 'Your text has been analyzed!'
            text = result

        if charcount:
            length = len(text)
            context['purpose'].append('Character Counted')
            context['result'] = f'{text} - {length} characters'
            context['info'] = 'Your text has been analyzed!'
        
        elif not(removepuncs or removenumbers or fullcaps or alllower or charcount):
            context['result'] = text
            context['info'] = 'No changes made to the text!'

    return render(request, 'analyze.html', context)
