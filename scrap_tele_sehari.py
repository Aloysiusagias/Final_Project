from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
import csv

myprofile = webdriver.FirefoxProfile(r'C:\Users\Aloysius\AppData\Roaming\Mozilla\Firefox\Profiles\fcbei8vp.teleScrape')
PATH = "C:\Program Files (x86)\geckodriver.exe"
driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)

target = 4
Saham = ['AALI', 'ABBA', 'ABDA', 'ABMM', 'ACES', 'ACST', 'ADES', 'ADHI', 'ADMF', 'ADMG', 'ADRO', 'AGII', 'AGRO', 'AGRS', 'AHAP', 'AIMS', 'AISA', 'AKKU', 'AKPI', 'AKRA', 'AKSI', 'ALDO', 'ALKA' 'ALMI', 'ALTO', 'AMAG', 'AMFG', 'AMOR', 'AMRT', 'ANJT', 'ANTM', 'APEX', 'APIC', 'APII', 'APLI', 'APLN', 'ARGO', 'ARII', 'ARKA', 'ARNA', 'ARTA', 'ARTO', 'ASBI', 'ASDM', 'ASGR', 'ASII', 'ASJT', 'ASMI', 'ASPI', 'ASRI', 'ASRM', 'ASSA', 'ATIC', 'AYLS', 'BABP', 'BAPI', 'BBCA', 'BBHI', 'BBKP', 'BBLD', 'BBMD', 'BBNI', 'BBRI', 'BBRM', 'BBSI', 'BBSS', 'BBTN', 'BBYB', 'BCAP', 'BCIC', 'BCIP', 'BDMN', 'BEKS', 'BESS', 'BFIN', 'BGTG', 'BHAT', 'BHIT', 'BIKA', 'BIMA', 'BIPI', 'BIPP', 'BISI', 'BJBR', 'BJTM', 'BKDP', 'BKSL', 'BKSW', 'BLTA', 'BLTZ', 'BMAS', 'BMRI', 'BMSR', 'BMTR', 'BNBA', 'BNBR', 'BNGA', 'BNII', 'BNLI', 'BPFI', 'BPII', 'BPTR', 'BRAM', 'BRIS', 'BRMS', 'BRNA', 'BRPT', 'BSDE', 'BSIM', 'BSSR', 'BSWD', 'BTEK', 'BTEL', 'BTON', 'BTPN', 'BTPS', 'BUKK', 'BUVA', 'BVIC', 'BWPT', 'BYAN', 'CAKK', 'CANI', 'CASA', 'CASS', 'CBMF', 'CCSI', 'CEKA','CENT', 'CFIN', 'CINT', 'CITA', 'CLAY', 'CLEO', 'CLPI', 'CMNP', 'CMPP', 'CNKO', 'CNTX', 'COCO', 'COWL', 'CPIN', 'CPRI', 'CPRO', 'CSAP', 'CSIS', 'CSMI', 'CSRA', 'CTBN', 'CTRA', 'CTTH', 'DART', 'DCII', 'DEFI', 'DFAM', 'DGIK', 'DGNS', 'DIGI', 'DILD', 'DIVA', 'DKFT', 'DLTA', 'DMAS', 'DMMX', 'DMND', 'DNAR', 'DNET', 'DOID', 'DPNS', 'DPUM', 'DSFI', 'DSNG', 'DSSA', 'DUCK', 'DUTI', 'DVLA', 'DWGL', 'ECII', 'EKAD', 'ELSA', 'ELTY', 'EMDE', 'EMTK', 'ENRG', 'ENVY', 'ENZO', 'EPAC', 'EPMT', 'ERAA', 'ERTX', 'ESIP', 'ESSA', 'ESTA', 'ESTI', 'ETWA', 'EXCL', 'FAPA', 'FASW', 'FILM', 'FINN', 'FIRE', 'FISH', 'FITT', 'FMII', 'FORU', 'FORZ', 'FPNI', 'FREN', 'FUJI', 'GAMA', 'GDST', 'GDYR', 'GEMS', 'GGRM', 'GGRP', 'GHON', 'GIAA', 'GJTL', 'GLOB', 'GLVA', 'GMFI', 'GMTD', 'GOLL', 'GPRA', 'GSMF', 'GTBO', 'GWSA', 'GZCO', 'HADE', 'HDFA', 'HDIT', 'HDTX', 'HKMU', 'HMSP', 'HOMI', 'HOTL', 'HRME', 'HRTA', 'HRUM', 'IATA', 'IBFN', 'IBST', 'ICBP', 'ICON', 'IDPR', 'IFII', 'IFSH', 'IGAR', 'IIKP', 'IKAI', 'IKBI', 'IMAS', 'IMJS', 'IMPC', 'INAF', 'INAI', 'INCF', 'INCI', 'INCO', 'INDF', 'INDR', 'INDS', 'INDX', 'INDY', 'INKP', 'INOV', 'INPC', 'INPP', 'INPS', 'INRU', 'INTA', 'INTD', 'INTP', 'IPCC', 'IPCM', 'IPOL', 'IPTV', 'IRRA', 'ISAT', 'ISSP', 'ITIC', 'ITMA', 'ITMG', 'JAST', 'JECC', 'JGLE', 'JIHD', 'JKON', 'JKSW', 'JMAS', 'JPFA', 'JRPT', 'JSKY', 'JSMR', 'JSPT', 'JTPE', 'KAEF', 'KARW', 'KBAG', 'KBLI', 'KBLM', 'KBLV', 'KBRI', 'KDSI', 'KEEN', 'KICI', 'KIJA', 'KINO', 'KIOS', 'KJEN', 'KKGI', 'KLBF', 'KMDS', 'KMTR', 'KOBX', 'KOIN', 'KONI', 'KPAL', 'KPAS', 'KPIG', 'KRAH', 'KRAS', 'KREN', 'LAPD', 'LCGP', 'LCKM', 'LMAS', 'LMPI', 'LMSH', 'LPCK', 'LPGI', 'LPIN', 'LPKR', 'LPLI', 'LPPF', 'LPPS', 'LRNA', 'LSIP', 'LTLS', 'MAGP', 'MAPA', 'MAPB', 'MAPI', 'MARK', 'MBAP', 'MBSS', 'MBTO', 'MCAS', 'MCOR', 'MDIA', 'MDKA', 'MDKI', 'MDLN', 'MDRN', 'MEDC', 'MEGA', 'META', 'MFIN', 'MFMI', 'MGNA', 'MGRO', 'MICE', 'MIDI', 'MIKA', 'MINA', 'MIRA', 'MITI', 'MKNT', 'MKPI', 'MLBI', 'MLIA', 'MLPL', 'MLPT', 'MMLP', 'MNCN', 'MOLI', 'MPMX', 'MPOW', 'MPPA', 'MPRO', 'MRAT', 'MREI', 'MSIN', 'MSKY', 'MTDL', 'MTFN', 'MTLA', 'MTPS', 'MTRA', 'MTSM', 'MTWI', 'MYOH', 'MYOR', 'MYRX', 'MYTX', 'NELY', 'NFCX', 'NICK', 'NIKL', 'NIPS', 'NIRO', 'NISP', 'NOBU', 'NRCA', 'NZIA', 'OASA', 'OCAP', 'OKAS', 'OMRE', 'OPMS', 'PAMG', 'PANI', 'PANR', 'PANS', 'PBID', 'PBRX', 'PBSA', 'PCAR', 'PDES', 'PEGE', 'PEHA', 'PGAS', 'PGJO', 'PGLI', 'PGUN', 'PICO', 'PJAA', 'PKPK', 'PLAS', 'PLIN', 'PMJS', 'PMMP', 'PNBN', 'PNBS', 'PNGO', 'PNIN', 'PNLF', 'PNSE', 'POLI', 'POLL', 'POLU', 'POLY', 'POSA', 'POWR', 'PPGL', 'PPRE', 'PPRO', 'PRAS', 'PRDA', 'PRIM', 'PSAB', 'PSDN', 'PSGO', 'PSKT', 'PSSI', 'PTBA', 'PTDU', 'PTIS', 'PTPP', 'PTPW', 'PTRO', 'PTSN', 'PTSP', 'PUDP', 'PWON', 'PYFA', 'PZZA', 'RALS', 'RANC', 'RBMS', 'RDTX', 'RELI', 'RICY', 'RIGS', 'RIMO', 'RMBA', 'RONY', 'RUIS', 'SAME', 'SAMF', 'SAPX', 'SBAT', 'SCCO', 'SCMA', 'SCNP', 'SCPI', 'SDMU', 'SDPC', 'SDRA', 'SFAN', 'SGER', 'SGRO', 'SHID', 'SHIP', 'SIDO', 'SILO', 'SIMA', 'SIMP', 'SIPD', 'SKBM', 'SKLT', 'SKRN', 'SKYB', 'SLIS', 'SMAR', 'SMBR', 'SMCB', 'SMDM', 'SMDR', 'SMGR', 'SMKL', 'SMMA', 'SMMT', 'SMRA', 'SMRU', 'SMSM', 'SOCI', 'SOFA', 'SOHO', 'SONA', 'SOSS', 'SOTS', 'SPMA', 'SPTO', 'SQMI', 'SRAJ', 'SRIL', 'SRSN', 'SRTG', 'SSIA', 'SSMS', 'SSTM', 'STTP', 'SUGI', 'SULI', 'SUPR', 'TALF', 'TAMA', 'TARA', 'TBIG', 'TBLA', 'TBMS', 'TCID', 'TCPI', 'TDPM', 'TEBE', 'TELE', 'TFAS', 'TFCO', 'TGKA', 'TGRA', 'TIFA', 'TINS', 'TIRA', 'TIRT', 'TKIM', 'TLKM', 'TMAS', 'TMPO', 'TNCA', 'TOBA', 'TOPS', 'TOTL', 'TOTO', 'TOWR', 'TOYS', 'TPIA', 'TPMA', 'TRAM', 'TRIL', 'TRIN', 'TRIS', 'TRJA', 'TRST', 'TSPC', 'TURI', 'UCID', 'UFOE', 'ULTJ', 'UNIC', 'UNIQ', 'UNSP', 'UNTR', 'UNVR', 'URBN', 'VICI', 'VICO', 'VINS', 'VIVA', 'VOKS', 'VRNA', 'WAPO', 'WEGE', 'WEHA', 'WICO', 'WIIM', 'WIKA', 'WINS', 'WMUU', 'WOMF', 'WOOD', 'WOWS', 'WSBP', 'WSKT', 'WTON', 'YELO', 'YPAS', 'YULE', 'ZBRA', 'ZINC']
SahamAmbigu = ['AGAR', 'AKSI', 'AMAN', 'AMAR', 'AMIN', 'ANDI', 'ARMY', 'ARTI', 'ATAP', 'AUTO', 'BACA', 'BAJA', 'BALI', 'BANK', 'BAPA', 'BATA', 'BAYU', 'BEBS', 'BEEF', 'BELL', 'BEST', 'BINA', 'BIRD', 'BLUE', 'BOGA', 'BOLA', 'BOLT', 'BOSS', 'BUDI', 'BULL', 'BUMI', 'CAMP', 'CARE', 'CARS', 'CASH', 'CITY', 'DADA', 'DAYA', 'DEAL', 'DEWA','DYAN', 'EAST', 'EDGE', 'FAST', 'GOLD', 'GOOD', 'HEAL', 'HELI', 'HERO', 'HEXA', 'HITS', 'HOKI', 'HOME', 'IKAN', 'INDO', 'JAWA', 'JAYA', 'KAYU', 'KEJU', 'KIAS', 'KOPI', 'KOTA', 'LAND', 'LEAD', 'LIFE', 'LINK', 'LION', 'LUCK','MABA', 'MAIN', 'MAMI', 'MARI', 'MASA', 'MAYA', 'MERK', 'NASA', 'NATO', 'NUSA', 'PADI', 'PALM', 'PLAN', 'POLA', 'POOL', 'PORT', 'PURA', 'PURE', 'PURI', 'RAJA', 'REAL', 'RISE', 'ROCK', 'RODA', 'ROTI', 'SATU', 'SINI', 'STAR', 'SURE', 'SWAT', 'TAMU', 'TAXI','TECH', 'TRUK', 'TRIM', 'TRIO', 'TUGU', 'UANG', 'UNIT', 'WIFI', 'ZONE', 'TRUS', 'FOOD', 'SAFE', 'GEMA']
# Saham = ['ADHI', 'ADRO', 'AKRA', 'ANTM', 'ASII', 'ASRI', 'BBCA', 'BBNI', 'BBRI', 'BBTN', 'BKSL', 'BMRI', 'BSDE', 'CPIN', 'ELSA', 'EXCL', 'GGRM', 'HMSP', 'ICBP', 'INCO', 'INDF', 'INDY', 'INKP', 'INTP', 'ITMG', 'JSMR', 'KLBF', 'LPKR', 'LPPF', 'MEDC', 'MNCN', 'PGAS', 'PTBA', 'PTPP', 'SCMA', 'SMGR', 'SRIL', 'SSMS', 'TLKM', 'TPIA', 'UNTR', 'UNVR', 'WIKA', 'WSBP', 'WSKT']
# , 'TAHAN', 'HOLD', 'HALT', 'EIDO', 'IHSG','THN', 'THAN', 'THAN', "ARA", "ARB", "DIVIDEN", "DVDEN", "DIVDEN", "DVIDEN", "DVDEN", "UP", "DOWN", "LOSS", "CUAN", "CUTLOSS", "RUGI", "KEATAS", "JEBOL", "BUY", "SELL", "JUAL", "BELI"

