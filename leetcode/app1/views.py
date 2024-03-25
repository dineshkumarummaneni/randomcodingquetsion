
from django.shortcuts import render

# Create your views here.
import requests

import random
def show(request):
    link='https://alfa-leetcode-api.onrender.com/problems?limit=3000'
    # link1='https://alfa-leetcode-api.onrender.com/problems?limit=50'
    # link='https://leetcode.com/api/problems/all/'
    response=requests.get(link)
    print(response)
    if response.status_code==200:

        data=response.json()
        # print(len(data['stat_status_pairs']))
        ran = random.randint(1, data['totalQuestions'])
        title=data['problemsetQuestionList'][ran]['title']
        print(len(data['problemsetQuestionList']))
        total=data['totalQuestions']
        print(total)
        problems=[]

        print(ran)
        link2=r'https://leetcode.com/problems/'
        problem=link2+title.replace(' ','-')
        print(problem)
    else:
        print('hii')
    return render(request,'main.html')
