from flask import Flask, render_template
from flask_socketio import SocketIO
from flask import url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.externals import joblib
from Pre2 import Preprocessing
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
from svm import svm
import json
from selenium.webdriver.firefox.options import Options
from userNull import userNulll
import csv

ratee = pd.read_csv('../User Rating/Rating.csv')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from flask_socketio import send, emit

@app.route('/')
def home():
	return render_template('chat.html')

@app.route('/predict',methods=['POST'])
def predict():
    # teks = "Membalas : Saham mana yg arb berhari2 IKAN mungkin wkwk" #Negatif
    # teks = "Doid masih aman kalo belinya pas april 2020" #Positif
    teks = "Ati2 bank uda kena brp x suspend... Buangan nya banyak tuh barusan.jgn dikejar"

    svm = SVC(kernel='rbf')
    cv = TfidfVectorizer(use_idf=True)

    df = pd.read_csv('readytfidf3.csv')
    df = df.sample(frac = 1)
    df['Status'] = df['Status'].replace(['Negatif', 'Positif'], ['0','1'])
    y = df['Status']
    X = df['Normal']
    X = cv.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    svm.fit(X_train,y_train)
    print("accuracy score: " + str(svm.score(X_test, y_test)))
    if request.method == 'POST':
        tekss = request.form['message']
        tekss = Preprocessing(tekss)
        print(tekss)
        vect = cv.transform([tekss])
        my_prediction = svm.predict(vect)
        my_prediction = int(my_prediction[0])
        print("accuracy score: " + str(svm.score(X_test, y_test)))
        print(my_prediction)
    return render_template('result.html',prediction = my_prediction)

