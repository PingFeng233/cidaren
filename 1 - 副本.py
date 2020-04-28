import json
import time
import os
import pyperclip#调用pyperclip模块
while True:
    f = open('c:\\cdr\\responseBody.txt', 'r', encoding='utf-8')
    j = json.load(f)
    #print(j['data']['options'])
    if 'options' in j['data']:
        lenth=len(j['data']['options'])
        for i in range(0,lenth):
            # print(j['data']['options'][i]['answer'])
            answer = str(j['data']['options'][i]['answer'])
            if answer == 'True':
                print(j['data']['options'][i]['content'])
    if 'options' in j['data']:
        lenth=len(j['data']['options'])
        for i in range(0,lenth):
            answer3 = str(j['data']['topic_mode'])
            if answer3 == '32':
                print(j['data']['answer_content']['answer_str'])
     if 'options' in j['data']:
        lenth=len(j['data']['options'])
        for i in range(0,lenth):
            answer4 = str(j['data']['topic_mode'])
            if answer4 == '43':
                print(j['data']['answer_content']['answer_str'])


    if 'answer_content' in j['data']:
        if 'stem' in j['data']:
            answer2 = str(j['data']['topic_mode'])
            if answer2 == '51':
                print(j['data']['answer_content'])
                pyperclip.copy(j['data']['answer_content'])#复制答案到剪贴板
    time.sleep(0.1)
    i = os.system('cls')