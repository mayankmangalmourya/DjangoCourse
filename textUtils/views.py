# this file made by harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    text = request.POST.get('text', 'default')
    trig_remove_punc = request.POST.get('removepunc', 'off')
    trig_capitalize_text = request.POST.get('capitalizeLetter', 'off')
    trig_remove_newLine = request.POST.get('removeNewLine', 'off')
    trig_sapce_remove = request.POST.get('spaceRemove', 'off')
    trig_count_char = request.POST.get('countChar', 'off')

    if (trig_remove_punc == 'on'):
        analyzed_txt = ""
        for char in text:
            if (char not in punctuations):
                analyzed_txt = analyzed_txt + char
        params = {'functioning': 'Remove Punctuations', 'analyzed_text': analyzed_txt}
        text = analyzed_txt

    if (trig_capitalize_text == 'on'):
        analyzed_txt = ""
        for char in text:
            analyzed_txt = analyzed_txt + char.upper()
        params = {'functioning': 'Capitalize Text', 'analyzed_text': analyzed_txt}
        text = analyzed_txt

    if (trig_remove_newLine == 'on'):
        analyzed_txt = ""
        for char in text:
            if char != '\n' and char != '\r':
                analyzed_txt = analyzed_txt + char
        params = {'functioning': 'Remove New Line', 'analyzed_text': analyzed_txt}
        text = analyzed_txt

    if (trig_sapce_remove == 'on'):
        analyzed_txt = ""
        for index, char in enumerate(text):
            if (text[index] == " " and text[index + 1] == " "):
                continue
            else:
                analyzed_txt = analyzed_txt + char
        params = {'functioning': 'Remove Extra Space', 'analyzed_text': analyzed_txt}
        text = analyzed_txt

    if (trig_count_char == 'on'):
        count = 0
        for char in text:
            count += 1
        params = {'functioning': 'Count Character', 'analyzed_text': count}
        text = count

    if (trig_remove_punc != 'on' and trig_sapce_remove != 'on' and trig_remove_newLine != 'on' and
            trig_capitalize_text != 'on' and trig_count_char != 'on'):
        return HttpResponse("Please Select Any Operation and Try Again !!!!")

    return render(request, 'analyze.html', params)
