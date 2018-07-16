#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import urllib.request


url_changer = input('Enter the project name: ')


def project():
    if url_changer == 'HAHMI':
        link = 'https://saeljira.it.here.com/issues/?jql=project%20%3D%20HAHMI'
    elif url_changer == 'AEPREQ':
        link = 'https://saeljira.it.here.com/issues/?jql=project%20%3D%20AEPREQ'
    elif url_changer == 'AEPORT':
        link = 'https://saeljira.it.here.com/issues/?jql=project%20%3D%20AEPORT'
    else:
        print("We are not working with this project")
    return link


response = urllib.request.urlopen('{}'.format(project()))                        # Открываем линку из project()
reading_link = response.read()


def copy_to_file():
    f = open('/home/dkicha/temp.html', 'w')
    f.write(str(reading_link))
    f.close()


copy_to_file()

