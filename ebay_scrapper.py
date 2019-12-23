



import requests
from bs4 import BeautifulSoup
import csv


def get_page(url):

    response = requests.get(url)

    if not response.ok:
        print("Server responded: "+response.status_code)
    else:
        soup = BeautifulSoup(response.text,'lxml')
        return soup



def get_detailed_data(soup):
    try:
        h1 = soup.find('h1',id='itemTitle').text.split('about')[1].replace('\xa0','')
    except:
        h1 = ''

    try:
        try:
            p = soup.find('span',id='prcIsum').text
        except:
            p = soup.find('span',id='mm-saleDscPrc').text
        currency,price = p.split(' ')
    except:
        currency = ''
        price = ''


    try:
        sold_items= soup.find('div',id="why2buy").find('div',class_="w2b-cnt w2b-3 w2b-red").text.split(" ")[0].replace('\xa0','')
    except:
        sold_items = ''


    data = {
        'title':h1,
        'currency':currency,
        'price':price,
        'quantity sold':sold_items
    }

    return data


def get_index_data(soup):

    try:
        links = soup.find_all('a',class_="s-item__link")
    except:
        links = []


    urls = [item.get('href') for item in links]
    return urls

def write_csv(data,url):
    with open('scraped_data_of_watches_from_ebay.csv','a') as csvfile:
        writer = csv.writer(csvfile)
        row = [data['title'],data['currency'],data['price'],data['quantity sold'],url]
        writer.writerow(row)

def main():
    url = "https://www.ebay.com/sch/i.html?_nkw=watches&_pgn=2"
    products = get_index_data(get_page(url))

    for link in products:
        data = get_detailed_data(get_page(link))
        write_csv(data,link)
        #print (data)
    #url ="https://www.ebay.com/itm/Fashion-Men-LED-Digital-Date-Military-Sport-Rubber-Quartz-Watch-Alarm-Waterproof/401272383158?epid=14027539613&hash=item5d6db2a6b6:g:KFcAAOSwImRYmQ92"
    #collected_data = get_detailed_data(get_page(url))



if __name__ == '__main__':
    main()




