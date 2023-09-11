from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def removepunc(request):
    textdata=request.POST.get('text','default')
    removepunch=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('NewLineRemover','off')
    extraspace=request.POST.get('Extraspaceremov','off')
    CharCount=request.POST.get('CharCount','off')

    if removepunch == 'on':
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for text in textdata:
            if text not in punctuations:
                analyzed+=text
        textdata=analyzed
        params={'purpose':'Removed Punctuation','analyzed':analyzed}

    if fullcaps == 'on':
        analyzed=""
        for char in textdata:
            analyzed+=char.upper()
        textdata=analyzed
        params={'purpose':'Changed to Uppercase','analyzed':analyzed}

    if newline == 'on':
        analyzed=""
        for char in textdata:
            if char != '\n' and char != '\r':
                analyzed+=char
        textdata=analyzed
        params={'purpose':'Removed New Lines','analyzed':analyzed}

    if extraspace == 'on':
        analyzed=""
        for index,char in enumerate(textdata):
            if not (textdata[index] ==" " and textdata[index+1]== " "):
                analyzed+=char
        textdata=analyzed
        params = {'purpose': 'Removed Extra Space', 'analyzed': analyzed}

    if CharCount == 'on':
        analyzed=0
        for char in textdata:
            if char.isalpha():
                analyzed+=1
        textdata=analyzed
        params = {'purpose': 'Character Counter', 'analyzed': 'Total count of char is '+str(analyzed)}

    if removepunch != 'on' and CharCount !='on' and extraspace != 'on' and newline != 'on' and fullcaps != 'on':
        return render(request,'error.html')

    return render(request,'removepunc.html',params)
def Search(request):
    data=request.GET.get('SearchResult','default')
    print(data)
    if data.lower() == 'HOME'.lower():
        return render(request,'index.html')
    elif data.lower() == 'About Us'.lower():
        return render(request,'about.html')
    elif data.lower() == 'Contact Us'.lower():
        return render(request,'contact.html')
    else:
        return render(request,'error.html')
def AboutUs(request):
    return render(request,'about.html')
def ContactUs(request):
    return render(request,'contact.html')
