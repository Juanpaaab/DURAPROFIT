from Proceso import HashrateTotal
from bs4 import BeautifulSoup
import urllib.request
import json
import requests

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


url2 = 'https://whattomine.com/coins.json?eth=true&factor%5Beth_hr%5D=500.0&factor%5Beth_p%5D=200.0&e4g=true&factor%5Be4g_hr%5D=0.0&factor%5Be4g_p%5D=0.0&zh=true&factor%5Bzh_hr%5D=0.0&factor%5Bzh_p%5D=0.0&cnh=true&factor%5Bcnh_hr%5D=0.0&factor%5Bcnh_p%5D=0.0&cng=true&factor%5Bcng_hr%5D=0.0&factor%5Bcng_p%5D=0.0&cnr=true&factor%5Bcnr_hr%5D=0.0&factor%5Bcnr_p%5D=0.0&cnf=true&factor%5Bcnf_hr%5D=0.0&factor%5Bcnf_p%5D=0.0&eqa=true&factor%5Beqa_hr%5D=0.0&factor%5Beqa_p%5D=0.0&cc=true&factor%5Bcc_hr%5D=0.0&factor%5Bcc_p%5D=0.0&cr29=true&factor%5Bcr29_hr%5D=0.0&factor%5Bcr29_p%5D=0.0&ct31=true&factor%5Bct31_hr%5D=0.0&factor%5Bct31_p%5D=0.0&ct32=true&factor%5Bct32_hr%5D=0.0&factor%5Bct32_p%5D=0.0&eqb=true&factor%5Beqb_hr%5D=0.0&factor%5Beqb_p%5D=0.0&rmx=true&factor%5Brmx_hr%5D=0.0&factor%5Brmx_p%5D=0.0&ns=true&factor%5Bns_hr%5D=0.0&factor%5Bns_p%5D=0.0&al=true&factor%5Bal_hr%5D=0.0&factor%5Bal_p%5D=0.0&ops=true&factor%5Bops_hr%5D=0.0&factor%5Bops_p%5D=0.0&eqz=true&factor%5Beqz_hr%5D=0.0&factor%5Beqz_p%5D=0.0&zlh=true&factor%5Bzlh_hr%5D=0.0&factor%5Bzlh_p%5D=0.0&kpw=true&factor%5Bkpw_hr%5D=0.0&factor%5Bkpw_p%5D=0.0&ppw=true&factor%5Bppw_hr%5D=0.0&factor%5Bppw_p%5D=0.0&x25x=true&factor%5Bx25x_hr%5D=0.0&factor%5Bx25x_p%5D=0.0&mtp=true&factor%5Bmtp_hr%5D=0.0&factor%5Bmtp_p%5D=0.0&vh=true&factor%5Bvh_hr%5D=0.0&factor%5Bvh_p%5D=0.0&factor%5Bcost%5D=0.08&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main'
Respuesta2 = requests.get(url2)

RespuestaJson = Respuesta2.json()

print(RespuestaJson["coins"]["Ethereum"]["block_time"])
print(RespuestaJson["coins"]["Ethereum"]["block_reward"])
print(RespuestaJson["coins"]["Ethereum"]["nethash"] / 1e+9)


