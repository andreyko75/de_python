from requests import get

response = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text
with open('ngnix_logs.txt', 'w', encoding='utf-8') as _:
    _.write(response)
result = []
with open('ngnix_logs.txt', 'r', encoding='utf-8') as _:
    for line in _:
        line_work = line.replace('"', '').split()
        result.append((line_work[0], line_work[5], line_work[6]))
print(result)
