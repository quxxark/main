#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
from jira import JIRA


options = {'server': 'https://adc.luxoft.com'}
username = input('Enter your login: ')
password = input('Enter your password: ')


jira = JIRA(options)
authed_jira = JIRA(basic_auth=(username, password))
issue = jira.issue('HAHMI-1662')
print(issue)

