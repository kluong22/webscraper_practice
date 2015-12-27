#easier to hard code, but if I add more than 3 than I'll use classes
#or if I do multiple links for each one 
from lxml import html
import requests
import smtplib
from time import sleep


from_addr = xxx
from_pass = xxx
to_addr = xxx

def main():
    gs_link = 'http://www.gamestop.com/nintendo-3ds/games/fire-emblem-fates-special-edition/126802'
    amazon_link = 'http://www.amazon.com/Fire-Emblem-Fates-Special-Nintendo-3DS/dp/B017W16ZDK/ref=sr_1_1_twi_gam_1?ie=UTF8&qid=1451030490&sr=8-1&keywords=fire+emblem+special+edition'
    found = False
    count = 0
    #for 31 days, since the game comes out in Feb
    month_in_hours = 744
    while (found == False and count < month_in_hours):
        page = requests.get(gs_link)
        tree = html.fromstring(page.content)
        status = tree.xpath('//div[@class="buttonna"]/a/span/text()')

        if ('Not' in status[0]):
            print '\nOut of Stock at GS'
        else:
            send_mail(from_addr, from_pass, to_addr, 'Gamestop')
            found = True
        
        page = requests.get(amazon_link)
        tree = html.fromstring(page.content)
        status = tree.xpath('//span[@class ="a-size-medium a-color-price"]/text()')

        if ('unavailable' in status[0]):
            print '\nOut of Stock at Amazon :('
        else:
            sendmail(from_adr, from_pass, to_addr, 'Amazon')
            found = True
        if not (found):
            sleep(3600)
            count++
def send_mail(from_addr, from_pass, to_addr, store):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.login(from_addr,from_pass)
    msg = '\nThe item you are looking for is available at %s' %store
    server.sendmail(from_addr,to_addr,msg)

if __name__ == '__main__':
    main()