driver.get('https://web.telegram.org/#/im?p=@TheTradersGroup')
time.sleep(5)

wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
jumlah = 1
scrap = len(chat)
smntr = len(chat)
psn = len(chat)
penulis = ""
pesan2 = [""]
jam = ""
time.sleep(2)
tanggal = []
tanggal2 = []
n = 0
lastline = psn
tambah = 0
psn2 = 0
hari = 0
belum = hari!=target
akumulasi = {}
indikasi = []
with open('indikasi.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for i in readCSV:
        indikasi.insert(len(indikasi),i[0])
# print(indikasi)

normalizad_word = pd.read_excel("Normalisasi.xlsx")
normalizad_word_dict = {}
print('jalan1')
for index, row in normalizad_word.iterrows():
    if row[0] not in normalizad_word_dict:
        normalizad_word_dict[row[0]] = row[1] 
print('jalan2')
def normalized_term(document):
    document = document.split(' ')
    aaa = [normalizad_word_dict[term] if term in normalizad_word_dict else term for term in document]
    aaa = ' '.join(aaa)
    return(aaa)
print('jalan3')
f = open("Scrap2Juni.txt","w+")
html = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]')
# try :
while belum:
    # if(psn < 0):
    #     lastline = abs(psn)
    #     wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    #     chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
    #     # print(len(chat))
    #     jumlah2 = len(chat)
    #     while jumlah2 != lastline:
    #         html = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]')
    #         wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    #         chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
    #         driver.execute_script("arguments[0].scrollTop = 0", html)
    #         jumlah2 = len(chat)
    waktu = time.time() + 5
    if (psn>5):
        time.sleep(0.25)
    elif (psn>1) :
        time.sleep(1)
    while (psn==1):
        time.sleep(1)
        scrap = psn
        wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
        chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
        scrap = len(chat)
        ada = len(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(psn)+"]")) > 0
        # if(not(ada)):
        #     psn+=20
        #     print('jalan')
        if(smntr!=scrap):
            psn2 = scrap - smntr
            smntr = scrap
            psn += psn2
            # psn +=1
        if (int(time.time())>int(waktu)):
            # print("Sudah 5 detik")
            # print(int(time.time()))
            driver.execute_script("arguments[0].scrollTop = 0", html)
            waktu = time.time() + 5
    scrap = psn
    wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
    scrap = len(chat)
    ada = len(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(psn)+"]")) > 0
    # if(not(ada)):
    #     psn+=20
    #     print('jalan')
    if(smntr!=scrap):
        psn2 = scrap - smntr
        smntr = scrap
        psn += psn2
    while(psn==0):
        print('########################################################################################################')
        time.sleep(2)
        wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
        chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
        scrap = len(chat)
        psn = scrap - smntr
        smntr = scrap
        psn +=1
    while not(ada):
        ada = len(driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(psn)+"]")) > 0        
        driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(psn)+"]"))
        time.sleep(0.25)
        # psn+=20
        print('wait')
    pesan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(psn)+"]")
    driver.execute_script("arguments[0].scrollIntoView(true);", pesan)
    psn-=1
    try:
        if (len(pesan.find_elements_by_xpath(".//a[@class='im_message_photo_thumb']")) > 0) :
            # print('ini adalah foto')
            penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
            gambar = pesan.find_element_by_xpath(".//img[@class='im_message_photo_thumb']").get_attribute('src')
            # pesan2.insert(0,"Gambar : "+gambar)
            pesan2.insert(0, "Ini adalah foto")
            if (len(pesan.find_elements_by_xpath(".//div[@class='im_message_photo_caption']")) > 0):
                last = pesan.find_element_by_xpath(".//div[@class='im_message_photo_caption']").text
                emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                for x in emo :
                    if(x.text.strip()!=''):
                        last = last.replace(x.text.strip(), ' ')
                pesan2.insert(0, last)
            jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
        elif (len(pesan.find_elements_by_xpath(".//span[@ng-switch-when='messageActionChatJoined']")) > 0):
            # print('seseorang join')
            # penulis = pesan.find_element_by_xpath(".//div[@class='im_service_message']").text
            penulis = ''
            last = penulis
            pesan2 = [""]
            jam = ''
        elif (len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_split_text']")) > 0):
            if((len(pesan.find_elements_by_xpath(".//div[@class='im_message_date_split im_service_message_wrap' and @style='display: none;']")) > 0)):
                penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                last = pesan.find_element_by_xpath(".//div[@class='im_message_text']").text
                emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                for x in emo :
                    if(x.text.strip()!=''):
                        last = last.replace(x.text.strip(), ' ')
                pesan2.insert(0, last)
                jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
            else :
                print("ini adalah tanggal")
                tgl = pesan.find_element_by_xpath(".//span[@class='im_message_date_split_text']").text
                tgl = tgl.replace(",","")
                print(tgl)
                for k in range(len(tanggal2)):
                    tanggal2[k]['Tanggal'] = tgl
                    # time.sleep(0.1)
                f.write("########################################################"+tgl+"########################################################")
                tanggal.extend(tanggal2)
                hari +=1
                belum = (hari!=target)
                print(len(tanggal))
                tanggal2 = []
        else :
            # print('ini adalah pesan biasa')
            penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
            jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
            last = pesan.find_element_by_xpath(".//div[@class='im_message_text']").text
            emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
            for x in emo :
                if(x.text.strip()!=''):
                    last = last.replace(x.text.strip(), ' ')
            pesan2.insert(0, last)
            if(len(pesan.find_elements_by_xpath(".//span[@my-short-message='replyMessage']"))>0):
                balas = pesan.find_element_by_xpath(".//span[@my-short-message='replyMessage']").text
                balas = "Membalas : " + balas
                emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                for x in emo :
                    if(x.text.strip()!=''):
                        balas = balas.replace(x.text.strip(), ' ')
                pesan2.insert(0,balas)
    except: 
        penulis = "Error"
        pesan2 = "Error"
    pesan3 = "\n".join(pesan2)
    masuk1 = False
    masuk2 = False
    masuk = False
    stop = [",", ".", "#", "?", "*", "-"]
    cek = pesan3
    bahas = []
    bahasAmbigu = []
    for x in stop:
        cek = cek.replace(x, " ")
    for x in pesan3:
        b = x.isascii()
        if not b:
            pesan3 = pesan3.replace(x, ' ')
    cek = cek.replace('nya', '')
    cek = normalized_term(cek)
    # print(cek)
    if any(word in cek.upper().split() for word in Saham):
        masuk1 = True
    elif any(word in cek.split() for word in SahamAmbigu):
        masuk1 = True
    if any(word.upper() in cek.upper().split() for word in indikasi):
        masuk2 = True
    if(masuk1 and masuk2):
        masuk = True
    # bahas = [word for word in Saham if word in cek.upper().split()]
    # bahasAmbigu = [word for word in SahamAmbigu if word in cek.split()]
    # indikasiMasuk = [word for word in indikasi if word.upper() in cek.upper().split()]
    # print(pesan3, bahas, bahasAmbigu, indikasiMasuk)
    if(penulis != ""):
        if(masuk):
            bahas = [word for word in Saham if word in cek.upper().split()]
            bahasAmbigu = [word for word in SahamAmbigu if word in cek.split()]
            indikasiMasuk = [word for word in indikasi if word.upper() in cek.upper().split()]
            if bahasAmbigu:
                bahas.extend(bahasAmbigu)
            for x in penulis:
                c = x.isascii()
                if not c:
                    penulis = penulis.replace(x, ' ')
            for a in bahas :
                if a in akumulasi:
                    akumulasi[a]+=1
                else :
                    akumulasi[a]=1
            bahas = ",".join(bahas)
            print("Data : "+str(psn))
            print("user : "+penulis)
            # try:
            f.write("Data : "+ str(jumlah) +"\nUser : "+ penulis +"\n"+pesan3+"\nSaham : "+bahas+"\nJam : "+jam+"\n==========================\n")
            # except:
            #     print("Tidak bisa menampilkan pesan")
            print(pesan3)
            print("Saham : "+bahas)
            print("Indikasi : ",indikasiMasuk)
            print("jam : " + jam)
            print('=======================================================')
            item = {
                'Data' : jumlah,
                'User' : penulis,
                'Pesan' : pesan3,
                'Saham' : bahas,
                'Jam' : jam
            }
            tanggal2.append(item)

            jumlah+=1
        penulis = ""
        pesan2 = []
    jam = ""
# except:
#     print('Error')
akumulasi = {k: v for k, v in sorted(akumulasi.items(), key=lambda item: item[1])}
print(akumulasi)
f.write(str(akumulasi))
f.close()
df = pd.DataFrame(tanggal)
df.to_csv('Scrap2Juni.csv')