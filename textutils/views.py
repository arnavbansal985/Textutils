from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'arnav','city':'delhi'}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse("about page")

# def capfirst(request):
#     return HttpResponse("capfirst")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("removepunc")

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    extraspaces=request.POST.get('extraspaces','off')
    removenewline=request.POST.get('removenewline','off')
    capitalize=request.POST.get('capitalize','off')
    charcount=request.POST.get('charcount','off')
    print(removepunc)
    print(djtext)
    count=0
    if removepunc=='on':
        punctuations='''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
        analyzed=djtext
        for x in analyzed:
            if x in punctuations:
                analyzed=analyzed.replace(x,"")
        djtext=analyzed
        # params={'punct':'remove punctuations','analyzed_text':analyzed}
        # return render(request,'analyze.html',params)

    if extraspaces=='on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        djtext=analyzed
        # params = {'punct': 'remove extra spaces', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if removenewline=='on':
        analyzed = djtext
        # count_list = analyzed.split()
        # analyzed = " ".join(count_list)
        for i in analyzed:
             if i=="\n" or i=="\r":
                 analyzed=analyzed.replace(i,' ')
        djtext = analyzed
        # params = {'punct': 'remove extra spaces', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if capitalize=='on':
        analyzed=djtext
        for i in analyzed:
            j=i.capitalize()
            analyzed=analyzed.replace(i,j)
        djtext = analyzed
        # params = {'punct': 'capitalzie', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if charcount=='on':
        analyzed=djtext
        count_list=analyzed.split()
        count=len(count_list)
        # params = {'punct': 'remove new line', 'analyzed_text': count}
        # return render(request, 'analyze.html', params)

    if (removepunc!='on' and extraspaces!='on' and removenewline!='on' and capitalize!='on' and charcount!='on' ):
        return HttpResponse("<h1>Error</h1>")

    params={'analyzed_text':analyzed,'count':count}
    return render(request,'analyze.html',params)

