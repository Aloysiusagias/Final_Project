from svm import svm
import csv
import pandas as pd
import json
from firebase import insertt
import pandas as pd
# from SQL import insertt


def respons(input_text):
    def ambil_penulis(dict, balas):
        # df = pd.DataFrame.from_dict(dict)
        if(not balas):
            isi_from = dict['message']['from']
        else :
            isi_from = dict['message']['reply_to_message']['from']
        first = isi_from['first_name']
        last = isi_from['last_name']
        penulis = first + " " + last
        return penulis
    
    def ambil_rating(user):
        rate = pd.read_csv('Rating.csv',index_col=0)
        a = rate[rate['User']==user]
        if(not a.empty):
            print(a)
            hit = a.iloc[0][1]
            miss = a.iloc[0][2]
            rating = a.iloc[0][3]
        else :
            hit = "No record"
            miss = "No record"
            rating = "No record"
        return {
            "hit" : hit,
            "miss" : miss,
            "rating" : rating
        }

        

    #Mengubah json menjadi dict
    penulis = 'kosong'
    text = str(input_text)
    text = text.replace("'", '"')
    text = text.replace("False","false")
    text = text.replace("True","true")
    dict = json.loads(text)
    print(dict)
    
    #Cek apakah membalas pesan
    if "reply_to_message" in dict['message'].keys():
        balas_user = ambil_penulis(dict, True)
        balas_pesan = dict['message']['reply_to_message']['text']
        balas_message_id = dict['message']['reply_to_message']['message_id']
    else :
        balas_user = '-'
        balas_pesan = '-'
        balas_message_id = '-'

    penulis = ambil_penulis(dict, False)
    teks = dict['message']['text']
    message_id = dict['message']['message_id']
    grup = dict['message']['chat']['title']
    grup = grup.replace(' ', '_')
    grup = grup.lower()
    

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
    masuk1 = False
    masuk2 = False
    masuk = False

    cek = normalized_term(teks)
    cek = cek.replace('nya', '')
    stop = [",", ".", "#", "?", "*", "-", "!", "@", "(", ")", "*", "&", "nya"]
    for x in stop:
        cek = cek.replace(x, " ")
    bahas = [word for word in Saham if word in cek.upper().split()]
    bahasAmbigu = [word for word in SahamAmbigu if word in cek.split()]
    indi = [word for word in indikasi if word in cek.lower().split()]

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


    if(masuk):
        predict = svm(teks)
    else:
        predict = 'Hapus'

    b = ambil_rating(penulis)
    hit = b["hit"]
    miss = b["miss"]
    rating = b["rating"]

    data = {}
    data['user'] = penulis
    data['pesan'] = teks
    data['prediksi'] = predict
    data['balas_user'] = balas_user
    data['balas_pesan'] = balas_pesan
    data['message_id'] = message_id
    data['balas_message_id'] = balas_message_id
    data['grup'] = grup
    data['hit'] = hit
    data['miss'] = miss
    data['rating_user'] = rating

    insertt(data)
    print("Penulis : ",penulis,"\nbalas_user : ",balas_user,"\nbalas_pesan : ",
    balas_pesan,"\nPrediksi : ",predict,"\nIndikasi : ", indi, "\nSaham : ",bahas,
    "\nGrup : ",grup,"\n=============================\n\n")