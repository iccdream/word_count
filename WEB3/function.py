from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)
    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] +=1
    sorted_dict = sorted(word_dict.items(),key = lambda w: w[1],reverse=True) #word_dict是（你,5）,w[1],就是代表按数字排序
    return render(request, 'count.html',{'count':total_count,'worddict':word_dict,'sorted':sorted_dict})