from Interfaz1 import *
from Interfaz2 import *
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys
import requests
import urllib.request
import pandas as pd
import requests.exceptions
import json

# python -m PyQt5.uic.pyuic Interfaz1.ui -o Interfaz1.py -x
Codigo = 0
HashrateTotal = 0
WattsTotal = 0
Algo = ""
url1 = 'https://whattomine.com/gpus'
url2 = 'https://whattomine.com/coins.json?eth=true&factor%5Beth_hr%5D=500.0&factor%5Beth_p%5D=200.0&e4g=true&factor%5Be4g_hr%5D=0.0&factor%5Be4g_p%5D=0.0&zh=true&factor%5Bzh_hr%5D=0.0&factor%5Bzh_p%5D=0.0&cnh=true&factor%5Bcnh_hr%5D=0.0&factor%5Bcnh_p%5D=0.0&cng=true&factor%5Bcng_hr%5D=0.0&factor%5Bcng_p%5D=0.0&cnr=true&factor%5Bcnr_hr%5D=0.0&factor%5Bcnr_p%5D=0.0&cnf=true&factor%5Bcnf_hr%5D=0.0&factor%5Bcnf_p%5D=0.0&eqa=true&factor%5Beqa_hr%5D=0.0&factor%5Beqa_p%5D=0.0&cc=true&factor%5Bcc_hr%5D=0.0&factor%5Bcc_p%5D=0.0&cr29=true&factor%5Bcr29_hr%5D=0.0&factor%5Bcr29_p%5D=0.0&ct31=true&factor%5Bct31_hr%5D=0.0&factor%5Bct31_p%5D=0.0&ct32=true&factor%5Bct32_hr%5D=0.0&factor%5Bct32_p%5D=0.0&eqb=true&factor%5Beqb_hr%5D=0.0&factor%5Beqb_p%5D=0.0&rmx=true&factor%5Brmx_hr%5D=0.0&factor%5Brmx_p%5D=0.0&ns=true&factor%5Bns_hr%5D=0.0&factor%5Bns_p%5D=0.0&al=true&factor%5Bal_hr%5D=0.0&factor%5Bal_p%5D=0.0&ops=true&factor%5Bops_hr%5D=0.0&factor%5Bops_p%5D=0.0&eqz=true&factor%5Beqz_hr%5D=0.0&factor%5Beqz_p%5D=0.0&zlh=true&factor%5Bzlh_hr%5D=0.0&factor%5Bzlh_p%5D=0.0&kpw=true&factor%5Bkpw_hr%5D=0.0&factor%5Bkpw_p%5D=0.0&ppw=true&factor%5Bppw_hr%5D=0.0&factor%5Bppw_p%5D=0.0&x25x=true&factor%5Bx25x_hr%5D=0.0&factor%5Bx25x_p%5D=0.0&mtp=true&factor%5Bmtp_hr%5D=0.0&factor%5Bmtp_p%5D=0.0&vh=true&factor%5Bvh_hr%5D=0.0&factor%5Bvh_p%5D=0.0&factor%5Bcost%5D=0.08&sort=Profitability24&volume=0&revenue=24h&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bitforex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=dove&factor%5Bexchanges%5D%5B%5D=exmo&factor%5Bexchanges%5D%5B%5D=gate&factor%5Bexchanges%5D%5B%5D=graviex&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=hotbit&factor%5Bexchanges%5D%5B%5D=ogre&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=stex&dataset=Main'
xhtml = ""
DatosMinadoCoin = ""

class parentWindow(QtWidgets.QMainWindow, Ui_Interfaz1):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.father = Ui_Interfaz1()
        self.father.setupUi(self)
        self.father.Warning0.setVisible(0)


