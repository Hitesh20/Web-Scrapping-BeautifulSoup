

'''
from bs4 import BeautifulSoup
import requests
with open('forms.html') as html_file:
    soup = BeautifulSoup(html_file , 'lxml')


#print(soup.prettify())

match = soup.title
print(match)

mat = soup.title.text
print(mat)

matc = soup.find('input')
print(matc)

ma = soup.find('input',type='submit')
print(ma)

print("----------------------")
for input_line in soup.find_all('h2'):
    pr = input_line.text
    print(pr)
    print()


'''


from bs4 import BeautifulSoup
import requests
import csv

def use_csv(dictionary):
    #for data in dictionary:

        with open('scraping.csv','a') as csv_file:
            csv_writer = csv.writer(csv_file)
            row=[dictionary['headline'],dictionary['summary'],dictionary['video_link']]
            csv_writer.writerow(row)
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())
#dict = {}
for article in soup.find_all('article'):
# print(article.prettify())
    heading = article.header.h2.a.text

    #print(heading)

    summary = article.find('div',class_='entry-content').p.text

    #print(summary)
    try:
        vid_src = article.find('iframe',class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4].split('?')[0]
    except Exception as e:
        yt_link = None
    #print(vid_id)

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    #print(yt_link)

    dictionary = {
        'Heading':heading,
               'Summary':summary,
        'Youtube Link':yt_link
    }
    use_csv(dictionary)




'''

from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.codechannels.com/channel/thenewboston/page/2/').text

soup = BeautifulSoup(source,'lxml')

#print(soup)

for article in soup.find_all('article'):

    heading = article.header.h2.text
    print(heading)
    print("-----------------")

    img_src = article.find('a',class_='post-image post-image-left')['href']
    print(img_src)
    print("---------------------------")
    print("--------------------------------")



'''



