from bs4 import BeautifulSoup
import requests
import json

url = "https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
my_dict = {}

all_titles = soup.find_all(name='li', class_='css-32630i emt9r7s3')
data_node_ids = ["10", "16", "21", "26", "30", "35", "40"]

for index, title in enumerate(all_titles):
    title_text = title.find('a', class_='emt9r7s2 css-1mp8e4k e1c1bym14').text
    my_dict[title_text] = []
    ul_tag = soup.find('ul', attrs={"data-node-id": data_node_ids[index]})
    
    if ul_tag:
        for li in ul_tag.find_all('li'):
            pickup_line = li.text.strip()
            my_dict[title_text].append(pickup_line)

print("\nDictionary of Pickup Lines:")
for title, lines in my_dict.items():
    print(f"\nTitle: {title}")
    for line in lines:
        print(f"    • {line}")
        

json_filename = "manuthBTB.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(my_dict, json_file, ensure_ascii=False, indent=4)

