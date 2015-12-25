from lxml import html
import requests
from time import sleep

web_link = 'http://www.gamestop.com/nintendo-3ds/games/fire-emblem-fates-special-edition/126802'

page = requests.get(web_link)
tree = html.fromstring(page.content)

status = tree.xpath('//div[@class="buttonna"]/a/span/text()')

if ('Not' in status[0]):
    print '\nnope :('
else:
    print '\nwoo!'