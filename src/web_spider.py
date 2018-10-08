from urllib import request

response = request.urlopen("http://www.iciba.com/proprietary")
content = response.read().decode('utf-8')
print(content)