@socketio.on('my event')
def handle_my_custom_event(json):
    def formatJam(teks):
        global sawaktu, tawaktu, AM, PM, tawaktu2
        if(not "sawaktu" in globals()):
            sawaktu = ''
            tawaktu = 0
            tawaktu2 = 0
            AM = {
                'sawaktu' : '',
                'tawaktu' : 0
            }
            PM = {
                'sawaktu' : '',
                'tawaktu' : 0
            }
        # print('Jam nya adalah : '+teks)
        formm = teks.split()
        satuan = formm[1]
        jamm = formm[0]
        jamm = jamm.split(':')
        jam2 = jamm[0]
        if(int(jam2) == 12):
            jam2 = "00"
        elif(int(jam2)<10):
            jam2 = "0" + str(jam2)
        menit = jamm[1]
        detik = jamm[2]
        formatt = jam2+menit+detik
        if(sawaktu!=satuan):
            sawaktu = satuan
            if(sawaktu == 'AM'):
                if(formatt!=AM['tawaktu']):
                    tawaktu +=1
                    tawaktu2 = tawaktu
                    AM['tawaktu'] = tawaktu2
                else:
                    tawaktu2 = AM['tawaktu']
            elif(sawaktu == 'PM'):
                if(formatt!=PM['sawaktu']):
                    tawaktu +=1
                    tawaktu2 = tawaktu
                    PM['tawaktu'] = tawaktu2
                else:
                    tawaktu2 = PM['tawaktu']
        formatt = str(tawaktu2) + formatt
        return int(formatt)

    def ascii(teks):
        for x in teks:
            b = x.isascii()
            if not b:
                teks = teks.replace(x, ' ')
        return teks

    # options = Options()
    # options.add_argument('--headless')

    myprofile = webdriver.FirefoxProfile(r'C:\Users\Aloysius\AppData\Roaming\Mozilla\Firefox\Profiles\fcbei8vp.teleScrape')
    PATH = "C:\Program Files (x86)\geckodriver.exe"
    driver = webdriver.Firefox(firefox_profile=myprofile ,executable_path=PATH)

    target = 3
    # Saham = ['AALI', 'ABBA', 'ABDA', 'ABMM', 'ACES', 'ACST', 'ADES', 'ADHI', 'ADMF', 'ADMG', 'ADRO', 'AGAR', 'AGII', 'AGRO', 'AGRS', 'AHAP', 'AIMS', 'AISA', 'AKKU', 'AKPI', 'AKRA', 'AKSI', 'ALDO', 'ALKA', 'ALMI', 'ALTO', 'AMAG', 'AMAN', 'AMAR', 'AMFG', 'AMIN', 'AMOR', 'AMRT', 'ANDI', 'ANJT', 'ANTM', 'APEX', 'APIC', 'APII', 'APLI', 'APLN', 'ARGO', 'ARII', 'ARKA', 'ARMY', 'ARNA', 'ARTA', 'ARTI', 'ARTO', 'ASBI', 'ASDM', 'ASGR', 'ASII', 'ASJT', 'ASMI', 'ASPI', 'ASRI', 'ASRM', 'ASSA', 'ATAP', 'ATIC', 'AUTO', 'AYLS', 'BABP', 'BACA', 'BAJA', 'BALI', 'BANK', 'BAPA', 'BAPI', 'BATA', 'BAYU', 'BBCA', 'BBHI', 'BBKP', 'BBLD', 'BBMD', 'BBNI', 'BBRI', 'BBRM', 'BBSI', 'BBSS', 'BBTN', 'BBYB', 'BCAP', 'BCIC', 'BCIP', 'BDMN', 'BEBS', 'BEEF', 'BEKS', 'BELL', 'BESS', 'BEST', 'BFIN', 'BGTG', 'BHAT', 'BHIT', 'BIKA', 'BIMA', 'BINA', 'BIPI', 'BIPP', 'BIRD', 'BISI', 'BJBR', 'BJTM', 'BKDP', 'BKSL', 'BKSW', 'BLTA', 'BLTZ', 'BLUE', 'BMAS', 'BMRI', 'BMSR', 'BMTR', 'BNBA', 'BNBR', 'BNGA', 'BNII', 'BNLI', 'BOGA', 'BOLA', 'BOLT', 'BOSS', 'BPFI', 'BPII', 'BPTR', 'BRAM', 'BRIS', 'BRMS', 'BRNA', 'BRPT', 'BSDE', 'BSIM', 'BSSR', 'BSWD', 'BTEK', 'BTEL', 'BTON', 'BTPN', 'BTPS', 'BUDI', 'BUKK', 'BULL', 'BUMI', 'BUVA', 'BVIC', 'BWPT', 'BYAN', 'CAKK', 'CAMP', 'CANI', 'CARE', 'CARS', 'CASA', 'CASH', 'CASS', 'CBMF', 'CCSI', 'CEKA', 'CENT', 'CFIN', 'CINT', 'CITA', 'CITY', 'CLAY', 'CLEO', 'CLPI', 'CMNP', 'CMPP', 'CNKO', 'CNTX', 'COCO', 'COWL', 'CPIN', 'CPRI', 'CPRO', 'CSAP', 'CSIS', 'CSMI', 'CSRA', 'CTBN', 'CTRA', 'CTTH', 'DADA', 'DART', 'DAYA', 'DCII', 'DEAL', 'DEFI', 'DEWA', 'DFAM', 'DGIK', 'DGNS', 'DIGI', 'DILD', 'DIVA', 'DKFT', 'DLTA', 'DMAS', 'DMMX', 'DMND', 'DNAR', 'DNET', 'DOID', 'DPNS', 'DPUM', 'DSFI', 'DSNG', 'DSSA', 'DUCK', 'DUTI', 'DVLA', 'DWGL', 'DYAN', 'EAST', 'ECII', 'EDGE', 'EKAD', 'ELSA', 'ELTY', 'EMDE', 'EMTK', 'ENRG', 'ENVY', 'ENZO', 'EPAC', 'EPMT', 'ERAA', 'ERTX', 'ESIP', 'ESSA', 'ESTA', 'ESTI', 'ETWA', 'EXCL', 'FAPA', 'FAST', 'FASW', 'FILM', 'FINN', 'FIRE', 'FISH', 'FITT', 'FMII', 'FOOD', 'FORU', 'FORZ', 'FPNI', 'FREN', 'FUJI', 'GAMA', 'GDST', 'GDYR', 'GEMA', 'GEMS', 'GGRM', 'GGRP', 'GHON', 'GIAA', 'GJTL', 'GLOB', 'GLVA', 'GMFI', 'GMTD', 'GOLD', 'GOLL', 'GOOD', 'GPRA', 'GSMF', 'GTBO', 'GWSA', 'GZCO', 'HADE', 'HDFA', 'HDIT', 'HDTX', 'HEAL', 'HELI', 'HERO', 'HEXA', 'HITS', 'HKMU', 'HMSP', 'HOKI', 'HOME', 'HOMI', 'HOTL', 'HRME', 'HRTA', 'HRUM', 'IATA', 'IBFN', 'IBST', 'ICBP', 'ICON', 'IDPR', 'IFII', 'IFSH', 'IGAR', 'IIKP', 'IKAI', 'IKAN', 'IKBI', 'IMAS', 'IMJS', 'IMPC', 'INAF', 'INAI', 'INCF', 'INCI', 'INCO', 'INDF', 'INDO', 'INDR', 'INDS', 'INDX', 'INDY', 'INKP', 'INOV', 'INPC', 'INPP', 'INPS', 'INRU', 'INTA', 'INTD', 'INTP', 'IPCC', 'IPCM', 'IPOL', 'IPTV', 'IRRA', 'ISAT', 'ISSP', 'ITIC', 'ITMA', 'ITMG', 'JAST', 'JAWA', 'JAYA', 'JECC', 'JGLE', 'JIHD', 'JKON', 'JKSW', 'JMAS', 'JPFA', 'JRPT', 'JSKY', 'JSMR', 'JSPT', 'JTPE', 'KAEF', 'KARW', 'KAYU', 'KBAG', 'KBLI', 'KBLM', 'KBLV', 'KBRI', 'KDSI', 'KEEN', 'KEJU', 'KIAS', 'KICI', 'KIJA', 'KINO', 'KIOS', 'KJEN', 'KKGI', 'KLBF', 'KMDS', 'KMTR', 'KOBX', 'KOIN', 'KONI', 'KOPI', 'KOTA', 'KPAL', 'KPAS', 'KPIG', 'KRAH', 'KRAS', 'KREN', 'LAND', 'LAPD', 'LCGP', 'LCKM', 'LEAD', 'LIFE', 'LINK', 'LION', 'LMAS', 'LMPI', 'LMSH', 'LPCK', 'LPGI', 'LPIN', 'LPKR', 'LPLI', 'LPPF', 'LPPS', 'LRNA', 'LSIP', 'LTLS', 'LUCK', 'MABA', 'MAGP', 'MAIN', 'MAMI', 'MAPA', 'MAPB', 'MAPI', 'MARI', 'MARK', 'MASA', 'MAYA', 'MBAP', 'MBSS', 'MBTO', 'MCAS', 'MCOR', 'MDIA', 'MDKA', 'MDKI', 'MDLN', 'MDRN', 'MEDC', 'MEGA', 'MERK', 'META', 'MFIN', 'MFMI', 'MGNA', 'MGRO', 'MICE', 'MIDI', 'MIKA', 'MINA', 'MIRA', 'MITI', 'MKNT', 'MKPI', 'MLBI', 'MLIA', 'MLPL', 'MLPT', 'MMLP', 'MNCN', 'MOLI', 'MPMX', 'MPOW', 'MPPA', 'MPRO', 'MRAT', 'MREI', 'MSIN', 'MSKY', 'MTDL', 'MTFN', 'MTLA', 'MTPS', 'MTRA', 'MTSM', 'MTWI', 'MYOH', 'MYOR', 'MYRX', 'MYTX', 'NASA', 'NATO', 'NELY', 'NFCX', 'NICK', 'NIKL', 'NIPS', 'NIRO', 'NISP', 'NOBU', 'NRCA', 'NUSA', 'NZIA', 'OASA', 'OCAP', 'OKAS', 'OMRE', 'OPMS', 'PADI', 'PALM', 'PAMG', 'PANI', 'PANR', 'PANS', 'PBID', 'PBRX', 'PBSA', 'PCAR', 'PDES', 'PEGE', 'PEHA', 'PGAS', 'PGJO', 'PGLI', 'PGUN', 'PICO', 'PJAA', 'PKPK', 'PLAN', 'PLAS', 'PLIN', 'PMJS', 'PMMP', 'PNBN', 'PNBS', 'PNGO', 'PNIN', 'PNLF', 'PNSE', 'POLA', 'POLI', 'POLL', 'POLU', 'POLY', 'POOL', 'PORT', 'POSA', 'POWR', 'PPGL', 'PPRE', 'PPRO', 'PRAS', 'PRDA', 'PRIM', 'PSAB', 'PSDN', 'PSGO', 'PSKT', 'PSSI', 'PTBA', 'PTDU', 'PTIS', 'PTPP', 'PTPW', 'PTRO', 'PTSN', 'PTSP', 'PUDP', 'PURA', 'PURE', 'PURI', 'PWON', 'PYFA', 'PZZA', 'RAJA', 'RALS', 'RANC', 'RBMS', 'RDTX', 'REAL', 'RELI', 'RICY', 'RIGS', 'RIMO', 'RISE', 'RMBA', 'ROCK', 'RODA', 'RONY', 'ROTI', 'RUIS', 'SAFE', 'SAME', 'SAMF', 'SAPX', 'SATU', 'SBAT', 'SCCO', 'SCMA', 'SCNP', 'SCPI', 'SDMU', 'SDPC', 'SDRA', 'SFAN', 'SGER', 'SGRO', 'SHID', 'SHIP', 'SIDO', 'SILO', 'SIMA', 'SIMP', 'SINI', 'SIPD', 'SKBM', 'SKLT', 'SKRN', 'SKYB', 'SLIS', 'SMAR', 'SMBR', 'SMCB', 'SMDM', 'SMDR', 'SMGR', 'SMKL', 'SMMA', 'SMMT', 'SMRA', 'SMRU', 'SMSM', 'SOCI', 'SOFA', 'SOHO', 'SONA', 'SOSS', 'SOTS', 'SPMA', 'SPTO', 'SQMI', 'SRAJ', 'SRIL', 'SRSN', 'SRTG', 'SSIA', 'SSMS', 'SSTM', 'STAR', 'STTP', 'SUGI', 'SULI', 'SUPR', 'SURE', 'SWAT', 'TALF', 'TAMA', 'TAMU', 'TARA', 'TAXI', 'TBIG', 'TBLA', 'TBMS', 'TCID', 'TCPI', 'TDPM', 'TEBE', 'TECH', 'TELE', 'TFAS', 'TFCO', 'TGKA', 'TGRA', 'TIFA', 'TINS', 'TIRA', 'TIRT', 'TKIM', 'TLKM', 'TMAS', 'TMPO', 'TNCA', 'TOBA', 'TOPS', 'TOTL', 'TOTO', 'TOWR', 'TOYS', 'TPIA', 'TPMA', 'TRAM', 'TRIL', 'TRIM', 'TRIN', 'TRIO', 'TRIS', 'TRJA', 'TRST', 'TRUK', 'TRUS', 'TSPC', 'TUGU', 'TURI', 'UANG', 'UCID', 'UFOE', 'ULTJ', 'UNIC', 'UNIQ', 'UNIT', 'UNSP', 'UNTR', 'UNVR', 'URBN', 'VICI', 'VICO', 'VINS', 'VIVA', 'VOKS', 'VRNA', 'WAPO', 'WEGE', 'WEHA', 'WICO', 'WIFI', 'WIIM', 'WIKA', 'WINS', 'WMUU', 'WOMF', 'WOOD', 'WOWS', 'WSBP', 'WSKT', 'WTON', 'YELO', 'YPAS', 'YULE', 'ZBRA', 'ZINC', 'ZONE']
    Saham = ['AALI', 'ABBA', 'ABDA', 'ABMM', 'ACES', 'ACST', 'ADES', 'ADHI', 'ADMF', 'ADMG', 'ADRO', 'AGII', 'AGRO', 'AGRS', 'AHAP', 'AIMS', 'AISA', 'AKKU', 'AKPI', 'AKRA', 'AKSI', 'ALDO', 'ALKA' 'ALMI', 'ALTO', 'AMAG', 'AMFG', 'AMOR', 'AMRT', 'ANJT', 'ANTM', 'APEX', 'APIC', 'APII', 'APLI', 'APLN', 'ARGO', 'ARII', 'ARKA', 'ARNA', 'ARTA', 'ARTO', 'ASBI', 'ASDM', 'ASGR', 'ASII', 'ASJT', 'ASMI', 'ASPI', 'ASRI', 'ASRM', 'ASSA', 'ATIC', 'AYLS', 'BABP', 'BAPI', 'BBCA', 'BBHI', 'BBKP', 'BBLD', 'BBMD', 'BBNI', 'BBRI', 'BBRM', 'BBSI', 'BBSS', 'BBTN', 'BBYB', 'BCAP', 'BCIC', 'BCIP', 'BDMN', 'BEKS', 'BESS', 'BFIN', 'BGTG', 'BHAT', 'BHIT', 'BIKA', 'BIMA', 'BIPI', 'BIPP', 'BISI', 'BJBR', 'BJTM', 'BKDP', 'BKSL', 'BKSW', 'BLTA', 'BLTZ', 'BMAS', 'BMRI', 'BMSR', 'BMTR', 'BNBA', 'BNBR', 'BNGA', 'BNII', 'BNLI', 'BPFI', 'BPII', 'BPTR', 'BRAM', 'BRIS', 'BRMS', 'BRNA', 'BRPT', 'BSDE', 'BSIM', 'BSSR', 'BSWD', 'BTEK', 'BTEL', 'BTON', 'BTPN', 'BTPS', 'BUKK', 'BUVA', 'BVIC', 'BWPT', 'BYAN', 'CAKK', 'CANI', 'CASA', 'CASS', 'CBMF', 'CCSI', 'CEKA','CENT', 'CFIN', 'CINT', 'CITA', 'CLAY', 'CLEO', 'CLPI', 'CMNP', 'CMPP', 'CNKO', 'CNTX', 'COCO', 'COWL', 'CPIN', 'CPRI', 'CPRO', 'CSAP', 'CSIS', 'CSMI', 'CSRA', 'CTBN', 'CTRA', 'CTTH', 'DART', 'DCII', 'DEFI', 'DFAM', 'DGIK', 'DGNS', 'DIGI', 'DILD', 'DIVA', 'DKFT', 'DLTA', 'DMAS', 'DMMX', 'DMND', 'DNAR', 'DNET', 'DOID', 'DPNS', 'DPUM', 'DSFI', 'DSNG', 'DSSA', 'DUCK', 'DUTI', 'DVLA', 'DWGL', 'ECII', 'EKAD', 'ELSA', 'ELTY', 'EMDE', 'EMTK', 'ENRG', 'ENVY', 'ENZO', 'EPAC', 'EPMT', 'ERAA', 'ERTX', 'ESIP', 'ESSA', 'ESTA', 'ESTI', 'ETWA', 'EXCL', 'FAPA', 'FASW', 'FILM', 'FINN', 'FIRE', 'FISH', 'FITT', 'FMII', 'FORU', 'FORZ', 'FPNI', 'FREN', 'FUJI', 'GAMA', 'GDST', 'GDYR', 'GEMS', 'GGRM', 'GGRP', 'GHON', 'GIAA', 'GJTL', 'GLOB', 'GLVA', 'GMFI', 'GMTD', 'GOLL', 'GPRA', 'GSMF', 'GTBO', 'GWSA', 'GZCO', 'HADE', 'HDFA', 'HDIT', 'HDTX', 'HKMU', 'HMSP', 'HOMI', 'HOTL', 'HRME', 'HRTA', 'HRUM', 'IATA', 'IBFN', 'IBST', 'ICBP', 'ICON', 'IDPR', 'IFII', 'IFSH', 'IGAR', 'IIKP', 'IKAI', 'IKBI', 'IMAS', 'IMJS', 'IMPC', 'INAF', 'INAI', 'INCF', 'INCI', 'INCO', 'INDF', 'INDR', 'INDS', 'INDX', 'INDY', 'INKP', 'INOV', 'INPC', 'INPP', 'INPS', 'INRU', 'INTA', 'INTD', 'INTP', 'IPCC', 'IPCM', 'IPOL', 'IPTV', 'IRRA', 'ISAT', 'ISSP', 'ITIC', 'ITMA', 'ITMG', 'JAST', 'JECC', 'JGLE', 'JIHD', 'JKON', 'JKSW', 'JMAS', 'JPFA', 'JRPT', 'JSKY', 'JSMR', 'JSPT', 'JTPE', 'KAEF', 'KARW', 'KBAG', 'KBLI', 'KBLM', 'KBLV', 'KBRI', 'KDSI', 'KEEN', 'KICI', 'KIJA', 'KINO', 'KIOS', 'KJEN', 'KKGI', 'KLBF', 'KMDS', 'KMTR', 'KOBX', 'KOIN', 'KONI', 'KPAL', 'KPAS', 'KPIG', 'KRAH', 'KRAS', 'KREN', 'LAPD', 'LCGP', 'LCKM', 'LMAS', 'LMPI', 'LMSH', 'LPCK', 'LPGI', 'LPIN', 'LPKR', 'LPLI', 'LPPF', 'LPPS', 'LRNA', 'LSIP', 'LTLS', 'MAGP', 'MAPA', 'MAPB', 'MAPI', 'MARK', 'MBAP', 'MBSS', 'MBTO', 'MCAS', 'MCOR', 'MDIA', 'MDKA', 'MDKI', 'MDLN', 'MDRN', 'MEDC', 'MEGA', 'META', 'MFIN', 'MFMI', 'MGNA', 'MGRO', 'MICE', 'MIDI', 'MIKA', 'MINA', 'MIRA', 'MITI', 'MKNT', 'MKPI', 'MLBI', 'MLIA', 'MLPL', 'MLPT', 'MMLP', 'MNCN', 'MOLI', 'MPMX', 'MPOW', 'MPPA', 'MPRO', 'MRAT', 'MREI', 'MSIN', 'MSKY', 'MTDL', 'MTFN', 'MTLA', 'MTPS', 'MTRA', 'MTSM', 'MTWI', 'MYOH', 'MYOR', 'MYRX', 'MYTX', 'NELY', 'NFCX', 'NICK', 'NIKL', 'NIPS', 'NIRO', 'NISP', 'NOBU', 'NRCA', 'NZIA', 'OASA', 'OCAP', 'OKAS', 'OMRE', 'OPMS', 'PAMG', 'PANI', 'PANR', 'PANS', 'PBID', 'PBRX', 'PBSA', 'PCAR', 'PDES', 'PEGE', 'PEHA', 'PGAS', 'PGJO', 'PGLI', 'PGUN', 'PICO', 'PJAA', 'PKPK', 'PLAS', 'PLIN', 'PMJS', 'PMMP', 'PNBN', 'PNBS', 'PNGO', 'PNIN', 'PNLF', 'PNSE', 'POLI', 'POLL', 'POLU', 'POLY', 'POSA', 'POWR', 'PPGL', 'PPRE', 'PPRO', 'PRAS', 'PRDA', 'PRIM', 'PSAB', 'PSDN', 'PSGO', 'PSKT', 'PSSI', 'PTBA', 'PTDU', 'PTIS', 'PTPP', 'PTPW', 'PTRO', 'PTSN', 'PTSP', 'PUDP', 'PWON', 'PYFA', 'PZZA', 'RALS', 'RANC', 'RBMS', 'RDTX', 'RELI', 'RICY', 'RIGS', 'RIMO', 'RMBA', 'RONY', 'RUIS', 'SAME', 'SAMF', 'SAPX', 'SBAT', 'SCCO', 'SCMA', 'SCNP', 'SCPI', 'SDMU', 'SDPC', 'SDRA', 'SFAN', 'SGER', 'SGRO', 'SHID', 'SHIP', 'SIDO', 'SILO', 'SIMA', 'SIMP', 'SIPD', 'SKBM', 'SKLT', 'SKRN', 'SKYB', 'SLIS', 'SMAR', 'SMBR', 'SMCB', 'SMDM', 'SMDR', 'SMGR', 'SMKL', 'SMMA', 'SMMT', 'SMRA', 'SMRU', 'SMSM', 'SOCI', 'SOFA', 'SOHO', 'SONA', 'SOSS', 'SOTS', 'SPMA', 'SPTO', 'SQMI', 'SRAJ', 'SRIL', 'SRSN', 'SRTG', 'SSIA', 'SSMS', 'SSTM', 'STTP', 'SUGI', 'SULI', 'SUPR', 'TALF', 'TAMA', 'TARA', 'TBIG', 'TBLA', 'TBMS', 'TCID', 'TCPI', 'TDPM', 'TEBE', 'TELE', 'TFAS', 'TFCO', 'TGKA', 'TGRA', 'TIFA', 'TINS', 'TIRA', 'TIRT', 'TKIM', 'TLKM', 'TMAS', 'TMPO', 'TNCA', 'TOBA', 'TOPS', 'TOTL', 'TOTO', 'TOWR', 'TOYS', 'TPIA', 'TPMA', 'TRAM', 'TRIL', 'TRIN', 'TRIS', 'TRJA', 'TRST', 'TSPC', 'TURI', 'UCID', 'UFOE', 'ULTJ', 'UNIC', 'UNIQ', 'UNSP', 'UNTR', 'UNVR', 'URBN', 'VICI', 'VICO', 'VINS', 'VIVA', 'VOKS', 'VRNA', 'WAPO', 'WEGE', 'WEHA', 'WICO', 'WIIM', 'WIKA', 'WINS', 'WMUU', 'WOMF', 'WOOD', 'WOWS', 'WSBP', 'WSKT', 'WTON', 'YELO', 'YPAS', 'YULE', 'ZBRA', 'ZINC']
    SahamAmbigu = ['AGAR', 'AKSI', 'AMAN', 'AMAR', 'AMIN', 'ANDI', 'ARMY', 'ARTI', 'ATAP', 'AUTO', 'BACA', 'BAJA', 'BALI', 'BANK', 'BAPA', 'BATA', 'BAYU', 'BEBS', 'BEEF', 'BELL', 'BEST', 'BINA', 'BIRD', 'BLUE', 'BOGA', 'BOLA', 'BOLT', 'BOSS', 'BUDI', 'BULL', 'BUMI', 'CAMP', 'CARE', 'CARS', 'CASH', 'CITY', 'DADA', 'DAYA', 'DEAL', 'DEWA','DYAN', 'EAST', 'EDGE', 'FAST', 'GOLD', 'GOOD', 'HEAL', 'HELI', 'HERO', 'HEXA', 'HITS', 'HOKI', 'HOME', 'IKAN', 'INDO', 'JAWA', 'JAYA', 'KAYU', 'KEJU', 'KIAS', 'KOPI', 'KOTA', 'LAND', 'LEAD', 'LIFE', 'LINK', 'LION', 'LUCK','MABA', 'MAIN', 'MAMI', 'MARI', 'MASA', 'MAYA', 'MERK', 'NASA', 'NATO', 'NUSA', 'PADI', 'PALM', 'PLAN', 'POLA', 'POOL', 'PORT', 'PURA', 'PURE', 'PURI', 'RAJA', 'REAL', 'RISE', 'ROCK', 'RODA', 'ROTI', 'SATU', 'SINI', 'STAR', 'SURE', 'SWAT', 'TAMU', 'TAXI','TECH', 'TRUK', 'TRIM', 'TRIO', 'TUGU', 'UANG', 'UNIT', 'WIFI', 'ZONE', 'TRUS', 'FOOD', 'SAFE', 'GEMA']
    indikasi = []
    with open('../indikasi.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for i in readCSV:
            indikasi.insert(len(indikasi),i[0])

    normalizad_word = pd.read_excel("../Normalisasi.xlsx")
    normalizad_word_dict = {}

    for index, row in normalizad_word.iterrows():
        if row[0] not in normalizad_word_dict:
            normalizad_word_dict[row[0]] = row[1]

    def normalized_term(document):
        document = document.split(' ')
        aaa = [normalizad_word_dict[term] if term in normalizad_word_dict else term for term in document]
        aaa = ' '.join(aaa)
        return(aaa)
    
    hari = 0
    tanggal2 = []
    tanggal = []
    itemss=[]
    percakapan = []
    # driver.get('https://web.telegram.org/#/im?p=@TheTradersGroup')
    driver.get('https://web.telegram.org/#/im?p=g579054022')
    # driver.get('https://web.telegram.org/#/im?p=@ilmucryptopro')
    time.sleep(20)
    temp = ''
    temp2 = ''
    first = True
    ptemp = ''
    wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
    chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
    psn = len(chat)
    Stoped = False
    tabung = []
    while True:
        joinn = False
        balas = ''
        penulis = ''
        last = penulis
        pesan2 = [""]
        jam = ''
        pesan2 = []
        # bisa = False
        # while not bisa:
        #     try :
        pesan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(psn)+"]")
        time.sleep(0.25)
        driver.execute_script("arguments[0].scrollIntoView(true);", pesan)
        psn -= 1
                # bisa = True
            # except :
            #     driver.execute_script("location.reload()")
            #     print('Masuk error')
            #     time.sleep(10)
            #     # driver.get('https://web.telegram.org/#/im?p=@ilmucryptopro')
            #     # time.sleep(20)
            #     # wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
            #     # chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
            #     # psn = len(chat)
            #     continue
        if (len(pesan.find_elements_by_xpath(".//a[@class='im_message_photo_thumb']")) > 0) :
            # print('ini adalah foto')
            penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
            gambar = pesan.find_element_by_xpath(".//img[@class='im_message_photo_thumb']").get_attribute('src')
            pesan4 = "photo"
            pesan2.insert(0, pesan4)
            if (len(pesan.find_elements_by_xpath(".//div[@class='im_message_photo_caption']")) > 0):
                last = pesan.find_element_by_xpath(".//div[@class='im_message_photo_caption']").text
                emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                for x in emo :
                    if(x.text.strip()!=''):
                        last = last.replace(x.text.strip(), ' ')
                pesan4 = pesan4 + last
                pesan2.insert(0, last)
            if (len(pesan.find_elements_by_xpath(".//div[@class='im_message_text']")) > 0):
                last = pesan.find_element_by_xpath(".//div[@class='im_message_text']").text
                emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                for x in emo :
                    if(x.text.strip()!=''):
                        last = last.replace(x.text.strip(), ' ')
                pesan4 = pesan4 + last
                pesan2.insert(0, last)
            jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
        elif (len(pesan.find_elements_by_xpath(".//span[@ng-switch-when='messageActionChatJoined']")) > 0):
            print('seseorang join')
            penulis = ''
            last = penulis
            pesan2 = [""]
            jam = ''
            joinn = True
            # print('Masuk2')
        elif (len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_split_text']")) > 0):
            if((len(pesan.find_elements_by_xpath(".//div[@class='im_message_date_split im_service_message_wrap' and @style='display: none;']")) > 0)):
                if(len(pesan.find_elements_by_xpath(".//div[@class='im_message_text']"))>0):
                    print('Ini juga sebenernya pesan biasa')
                    penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                    last = pesan.find_element_by_xpath(".//div[@class='im_message_text']").text
                    emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                    if (len(pesan.find_elements_by_xpath(".//div[@class='im_message_document_caption']"))>0):
                        last = last + pesan.find_element_by_xpath(".//div[@class='im_message_document_caption']").text
                    for x in emo :
                        if(x.text.strip()!=''):
                            last = last.replace(x.text.strip(), ' ')
                    pesan4 = last
                    pesan2.insert(0, pesan4)
                    try :
                        print('Masuk kesini kali2')
                        jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
                        if (jam == ''):
                            jamm2 = pesan.find_element_by_xpath(".//span[@class='im_message_date_text nocopy']")
                            jam = jam + jamm2.get_attribute('data-content')
                    except : 
                        print('Seperti nya masuk ke sini2')
                        jamm2 = pesan.find_element_by_xpath(".//span[@class='im_message_date_text nocopy']")
                        jam = jam + jamm2.get_attribute('data-content')
                    if(len(pesan.find_elements_by_xpath(".//span[@my-short-message='replyMessage']"))>0):
                        balas = pesan.find_element_by_xpath(".//span[@my-short-message='replyMessage']").text
                        emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                        for x in emo :
                            if(x.text.strip()!=''):
                                balas = balas.replace(x.text.strip(), ' ')
                        pesan2.insert(0,"Membalas : " + balas)
                else :
                    print('blong1')
            elif(len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_text nocopy']"))>0) :
                jamm2 = pesan.find_element_by_xpath(".//span[@class='im_message_date_text nocopy']")
                jam = jam + jamm2.get_attribute('data-content')
                if(len(pesan.find_elements_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]"))>0):
                    penulis = pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
                if(len(pesan.find_elements_by_xpath(".//div[@class='im_message_text']"))>0):
                    last = pesan.find_element_by_xpath(".//div[@class='im_message_text']").text
                else :
                    last = ''
                emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                for x in emo :
                    if(x.text.strip()!=''):
                        last = last.replace(x.text.strip(), ' ')
                pesan4 = last
                pesan2.insert(0, pesan4)
                if(len(pesan.find_elements_by_xpath(".//span[@my-short-message='replyMessage']"))>0):
                    balas = pesan.find_element_by_xpath(".//span[@my-short-message='replyMessage']").text
                    emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                    for x in emo :
                        if(x.text.strip()!=''):
                            balas = balas.replace(x.text.strip(), ' ')
                    pesan2.insert(0,"Membalas : " + balas)
                print("ini adalah tanggal")
                tgl = pesan.find_element_by_xpath(".//span[@class='im_message_date_split_text']").text
                tgl = tgl.replace(",","")
                print(tgl)
                for k in range(len(tanggal2)):
                    tanggal2[k]['Tanggal'] = tgl
                tanggal.extend(tanggal2)
                hari +=1
                belum = (hari!=target)
                print(len(tanggal))
                tanggal2 = []
            else :
                print('seseorang join')
                penulis = ''
                last = penulis
                pesan2 = [""]
                jam = ''
                joinn = True
        elif(len(pesan.find_elements_by_xpath(".//span[@ng-bind='::historyMessage.date | time']"))>0 or len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_text nocopy']"))>0) :
            print('ini adalah pesan biasa')
            penulis = penulis + pesan.find_element_by_xpath(".//a[contains(@class, 'im_message_author user_color_')]").text
            try :
                print('Masuk kesini kali')
                jam = jam + pesan.find_element_by_xpath(".//span[@ng-bind='::historyMessage.date | time']").text
                if (jam == ''):
                    jamm2 = pesan.find_element_by_xpath(".//span[@class='im_message_date_text nocopy']")
                    jam = jam + jamm2.get_attribute('data-content')
            except : 
                try:
                    print('Seperti nya masuk ke sini')
                    jamm2 = pesan.find_element_by_xpath(".//span[@class='im_message_date_text nocopy']")
                    jam = jam + jamm2.get_attribute('data-content')
                except :
                    print('seseorang join')
                    penulis = ''
                    last = penulis
                    pesan2 = [""]
                    jam = ''
                    joinn = True
            if(not joinn):
                last = pesan.find_element_by_xpath(".//div[@class='im_message_text']").text
                emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                for x in emo :
                    if(x.text.strip()!=''):
                        last = last.replace(x.text.strip(), ' ')
                pesan4 = last
                pesan2.insert(0, pesan4)
                if(len(pesan.find_elements_by_xpath(".//span[@my-short-message='replyMessage']"))>0):
                    balas = pesan.find_element_by_xpath(".//span[@my-short-message='replyMessage']").text
                    emo = pesan.find_elements_by_xpath(".//span[@class='emoji  emoji-spritesheet-0']")
                    for x in emo :
                        if(x.text.strip()!=''):
                            balas = balas.replace(x.text.strip(), ' ')
                    pesan2.insert(0,"Membalas : " + balas)
        else :
            print('seseorang join')
            penulis = ''
            last = penulis
            pesan2 = [""]
            jam = ''
            joinn = True









        pesan3 = "\n".join(pesan2)
        masuk = False
        stop = [",", ".", "#", "?", "*", "-"]
        cek = pesan3
        bahas = []
        bahasAmbigu = []
        for x in stop:
            cek = cek.replace(x, " ")
        # for x in pesan3:
        #     b = x.isascii()
        #     if not b:
        #         pesan3 = pesan3.replace(x, ' ')
        pesan3 = ascii(pesan3)
        pesan4 = ascii(pesan4)
        balas = ascii(balas)
        print('Jam sebelum berubah : ','|'+str(jam)+'|')
        if(jam=='' and not joinn):
            if(len(pesan.find_elements_by_xpath(".//span[@class='im_message_date_text nocopy']"))>0):
                jamm2 = pesan.find_element_by_xpath(".//span[@class='im_message_date_text nocopy']")
                jam = jam + jamm2.get_attribute('data-content')
            else :
                print('blong2')
        if('M' not in str(jam)):
            jam2 = 0
        elif(jam!=0) :
            jam2 = formatJam(jam)
        else : 
            jam2 = 0
        print('Temp sebelum berubah : ',temp)
        if(temp == '' and not first):
            temp = 0
        elif(isinstance(temp,str) and temp != '') :
            temp = formatJam(jam)
        elif(not isinstance(temp,int)) :
            temp = 0
        print('banding = ',temp,'<', jam2)
        print(joinn)
        print("ini adalah first = ", first)




        if((temp < jam2 or first) and not joinn):
            if (first):
                temp = jam2
                temp2 = jam2
            elif (temp2 == ''):
                temp2 = jam2
            if any(word in cek.upper().split() for word in Saham):
                masuk = True
            # if(penulis != ""):
            #     ptemp = penulis
            # else :
            #     penulis = ptemp
            if(penulis == ''):
                penulis = userNulll(driver, psn)
            isitabung = {
                'Penulis' : penulis,
                'Pesan3' : pesan3,
                'Cek' : cek,
                'Jam' : jam,
                'Balas' : balas,
                'Pesan4' : pesan4
            }
            tabung.append(isitabung)
            if (first == True):
                Stoped = True
        else :
            if(not joinn):
                Stoped = True
            else:
                Stoped = False

        if(Stoped) :
            if(tabung):
                tabung.reverse()
                for isi in tabung:
                    # bahas = [word for word in Saham if word in isi['Cek'].upper().split()]
                    bahas = [word for word in Saham if word in isi['Cek'].upper().split()]
                    bahasAmbigu = [word for word in SahamAmbigu if word in isi['Cek'].split()]
                    penulis = isi['Penulis']
                    masuk1 = False
                    masuk2 = False
                    masuk = False
                    cek = isi['Cek']
                    cek = cek.replace('nya', '')
                    cek = normalized_term(cek)
                    for x in penulis:
                        c = x.isascii()
                        if not c:
                            penulis = penulis.replace(x, ' ')
                    if any(word in cek.upper().split() for word in Saham):
                            masuk1 = True
                    elif any(word in cek.split() for word in SahamAmbigu):
                        masuk1 = True
                    if any(word.upper() in cek.upper().split() for word in indikasi):
                        masuk2 = True
                    if(masuk1 and masuk2):
                        masuk = True
                    if bahasAmbigu:
                        bahas.extend(bahasAmbigu)
                    bahas = ",".join(bahas)
                    print("Data : "+str(psn))
                    print("user : "+penulis)
                    print("Pesan : ",isi['Pesan3'])
                    print("Saham : "+bahas)
                    print("cek :",cek)
                    if(masuk):
                        predict = svm(isi['Pesan3'])
                    else:
                        predict = 'hapus'
                    print("Label : ",predict)
                    print("jam : " + isi['Jam'])
                    print('=======================================================')
                    ada = False
                    balas = isi['Balas']
                    print('Balas =',balas)
                    print('Percakapan =',percakapan)
                    perindex = 0
                    # counttt = 0
                    pesan4 = isi['Pesan4']
                    pesan4 = pesan4.replace('\n', ' ')
                    if(not percakapan and pesan4!=''):
                        print('Cakap1')
                        percakapan.append([pesan4])
                        perindex = 1
                        ada = True
                    elif(balas!='' and pesan4!='') :
                        for a in percakapan:
                            print('Sub percakapan =',a)
                            perindex2 = percakapan.index(a)
                            for b in a:
                                print('Sub a =',b+'||')
                                if(isi['Balas'] in b and isi['Balas']!=''):
                                    print('Cakap2')
                                    percakapan[perindex2].append(pesan4)
                                    perindex = perindex2 + 1
                                    ada = True
                    if(not ada and pesan4!=''):
                        print('Cakap3')
                        percakapan.append([pesan4])
                        perindex = percakapan.index([pesan4]) + 1






                        
                    exist = penulis in ratee.User.values
                    if(exist):
                        df1 = ratee[ratee['User']==penulis]
                        hit = df1.iloc[0]['Hit']
                        miss = df1.iloc[0]['Miss']
                        rate = df1.iloc[0]['Rate']
                        # print(exist)
                    else :
                        hit = 'No Record'
                        miss = 'No Record'
                        rate = 'No Record'
                    item = {
                        'User' : penulis,
                        'Pesan' : pesan4,
                        'Balas' : balas,
                        'Saham' : bahas,
                        'Label' : predict,
                        'Jam' : isi['Jam'],
                        'Hit' : str(hit),
                        'Miss' : str(miss),
                        'Rate' : str(rate),
                        'Percakapan' : str(perindex)
                    }
                    itemss.append(item)
                    # if(not pesan3==''):
                    #     emit('my response', item)
                    tanggal2.append(item)
                    penulis = ""
                    pesan2 = []
                    jam = ""
                    print('$$$$$$$$$$$$$$$$$$$$$$$$END OF FOR$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            if(itemss):
                # itemss.reverse()
                for it in itemss:
                    emit('my response', it)
            itemss=[]
            tabung = []
            # time.sleep(10)
            print('Temp sebelum masuk stop : ',temp)
            if (not first):
                if (temp2 != ''):
                    temp = temp2
            temp2 = ''
            # time.sleep(300)
            driver.execute_script("location.reload()")
            time.sleep(10)
            psn=0
            while psn==0:
                wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
                chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
                psn = len(chat)
            Stoped = False
            temp3 = 0
            while temp3 != psn:
                temp3 = psn
                pesan = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]/div["+str(psn)+"]")
                driver.execute_script("arguments[0].scrollIntoView(true);", pesan)
                print("************************************SCROLL***********************************************8")
                time.sleep(2)
                wrapper = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div[2]')
                chat = wrapper.find_elements_by_xpath(".//div[contains(@class, 'im_history_message_wrap')]")
                psn = len(chat)
        print('Jam di akhir = ',jam)
        print('Temp di akhir = ',temp)
        if (joinn and first):
            first = True
        else :
            first = False
if __name__ == '__main__':
    socketio.run(app)