#!/usr/bin/python
#-*- coding: utf-8 -*-
#Developer by Bafomet
import os
import random
import shodan
import time
import sys
#set color
os.system("printf '\033]2;OSINT SAN 3.5\a'")
os.system('clear')
WHSL = '\033[1;32m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[1;34m'
banner1 = '''{1} 
 {1}{0}[{2} Official channel {0}tg {1}@osint_san_framework {1}{0}]                {0}[{2} GitHub {1}https://github.com/Bafomet666 {1}{0}]
 
                                    $$$$$$$\                  $$\        $$$$$$\  $$\                      $$\     
                                    $$  __$$\                 $$ |      $$  __$$\ $$ |                     $$ |    
                                    $$ |  $$ | $$$$$$\   $$$$$$$ |      $$ /  $$ |$$ | $$$$$$\   $$$$$$\ $$$$$$\   
                                    $$$$$$$  |$$  __$$\ $$  __$$ |      $$$$$$$$ |$$ |$$  __$$\ $$  __$$\ _$$  _|  
                                    $$  __$$< $$$$$$$$ |$$ /  $$ |      $$  __$$ |$$ |$$$$$$$$ |$$ |  \__| $$ |    
                                    $$ |  $$ |$$   ____|$$ |  $$ |      $$ |  $$ |$$ |$$   ____|$$ |       $$ |$$\ 
                                    $$ |  $$ |\$$$$$$$\ \$$$$$$$ |      $$ |  $$ |$$ |\$$$$$$$\ $$ |       \$$$$  |
                                    \__|  \__| \_______| \_______|      \__|  \__|\__| \_______|\__|        \____/ 

 {2}Framework :{2}{0} OSINT SAN.{0}
  '''.format(GNSL, REDL, WHSL)
choi = (banner1,)
print (random.choice(choi))
time.sleep(0.5)


data = input(REDL + " [ + ] " + WHSL + " Вы хотите сохранить результат в файле? yes / no :").strip()
print("")
l0g = ("")

def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(data)
    file.close()

if data.startswith("y" or "Y"):
    l0g = input(REDL + " [ + ] " + WHSL + " Дайте название файлу :")
    print("")
    print(REDL +" Данные будут сохранены по пути: OSINT-SAN /module/ Название файла")
    print("")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print("")
    print (REDL + " [ + ] " + WHSL + " Ок скипнул да ! потом не пизди что не сохранил !!! ")
    print("")
    

def showdam():
    if os.path.exists("./api.txt") and os.path.getsize("./api.txt") > 0:
        with open("api.txt", "r") as file:
            shodan_api_key = file.readline().rstrip("\n")
    else:
        file = open("api.txt", "w")
        os.system("stty -echo")
        shodan_api_key = input(REDL + " [ + ] " + WHSL + " Ваш ключ не валидный. Введите другой :")
        print("")
        os.system("stty echo")
        file.write(shodan_api_key)
        print ("\n [~] \033[34mFile written: ./api.txt \033[0m")
        file.close()

    api = shodan.Shodan(shodan_api_key)
    time.sleep(0.4)

    limit = 500  # Just a number
    counter = 1

    try:
        print (REDL + " [ + ] " + WHSL + " Проверка вашего ключа shodan :")
        api.search("b00m")
        print("")
        print (REDL + " [ + ] " + WHSL + " Успешно авторизован.. ")
        print("")
        time.sleep(0.5)
        b00m = input(REDL + " [ + ] " + WHSL + " Введите ключевой запрос поиска :")
        print("")
        counter = counter + 1
        for banner in api.search_cursor(b00m):
            print (REDL + " [ + ] " + WHSL + " IP: " + (banner["ip_str"]))
            print (REDL + " [ + ] " + WHSL + " Порт: " + str(banner["port"]))
            print (REDL + " [ + ] " + WHSL + " Организация: " + str(banner["org"]))
            print (REDL + " [ + ] " + WHSL + " Локация: " + str(banner["location"]))
            print (REDL + " [ + ] " + WHSL + " Layer: " + (banner["transport"]))
            print (REDL + " [ + ] " + WHSL + " Layer: " + (banner["transport"]))
            print (REDL + " [ + ] " + WHSL + " Domains: " + str(banner["domains"]))
            print (REDL + " [ + ] " + WHSL + " Hostnames: " + str(banner["hostnames"]))
            print (REDL + " [ + ] " + WHSL + " Информация о баннере для службы: " + (banner["data"]))
            print (REDL + " [ + ] " + WHSL + " Результат: %s. Search query: %s" % (str(counter), str(b00m)))

            data = ("\nIP: " + banner["ip_str"]) + ("\nPort: " + str(banner["port"])) + ("\nOrganisation: " + str(banner["org"])) + ("\nLocation: " + str(banner["location"])) + ("\nLayer: " + banner["transport"]) + ("\nDomains: " + str(banner["domains"])) + ("\nHostnames: " + str(banner["hostnames"])) + ("\nData\n" + banner["data"])
            logger(data)
            time.sleep(0.1)
            print ("\n" + "  " + "»" * 78 + "\n")

            counter += 1
            if counter >= limit:
                exit()

    except KeyboardInterrupt:
            print ("\n")
            print (REDL + " [ + ] " + WHSL + " Приятно было иметь с вами дело сэр...")
            time.sleep(0.5)
            os.system("cd ..;python3 osintsan.py")

    except shodan.APIError as oeps:
            print (" [✘] \033[1;31mError: %s \033[0m" % (oeps))
            sha_api = input(REDL + " [ + ] " + WHSL + "Хотите поменять API-ключ? <Y/N>: ").lower()
            if sha_api.startswith("y" or "Y"):
                file = open("api.txt", "w")
                os.system("stty -echo")
                shodan_api_key = input(REDL + " [ + ] " + WHSL + " Чувак... У тебя ключ не валидный. ")
                os.system("stty echo")
                file.write(shodan_api_key)
                print ("\n[~] \033[34mFile written: ./api.txt\033[0m")
                file.close()
                print ("[~] \033[34mRestarting the Platform, Please wait...\033[0m \n")
                time.sleep(1)
                showdam()
            else:
                print ("")
                sys.exit()

# =====# Main #===== #
#bafomet
if __name__ == "__main__":
    showdam()