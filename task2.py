import re
from collections import Counter

# access_log.txt faylını oxumaq
with open("access_log.txt", "r") as file:
    log_content = file.read()

# URL-ləri və HTTP status kodlarını çıxarmaq üçün regex
pattern = re.compile(r'\"(?:GET|POST) (http[s]?://[^\s]+) HTTP/1\.[0-1]\" (\d{3})')
matches = pattern.findall(log_content)

# Yalnız 404 status kodu olan URL-ləri filtrləmək
urls_404 = [url for url, status in matches if status == '404']

# URL-lərin sayını hesablayın
url_404_counts = Counter(urls_404)

# Nəticələri çap edin
for url, count in url_404_counts.items():
    print(f"URL: {url} – Görünmə sayı: {count}")
