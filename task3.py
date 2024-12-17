import re

# access_log.txt faylını oxumaq
with open("access_log.txt", "r") as file:
    log_content = file.read()

# URL-ləri və HTTP status kodlarını çıxarmaq üçün regex
pattern = re.compile(r'\"(?:GET|POST) (http[s]?://[^\s]+) HTTP/1\.[0-1]\" (\d{3})')
matches = pattern.findall(log_content)

# Nəticələri fayla yazmaq
with open("url_status_report.txt", "w") as output_file:
    for url, status in matches:
        output_file.write(f"URL: {url} – Status: {status}\n")

print("URL-lər və status kodları 'url_status_report.txt' faylında saxlandı.")