class childWindow(QtWidgets.QMainWindow, Ui_Interfaz2):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.child = Ui_Interfaz2()
        self.child.setupUi(self)

        self.child.Costo.setEnabled(0)
        self.child.TituloMain.setVisible(0)

        self.child.Extraer.clicked.connect(self.extraerDatos)
        self.child.Limpiar.clicked.connect(self.limpiar)
        self.child.Cerrar.clicked.connect(self.cerrar)
        self.child.CalcularTiempo.clicked.connect(self.CalcularGanancias)
        self.child.MostrarRaking.clicked.connect(self.MostrarRanking)


    #Usado para prevenir el http error 403
        opener = urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
    #End

        Respuesta1 = urllib.request.Request(url1) 
        f = urllib.request.urlopen(Respuesta1)
        global xhtml
        xhtml = f.read().decode('utf-8')

    #Parte Web scrapping para la 2da pestaña
        Respuesta2 = requests.get(url2)
        global DatosMinadoCoin
        DatosMinadoCoin = Respuesta2.json()

        soup = BeautifulSoup(xhtml, "lxml")

        PrecioCoins = [
            soup.find("a", attrs={"href": "/coins/1-btc-sha-256"}).text,
            soup.find("a", attrs={"href": "/coins/166-zec-equihash"}).text,
            soup.find("a", attrs={"href": "/coins/151-eth-ethash"}).text,
            soup.find("a", attrs={"href": "/coins/101-xmr-randomx"}).text,
            soup.find("a", attrs={"href": "/coins/162-etc-etchash"}).text,
            soup.find("a", attrs={"href": "/coins/34-dash-x11"}).text,
            soup.find("a", attrs={"href": "/coins/4-ltc-scrypt"}).text
            ]  # Se crea una lista donde se guarda los precios de todas las monedas.

        PrecioCoins = (list(map(lambda x: x.strip(), PrecioCoins))) # Esto se usa para borrar todos los /n en la lista
        PrecioCoinsLimpia = [Limpiador.replace('$', '') for Limpiador in PrecioCoins]

        global PrecioCoinsLimpia2
        PrecioCoinsLimpia2 = [Limpiador.replace(',', '') for Limpiador in PrecioCoinsLimpia]

        ImgCoins = [
            str(soup.find("img", attrs={"alt": "BTC"})),
            str(soup.find("img", attrs={"alt": "ETH"})),
            str(soup.find("img", attrs={"alt": "ZEC"})),
            str(soup.find("img", attrs={"alt": "XMR"})),
            str(soup.find("img", attrs={"alt": "ETC"})),
            str(soup.find("img", attrs={"alt": "DASH"})),
            str(soup.find("img", attrs={"alt": "LTC"}))
            ]
        ImgCoinsSoup = list(range(len(ImgCoins)))
        Image = list(range(len(ImgCoins)))

        for Coins in range(len(ImgCoins)):
            ImgCoinsSoup[Coins] = BeautifulSoup(ImgCoins[Coins], 'html.parser')
            Image[Coins] = ImgCoinsSoup[Coins].img['src']

        urllib.request.urlretrieve(Image[0], "Iconos/BTC.png")
        urllib.request.urlretrieve(Image[1], "Iconos/ETH.png")
        urllib.request.urlretrieve(Image[2], "Iconos/ZEC.png")
        urllib.request.urlretrieve(Image[3], "Iconos/XMR.png")
        urllib.request.urlretrieve(Image[4], "Iconos/ETC.png")
        urllib.request.urlretrieve(Image[5], "Iconos/DASH.png")
        urllib.request.urlretrieve(Image[6], "Iconos/LTC.png")

        self.child.PrecioBTC.setText(PrecioCoins[0])
        self.child.PrecioETH.setText(PrecioCoins[2])
        self.child.PrecioZEC.setText(PrecioCoins[1])
        self.child.PrecioXMR.setText(PrecioCoins[3])
        self.child.PrecioETC.setText(PrecioCoins[4])
        self.child.PrecioDASH.setText(PrecioCoins[5])
        self.child.PrecioLTC.setText(PrecioCoins[6])
        
        self.child.PrecioBTCimg.setPixmap(QtGui.QPixmap("Iconos/BTC.png"))
        self.child.PrecioETHimg.setPixmap(QtGui.QPixmap("Iconos/ETH.png"))
        self.child.PrecioZECimg.setPixmap(QtGui.QPixmap("Iconos/ZEC.png"))
        self.child.PrecioXMRimg.setPixmap(QtGui.QPixmap("Iconos/XMR.png"))
        self.child.PrecioETCimg.setPixmap(QtGui.QPixmap("Iconos/ETC.png"))
        self.child.PrecioDASHimg.setPixmap(QtGui.QPixmap("Iconos/DASH.png"))
        self.child.PrecioLTCimg.setPixmap(QtGui.QPixmap("Iconos/LTC.png"))
    
    # Primera pestaña
    def extraerDatos(self):
        self.child.Costo.setEnabled(1)
        self.child.Warning1.setVisible(0)
        self.child.TituloMain.setVisible(1)

        RespuestaMiner = requests.get('http://127.0.0.1:4067/summary').json()
        B = RespuestaMiner
        
        #with open("SumarryOr.json") as B:
        #    B = json.load(B)

        Wallet = B["active_pool"]["user"]
        global Algo
        Algo = B["algorithm"]

        graficas = [
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]
                 ]

        Mensaje = [0, 0, 0, 0, 0]
        Mensaje2 = ""
        global HashrateTotal
        HashrateTotal = 0
        for entity in B["gpus"]:

            DeviceID = entity["device_id"]

            GPUs = entity["name"]
            graficas[DeviceID][0] = GPUs

            Vendor = entity["vendor"]
            graficas[DeviceID][1] = Vendor

            Hashrate = entity["hashrate"]
            graficas[DeviceID][2] = Hashrate

            Power = entity["power"]
            graficas[DeviceID][3] = Power

            Temperature = entity["temperature"]
            graficas[DeviceID][4] = Temperature

            PCI_bus = entity["pci_bus"]
            graficas[DeviceID][5] = PCI_bus

            Mensaje[DeviceID] = "Dispositivo: " + graficas[DeviceID][0] + "\n   ID: " + str(DeviceID) + "\n   Vendor: " + str(graficas[DeviceID][1]) + "\n   Hashrate: " + str(
                graficas[DeviceID][2]) + "\n   Consumo: " + str(graficas[DeviceID][3]) + "\n   Temperatura: " + str(graficas[DeviceID][4]) + "\n   PCI_bus: " + str(graficas[DeviceID][5])

            Mensaje2 = Mensaje2 + str(Mensaje[DeviceID]) + "\n"
            Mensaje3 = "Billetera actual: \n   " + Wallet + \
                "\nAlgoritmo usado: " + Algo + "\n" + Mensaje2
            self.child.CuadroDatos.setText(Mensaje3)
            
            HashrateTotal = HashrateTotal + graficas[DeviceID][2]
            global WattsTotal
            WattsTotal = WattsTotal + graficas[DeviceID][3]

    def limpiar(self):
        self.child.CuadroDatos.setText("")

    def cerrar(self):
        sys.exit(app.exec_())

    # Segunda pestaña
    def CalcularGanancias(self):
        
        if(self.child.EditInversion.text() == ""):
            self.child.CuadroCostos.setText("RECUERDA INGRESAR DATOS")
            self.child.CuadroCostos.setStyleSheet("background: none;\n" "font: 19.5pt \"MS Shell Dlg 2\";\n" "color: RED;\n""")
        elif(self.child.EditCostoEnergia.text() == ""):
            self.child.CuadroCostos.setText("RECUERDA INGRESAR DATOS")
            self.child.CuadroCostos.setStyleSheet("background: none;\n" "font: 19.5pt \"MS Shell Dlg 2\";\n" "color: RED;\n""")   
        elif(float(self.child.EditInversion.text()) <= 0):
            self.child.CuadroCostos.setText("RECUERDA INGRESAR DATOS")
            self.child.CuadroCostos.setStyleSheet("background: none;\n" "font: 19.5pt \"MS Shell Dlg 2\";\n" "color: RED;\n""")
        elif(float(self.child.EditCostoEnergia.text()) <= 0):
            self.child.CuadroCostos.setText("RECUERDA INGRESAR DATOS \nMAYORES A 0")
            self.child.CuadroCostos.setStyleSheet("background: none;\n" "font: 19.5pt \"MS Shell Dlg 2\";\n" "color: RED;\n""")     
        else:
            self.child.CuadroCostos.setStyleSheet("background: none;\n" "font: 19.5pt \"MS Shell Dlg 2\";\n" "color: WHITE;\n""")
            EditInversion = float(self.child.EditInversion.text())
            EditCostoEnergia = float(self.child.EditCostoEnergia.text())
            PrecioCoinUSD = 0
            BlockReward = 0
            BlockTime = 0
            netHash = 0

            #nethash está en GigaH/s
            if Algo == 'btc':
                PrecioCoinUSD = float(PrecioCoinsLimpia2[0])
                BlockReward = 6.25
                BlockTime = 600 #segundos
                netHash = 160725180000 # Gh/s
            if Algo == 'zec':
                PrecioCoinUSD = float(PrecioCoinsLimpia2[1])
                BlockReward = 3.13 #segundos
                BlockTime = 75 #segundos
                netHash = 54.919  #Gh/s
            if Algo == 'eth':
                PrecioCoinUSD = float(PrecioCoinsLimpia2[2])
                BlockReward = float(DatosMinadoCoin["coins"]["Ethereum"]["block_reward"])
                BlockTime = float(DatosMinadoCoin["coins"]["Ethereum"]["block_time"])
                netHash = float(DatosMinadoCoin["coins"]["Ethereum"]["nethash"]) / 1e9
            if Algo == 'xmr':
                PrecioCoinUSD = float(PrecioCoinsLimpia2[3])
                BlockReward = float(DatosMinadoCoin["coins"]["Monero"]["block_reward"])
                BlockTime = float(DatosMinadoCoin["coins"]["Monero"]["block_time"])
                netHash = float(DatosMinadoCoin["coins"]["Monero"]["nethash"]) / 1e9
            if Algo == 'etc':
                PrecioCoinUSD = float(PrecioCoinsLimpia2[4])
                BlockReward = float(DatosMinadoCoin["coins"]["EthereumClassic"]["block_reward"])
                BlockTime = float(DatosMinadoCoin["coins"]["EthereumClassic"]["block_time"])
                netHash = float(DatosMinadoCoin["coins"]["EthereumClassic"]["nethash"]) / 1e9
            if Algo == 'dash':
                PrecioCoinUSD = float(PrecioCoinsLimpia2[5]) 
                BlockReward = 2.88
                BlockTime = 150 #segundos
                netHash = 5100000 #Gh/s
            if Algo == 'ltc':
                PrecioCoinUSD = float(PrecioCoinsLimpia2[6])
                BlockReward = 12.5
                BlockTime =  150 #segundos
                netHash = 294370 #Gh/s
            if Algo == 'kawpow':
                PrecioCoinUSD = float(DatosMinadoCoin["coins"]['Ravencoin']['exchange_rate24']) * float(PrecioCoinsLimpia2[0])
                BlockReward = float(DatosMinadoCoin["coins"]["Ravencoin"]["block_reward"])
                BlockTime = float(DatosMinadoCoin["coins"]["Ravencoin"]["block_time"])
                netHash = float(DatosMinadoCoin["coins"]["Ravencoin"]["nethash"]) / 1e9
                

            userRatio = HashrateTotal / (netHash * 1e9) #La contribución del usuario a la red de minado global
            blockMins = 60 / BlockTime #Cantidad de bloques que se consiguen al minuto
            CoinsPerMin = blockMins * BlockReward #Canidad de ETH que se consigue por minuto
            earningMin = userRatio * CoinsPerMin #Cantidad de Eth que consigue el usuario por minuto
            Coin1h = earningMin * 60 #A la hora
            Coin1d = Coin1h * 24 #Al día
            PrecioUSD = Coin1d * PrecioCoinUSD
            kWhDia = (WattsTotal * 24) / 1000
            PagoElectricidadDia = kWhDia * EditCostoEnergia
            GananciasPlusElectriciad = PrecioUSD - PagoElectricidadDia
            
        
            Texto = ""
            TiempoRecuperarDias = float("{0:.1f}".format(EditInversion / GananciasPlusElectriciad))
            if(TiempoRecuperarDias <= 31):
                Texto = "Días: "+ str(TiempoRecuperarDias) 
            if(TiempoRecuperarDias > 31):
                Texto = "Meses: " + str(float("{0:.1f}".format(TiempoRecuperarDias/31))) +"\nDías: "+ str(TiempoRecuperarDias)
            if(TiempoRecuperarDias/31 > 12):
                Texto = "Años: "+ str(float("{0:.1f}".format(TiempoRecuperarDias/356))) + "\nMeses: " + str(float("{0:.1f}".format(TiempoRecuperarDias/31))) +"\nDías: "+ str(TiempoRecuperarDias)
            self.child.CuadroCostos.setText(Texto)
    
    # Tercera pestaña
    def MostrarRanking(self):
        self.child.MostrarRaking.setVisible(0)
        Tablas = pd.read_html(xhtml) # Se guarda todas las tablas de la página
        GPURankingTableP = Tablas[0]
        Separados = list(range(len(GPURankingTableP)))
        Hashrate = list(range(len(GPURankingTableP)))
        CEnergetico = list(range(len(GPURankingTableP)))

        for i in range(len(Separados)):
            Separados[i] = GPURankingTableP.at[i,'Hashrate'].split()

        for j in range(len(Separados)):
            Hashrate[j] = Separados[j][0] + Separados[j][1]
            CEnergetico[j] = Separados[j][2] + " - " + Separados[j][4]


        self.child.Modelo.setText("GRÁFICA")
        self.child.FechaSalida.setText("FECHA DE SALIDA")
        self.child.Hashrate.setText("HASHRATE")
        self.child.CE.setText("CONSUMO ENERGÉTICO")

        #Rank1
        self.child.GPURank1.setText(GPURankingTableP.at[0,'Model'])
        Color = GPURankingTableP.at[0,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank1.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank1.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank1.setText(GPURankingTableP.at[0,'Release Date'])
        self.child.HRank1.setText(Hashrate[0])
        self.child.CERank1.setText(CEnergetico[0])

        #Rank2
        self.child.GPURank2.setText(GPURankingTableP.at[1,'Model'])
        Color = GPURankingTableP.at[1,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank2.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank2.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank2.setText(GPURankingTableP.at[1,'Release Date'])
        self.child.HRank2.setText(Hashrate[1])
        self.child.CERank2.setText(CEnergetico[1])
        
        #Rank3
        self.child.GPURank3.setText(GPURankingTableP.at[2,'Model'])
        Color = GPURankingTableP.at[2,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank3.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank3.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank3.setText(GPURankingTableP.at[2,'Release Date'])
        self.child.HRank3.setText(Hashrate[2])
        self.child.CERank3.setText(CEnergetico[2])

        #Rank4
        self.child.GPURank4.setText(GPURankingTableP.at[3,'Model'])
        Color = GPURankingTableP.at[3,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank4.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank4.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank4.setText(GPURankingTableP.at[3,'Release Date'])
        self.child.HRank4.setText(Hashrate[3])
        self.child.CERank4.setText(CEnergetico[3])

        #Rank5
        self.child.GPURank5.setText(GPURankingTableP.at[4,'Model'])
        Color = GPURankingTableP.at[4,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank5.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank5.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank5.setText(GPURankingTableP.at[4,'Release Date'])
        self.child.HRank5.setText(Hashrate[4])
        self.child.CERank5.setText(CEnergetico[4])

        #Rank6
        self.child.GPURank6.setText(GPURankingTableP.at[5,'Model'])
        Color = GPURankingTableP.at[5,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank6.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank6.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank6.setText(GPURankingTableP.at[5,'Release Date'])
        self.child.HRank6.setText(Hashrate[5])
        self.child.CERank6.setText(CEnergetico[5])

        #Rank7
        self.child.GPURank7.setText(GPURankingTableP.at[6,'Model'])
        Color = GPURankingTableP.at[6,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank7.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank7.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank7.setText(GPURankingTableP.at[6,'Release Date'])
        self.child.HRank7.setText(Hashrate[6])
        self.child.CERank7.setText(CEnergetico[6])

        #Rank8
        self.child.GPURank8.setText(GPURankingTableP.at[7,'Model'])
        Color = GPURankingTableP.at[7,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank8.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank8.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank8.setText(GPURankingTableP.at[7,'Release Date'])
        self.child.HRank8.setText(Hashrate[7])
        self.child.CERank8.setText(CEnergetico[7])

        #Rank9
        self.child.GPURank9.setText(GPURankingTableP.at[8,'Model'])
        Color = GPURankingTableP.at[8,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank9.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank9.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank9.setText(GPURankingTableP.at[8,'Release Date'])
        self.child.HRank9.setText(Hashrate[8])
        self.child.CERank9.setText(CEnergetico[8])

        #Rank10
        self.child.GPURank10.setText(GPURankingTableP.at[9,'Model'])
        Color = GPURankingTableP.at[9,'Model'].find('NVIDIA')
        if Color != -1:
            self.child.GPURank10.setStyleSheet("background: none;\n" "font: 14pt \"MS Shell Dlg 2\";\n" "color: rgb(20, 221, 20);\n""")
        else:
            self.child.GPURank10.setStyleSheet("background: none;\n" "font: 75 14pt \"MS Shell Dlg 2\";\n" "color:rgb(255, 47, 50);\n""")
        self.child.FechaRank10.setText(GPURankingTableP.at[9,'Release Date'])
        self.child.HRank10.setText(Hashrate[9])
        self.child.CERank10.setText(CEnergetico[9])

if __name__ == '__main__':
    def ValidarMinero():
        global Codigo
        Codigo = 0
        try:
            r = requests.get("http://127.0.0.1:4067", timeout=0.001)
        except:
            Codigo = 1
        if(Codigo == 0):
            child.show()
            window.close()
        else:
            window.father.Warning0.setVisible(1)
    app = QApplication(sys.argv)
    window=parentWindow()
    child=childWindow()
    window.show()
    window.father.Warning0.setVisible(0)
    window.setWindowIcon(QtGui.QIcon("Iconos/DURAPROFIT INVI.png"))
    child.setWindowIcon(QtGui.QIcon("Iconos/DURAPROFIT INVI.png"))
    window.father.ConectarTrex.clicked.connect(ValidarMinero)

    
    sys.exit(app.exec_())


