#-*- coding: utf-8 -*-
#Developer by Bafomet
import requests
import webbrowser
def reverseimagesearch(img):
    try:
        surl='https://www.google.co.in/searchbyimage/upload'
        murl={'encoded_image': (img, open(img, 'rb')), 'image_content': ''}
        response = requests.post(surl, files=murl, allow_redirects=False)
        fetchUrl = response.headers['Location']
        openWeb = input(" Я открою браузер ? Мне тебе результаты нужно показать (Y/N) : ")
        if openWeb.upper() == 'Y':
            webbrowser.open(fetchUrl)
        else:
            pass
    except IOError:
        print()
        print("ERROR : File Does not Exist\n")
