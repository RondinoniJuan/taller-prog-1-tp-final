from collections import Counter

with open('web-server-log.txt', 'r') as f:
    logs = f.readlines()

ips = []
pages = []
codes = []

for log in logs:
    parts = log.split()
    ips.append(parts[0])
    pages.append(parts[6])
    codes.append(parts[8])

ip_counts = Counter(ips)
print("Accesos por IP:")
for ip, count in ip_counts.items():
    print(f"{ip}: {count} veces")

page_counts = Counter(pages)
top_3_pages = page_counts.most_common(3)
print("\nLas 3 páginas más visitadas:")
for page, count in top_3_pages:
    print(f"{page}: {count} veces")

total_accesses = len(codes)
successful_accesses = codes.count('200')
percentage_successful = (successful_accesses / total_accesses) * 100
print(f"\nPorcentaje de accesos exitosos: {percentage_successful:.2f}%")