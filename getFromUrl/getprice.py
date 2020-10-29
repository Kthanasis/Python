import bs4, requests

def getPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#prcIsum') #rigth click->copy selector
    return elems[0].text.strip()

    
price = getPrice('https://www.ebay.com/itm/313264789944?ul_noapp=true') #product url
print('The price is ' + price)
