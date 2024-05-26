import os
import csv

def generate_urls(folder_path, base_url):
    urls = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            urls.append(base_url + filename)
    return urls

def write_to_csv(urls, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for url in urls:
            writer.writerow([url])

if __name__ == "__main__":
    base_url = "https://pic.my-nas8.top/imgs/random/"
    folder_path = "./imgs/random/"
    output_file = "url.csv"
    
    urls = generate_urls(folder_path, base_url)
    write_to_csv(urls, output_file)
    print("CSV success")
