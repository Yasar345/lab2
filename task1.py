import re

# access_log.txt faylını oxumaq
with open("access_log.txt", "r") as file:
    log_content = file.read()

# URL-ləri və HTTP status kodlarını çıxarmaq üçün regex
pattern = re.compile(r'\"(?:GET|POST) (http[s]?://[^\s]+) HTTP/1\.[0-1]\" (\d{3})')

# Tapılan uyğunluqları çıxarmaq
matches = pattern.findall(log_content)

# Nəticələri çap etmək
for url, status in matches:
    print(f"URL: {url} – Status: {status}")
