from lxml import html
import requests

#easier to hard code, but if I add more than 3 than I'll use classes
#or if I do multiple links for each one 

gs_link = 'http://www.gamestop.com/nintendo-3ds/games/fire-emblem-fates-special-edition/126802'
amazon_link = 'http://www.amazon.com/Fire-Emblem-Fates-Special-Nintendo-3DS/dp/B017W16ZDK/ref=sr_1_1_twi_gam_1?ie=UTF8&qid=1451030490&sr=8-1&keywords=fire+emblem+special+edition'

page = requests.get(gs_link)
tree = html.fromstring(page.content)
status = tree.xpath('//div[@class="buttonna"]/a/span/text()')

if ('Not' in status[0]):
    print '\nOut of Stock at GS'
else:
    print '\nIn stock at GS!'
    
page = requests.get(amazon_link)
tree = html.fromstring(page.content)
status = tree.xpath('//span[@class ="a-size-medium a-color-price"]/text()')

if ('unavailable' in status[0]):
    print '\nOut of Stock at Amazon :('
else:
    print '\nIn stock at amazon!'
