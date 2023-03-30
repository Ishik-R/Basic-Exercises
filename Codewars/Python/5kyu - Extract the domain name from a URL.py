'''
5 kyu - Extract the domain name from a URL
https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
Python

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
'''

def domain_name(url):
    import re

    url_begining = re.compile('(http(s)?://)?(www.)?')
    m = url_begining.search(url)
    url = url[:m.start()] + url[m.end():]
    return url[:url.find('.')]

url = "http://github.com/carbonfive/raygun"
print(domain_name(url))