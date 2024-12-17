import re
import csv
from collections import Counter

# Fayl yolları
log_file_path = "access_log.txt"
output_csv_path = "malware_candidates.csv"

# Log faylından məlumat çıxarmaq üçün regex pattern
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\w+) (?P<url>https?://[^\s"]+) HTTP/1.[01]" '
    r'(?P<status_code>404) (?P<error_code>\d+)'
)

def extract_404_urls(file_path):
    """Log faylından 404 xətası olan URL-ləri çıxarır."""
    urls = []
    with open(file_path, "r") as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                urls.append(match.group("url"))
    return urls

def save_to_csv(urls, output_path):
    """404 xətası olan URL-ləri və onların sayını CSV faylında saxlayır."""
    # URL-lərin sayını hesablayır
    url_counts = Counter(urls)

    # CSV faylına yazmaq
    with open(output_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["URL", "404 Count"])  # Başlıq sütunları
        for url, count in url_counts.items():
            writer.writerow([url, count])

# 404 xətası olan URL-ləri çıxarmaq
urls_with_404 = extract_404_urls(log_file_path)

# Nəticələri CSV faylına yazmaq
save_to_csv(urls_with_404, output_csv_path)

print(f"404 xətası olan URL-lər '{output_csv_path}' faylına yazıldı.")
