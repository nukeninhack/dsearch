#!/usr/bin/python3
#-*-coding: utf-8-*-
# desenvolvido por major
# felipe silva: github.com/felipefs01
#######
import requests
print("=== DSearch codado por Nukenin ===")
url = str(input("Alvo>"))
ext = str(input("Extenção>"))
word = str(input("Wordlist>"))
with open(word, "r") as rw:
    with open("DSearch_log.txt", "w") as wwd:
        for out in rw.readlines():
            # ler diretórios
            x = url + "/" + out.rstrip("\n")
            getd = requests.get(x)
            code = getd.status_code
            if code == 200:
                print("{} -> {}".format(getd.status_code, x))
                okd = "{} -> {}".format(getd.status_code, x)
                # ler arquivos
                y = x + "." + ext
                getf = requests.get(y)
                print("{} -> {}".format(getf.status_code, y))
                okf = "{} -> {}".format(getf.status_code, y)
                # salva em log
                # dir
                wwd.write(okd)
                wwd.write("\n")
                # file
                wwd.write(okf)
                wwd.write("\n")
            else:
                print("{} not found".format(x))
                print("{} not found".format(y))
print("Scan completo!")