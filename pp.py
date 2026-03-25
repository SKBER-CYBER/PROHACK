#▬▭▬▭▬▭▬▭[IMPORT]▬▭▬▭▬▭▬▭#
import os
import uuid
import base64
import datetime
import subprocess
import time
import httpx
import os,sys,re,time,json,mechanize,asyncio,aiohttp,requests,urllib.parse,bs4,string,faker,fake_email,random,uuid,hashlib,subprocess,platform,marshal,zlib,base64
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime,timedelta
from time import sleep as sp
#▬▭▬▭▬▭▬▭[INTERNET]▬▭▬▭▬▭▬▭#
try:
    requests.get("https://www.google.com", timeout=5)
except requests.exceptions.ConnectionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"\033[1;92m [•] \033[1;31;1mNo Internet Connection & Don't Try To Bypass")
    print(f"\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    sys.exit()
#▬▭▬▭▬▭▬▭[HELPER FUNCTIONS]▬▭▬▭▬▭▬▭#
def clear():
    os.system("clear")

def slow(text, speed=0.01):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()    
#▬▭▬▭▬▭▬▭[PYCURL]▬▭▬▭▬▭▬▭#
def py_curl(url):
    curl=pycurl.Curl()
    buffer=BytesIO()
    try:
        curl.setopt(curl.URL,url)
        curl.setopt(curl.WRITEDATA,buffer)
        curl.setopt(curl.SSL_VERIFYPEER,1)
        curl.setopt(curl.SSL_VERIFYHOST,2)
        curl.setopt(curl.CAINFO,certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"AN ERROR IN PY{e}"
    finally:
        curl.close()
    response_body=buffer.getvalue().decode('utf-8')
    return response_body
#▬▭▬▭▬▭▬▭[USER AGENT]▬▭▬▭▬▭▬▭#
ugenx=[]
ua=UserAgent()
def ugenxx():
    ualist=[ua.random for _ in range(10000)]
    return str(random.choice(ualist))
for xd in range(10000):
    rr=random.randint
    build_b=random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
    bl_typ=random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
    oppo=random.choice(["CPH2461","CPH2451","PCGM00","PBBM00","PFZM10","PGGM10","PECT30","PCHM10","PEAT00","PEYM00","PESM10","PFGM00"])
    infinix=random.choice(["Infinix X669C","Infinix X6823","Infinix X676C","Infinix X683","Infinix X689C","Infinix X6811","Infinix X612B","Infinix X6810","Infinix X665E"])
    redmi=random.choice(["2211133G","M2004J19C","22041219I","22101316UG","2209116AG","M2010J19SY","M2012K11C","Redmi Note 7","Redmi Note 8","Redmi Note 5"])
    um2=f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {oppo} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um1=f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {redmi} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um3=f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix} Build/{bl_typ}.{str(rr(120000,220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
    um4=f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,114))}.0.{str(rr(4900,5700))}.{str(rr(70,150))} Mobile Safari/537.36"
    ugenx.append(um2)
    ugenx.append(um3)
    ugenx.append(um1)
    ugenx.append(um4)
def ____useragent____():
    version=random.choice(['14','15','10','13','7.0.0','7.1.1','9','12','11','9.0','8.0.0','7.1.2','7.0','4','5','4.4.2','5.1.1','6.0.1','9.0.1'])
    model=random.choice(['1105','1107','15','3T','62A','6779','6833','7273','9A','A1','A1 5G','A1 Pro','A11','A11k','A11x','A12','A15','A15s','A16','A16e','A16k','A16s','A17','A17k','A18','A1i 5G','A1k','A1s','A1x','A2 5G','A25','A2x 5G','A3','A3 5G','A3 Pro 5G','A30','A31','A31c','A32','A33','A33m','A33t','A34','A35','A36','A37','A37t','A38','A39','A3s','A3x 5G','A4','A40','A400','A41','A42','A43','A44','A45','A46','A47','A48','A49','A5','A5 (2020)','A50','A51','A52','A53','A53 5G','A53m','A53s','A53s 5G','A54','A54 5G','A54s','A55','A55 5G','A55s 5G','A56','A56 5G','A57','A57 (2016)','A57 (2022)','A58','A58 5G','A59','A59 5G','A59m','A59s','A59t','A5S','A60','A7','A71','A71 (2018)','A71A','A72','A72n 5G','A73','A73 5G','A73t','A74','A74 5G','A76','A77','A77 5G','A77s','A77t','A78','A78 5G','A79','A79 5G','A79k','A79t','A7n','A7x','A8','A83','A83 (2018)','A83PRO','A83t','A85T','A9','A9 (2020)','A91','A92','A92s','A93','A93s','A94','A95','A96','A96 5G','A97','A98','A98 5G','A9x','AX5','AX5s','AX7','C1','CNM632','CNM652','CPH1114','CPH1235','CPH1427','CPH1451','CPH1615','CPH1664','CPH1869','CPH1927','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2535','CPH2551','CPH2553','CPH2557','CPH2569','CPH2573','CPH2579','CPH2581','CPH2583','CPH2585','CPH2589','CPH2591','CPH2599','CPH2603','CPH2605','CPH2607','CPH2609','CPH2611','CPH2613','CPH2617','CPH2619','CPH2621','CPH2625','CPH2629','CPH2631','CPH2637','CPH2639','CPH2641','CPH2643','CPH2661','CPH2663','CPH2665','CPH2667','CPH2669','CPH2681','CPH2683','CPH2687','CPH2843','CPH2931','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','CPH9977','f','F1','F1 Plus','F10','F11','F11 Pro','F11Pro','F15','F17','F17 Pro','F19','F19 Pro','F19 Pro Plus','F19s','F1s','F21 Pro','F21s Pro','F23 5G','F25 Pro 5G','F27 Pro+ 5G','F3','F3 Plus','F5','F5 Youth','F51','F61','F7','F9','F9 Pro','Find','Find 5','Find 5 Mini','Find 7','Find 7a','Find Clover','Find Melody','Find Muse','Find N','Find N 5G','Find N2','lFind N2 Flip','Find N3','Find N3 Flip','Find Way S','Find X','Find X Lamborghini','Find X2','Find X2 Lite','Find X2 Pro','Find X3','Find X3 Lite','Find X3 Neo','Find X3 Pro','Find X5','Find X5 Pro','Find X6','Find X6 Pro','Find X7','Find X7 Ultra','Find X7 Ultra SE','JLAJH6','Joy Plus','K1','K10','K10 5G','K10 Pro 5G','K10x','K11 5G','K11x 5G','K12 5G','K3','K5','K7','K7x','K9 5G','K9 Pro 5G','K9s','K9x','N1 Mini','N1T','N3','Neo','Neo 3','Neo 5','Neo 7','Neo 7s','Pad 2','Pad Air','Pad Air 2','Pad Neo','Pad WiFi','R10','R1001','R11','R11 Plus','R11plus','R11s','R11s Plus','R15','R15 Dream Mirror','R15 Neo','R15 Pro','R15x','R17','R17 Neo','R17 Pro','R1K','R1L','R1S','R1x','R2001','R2010','R2017','R3006','R5','R53','R6007','R7','R7 Lite','R7 Plus','R7 Plus F','R7005','R7007','R7s','R7s Plus','R7sm','R7st','R7t','R801','R805','R807','R811','R819','R819T','R8205','R8207','R823T','R829','R829T','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 11','Reno 11 Pro','Reno 12','Reno 12 5G','Reno 12 F 4G','Reno 12 F 5G','Reno 12 Pro 5G','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9','Reno 9 A','Reno 9 Pro','Reno 9 Pro+','Reno A','Reno Ace','Reno Ace 2','Reno K3','Reno Z','Reno10','Reno11','Reno2','RENO3','Reno4','Reno5','Reno8','Reno9','RX17 Neo','S1','S17','S3','S4','T29','Ulike 2','V5','V8821','Watch 2 46mm','Watch 41mm','Watch 46mm','X','x20','x22','X50Pro','X54','X9017','X907','Y15','Y21','Y3','Z1'])
    build=random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver=str(random.choice(range(77,577)))
    ver2=str(random.choice(range(57,77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
def ugen():
    rr=random.randint
    rc=random.choice
    versi_android=f"{rr(4,12)}.0.1"
    android_api_level=str(rr(5,14))
    versi_chrome=f"{rr(50,114)}.0.{rr(1111,4445)}.{rr(45,150)}"
    device_oppo=rc(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269"])
    device_vivo=rc(["vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935"])
    device_samsung=rc(["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
    device_xiaomi=rc(["Mi 11 Lite 5G","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","Mi 12T","MIX 4","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","Mi A3","Mi 6","MI MAX 2","Mi A4"])
    device_infinix=rc(["Infinix Zero 20","Infinix Zero X","Infinix Note 12","Infinix Note 11","Infinix Note 10 Pro","Infinix Hot 12","Infinix Hot 11S","Infinix Hot 11","Infinix Hot 10","Infinix Hot 10i","Infinix Smart 5","Infinix S5 Pro","Infinix S4","Infinix Note 8i","Infinix Note 8","Infinix Hot 9"])
    device_google=rc(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel 5a"])
    device_realme=rc(["RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185"])
    density=rc(["{density=3.0,width=720,height=1280};FB_FW/1;","{density=3.0,width=1080,height=1920};FB_FW/1;","{density=2.75,width=1080,height=2028};FB_FW/1;"])
    opk=rc(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
    oph=rc(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
    carrier=rc(["SomeCarrier","Telkomsel","XL","Indosat","Three"])
    letters=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    build=f"{rc(letters)}{rc(letters)}{rr(10,90)}{rc(letters)}"
    fbbv=rr(881000000,998999999)
    ua_templates=[]
    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Samsung;FBBD/Samsung;FBPN/{opk};FBDV/{device_samsung};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )
    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/{opk};FBDV/{device_xiaomi};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )
    ua_templates.append(
        f"Dalvik/2.1.0 (Linux; U; Android {android_api_level}; {device_realme} Build/QP1A.{rr(111111,999999)}.{rr(111,999)}) {oph}/{rr(1,9)}"
    )
    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Infinix;FBBD/Infinix;FBPN/{opk};FBDV/{device_infinix};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )
    ua_templates.append(
        f"Mozilla/5.0 (Linux; Android {versi_android}; {device_google}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{rr(390,490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Google;FBBD/Google;FBPN/{opk};FBDV/{device_google};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]"
    )
    return rc(ua_templates)
pro=____useragent____()    
#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"\033[1;92m [•] \033[1;31;1mProhack Tool Is Not Allow Without Storage Permission");os.system('termux-setup-storage');os.system('clear');exit(f"{style} \033[1;32mRUN AGAIN : python Prohack.py")
#▬▭▬▭▬▭▬▭[TITLE]▬▭▬▭▬▭▬▭#
def clear():
	os.system('clear');print(logo)
sys.stdout.write('\x1b]2; MR OGGY\x07')
#▬▭▬▭▬▭▬▭[LOOP]▬▭▬▭▬▭▬▭#
oks,loop,ua,ussr,tw,cps,plist=[],0,[],[],[],[],[]
#▬▭▬▭▬▭▬▭[EXTRACTOR]▬▭▬▭▬▭▬▭#
def extractor(data):
    try:
        soup=BeautifulSoup(data,"html.parser")
        data={}
        for inputs in soup.find_all("input"):
            name=inputs.get("name")
            value=inputs.get("value")
            if name:
                data[name]=value
        return data
    except Exception as e:
        return {"error":str(e)}
#▬▭▬▭▬▭▬▭[FAKE NAME]▬▭▬▭▬▭▬▭#
def fake_philippines():
    first = Faker().first_name()
    last = Faker().last_name()
    return first,last
#▬▭▬▭▬▭▬▭[AUTO PASSWORD]▬▭▬▭▬▭▬▭#
random_password1=['magandaako','gandako','pogiako','pogiako123','gwapoako123','gwapoako','iloveyou','i love you','cuteko','cuteko123','cuteko143','mahal123','mahal143','iloveyou143','maganda123','maganda143','pogi123','pogi143']
random_password2=['nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
random_password3=['khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
random_password4=['afghan','afghan12345','Afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786','50006000']
random_password5=['Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire','57575751','57273200','i love you','iloveyou','59039200','708090']
random_password6=['57575751','57273200','i love you','iloveyou','59039200','708090']
def get_philippines_password():
    return random.choice(random_password1)
def get_nepal_password():
    return random.choice(random_password2)
def get_pakistan_password():
    return random.choice(random_password3)
def get_afghanistan_password():
    return random.choice(random_password4)
def get_bangladesh_password():
    return random.choice(random_password5)
def get_india_password():
    return random.choice(random_password6)
#▬▭▬▭▬▭▬▭[FAKE EMAIL]▬▭▬▭▬▭▬▭#
def get_temp_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domains = [
        'fexbox.org', 'fexpost.com', 'fextemp.com', 'mailto.plus',
        'merepost.com','rover.info','chitthi.in','any.pink','mailbox.in.ua'
    ]
    domain = random.choice(domains)
    return f"{name}@{domain}"

def GetEmail1():
    response=requests.post('https://api.internal.temp-mail.io/api/v3/email/new',timeout=15).json()
    return response['email']
#▬▭▬▭▬▭▬▭[FAKE EMAIL CODE]▬▭▬▭▬▭▬▭#
def get_temp_code(email):
    sess = requests.Session()
    headers = {
        "user-agent": "Mozilla/5.0 (Linux; Android 10; K)",
        "accept": "application/json",
        "cookie": f"email={email}"
    }
    url = f"https://tempmail.plus/api/mails?email={email}&limit=20&epin=&first_id=0"
    for _ in range(10):
        try:
            res = sess.get(url, headers=headers)
            data = res.json()
            if data.get("result") and data.get("mail_list"):
                for mail in data["mail_list"]:
                    subject = mail.get("subject", "")
                    body = mail.get("text", "")
                    code = re.search(r"\b(\d{4,8})\b", subject)
                    if code:
                        return code.group(1)
                    code = re.search(r"\b(\d{4,8})\b", body)
                    if code:
                        return code.group(1)
            time.sleep(2)
        except Exception:
            time.sleep(2)
    return None
def GetCode1(email):
    try:
        response=requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages',timeout=15).text
        code=re.search(r'FB-(\d+)', response).group(1)
        return code
    except:
        return None
#▬▭▬▭▬▭▬▭[SPECIAL LINE]▬▭▬▭▬▭▬▭#
def linex():
    print(f"\033[1;92m═════════════════════════════════════════")
#▬▭▬▭▬▭▬▭[LOGO]▬▭▬▭▬▭▬▭#
logo = ("""\033[1;92m    _          _
\033[1;92m     \\        /
\033[1;92m    __\\______/__
\033[1;92m    | [\033[1;31;1m©\033[1;92m]  [\033[1;31;1m©\033[1;92m] |​
 \033[1;92m   |  [\33[1;33m====\033[1;92m]  | [+] BANGLADESH CRACKER [+]
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mAuthor    :  \033[1;92m Mroggy              \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  :  \033[1;92m +8801917466867      \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mWhatsapp  : \033[1;92m  Mroggy404           \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mGroup Fb  :  \033[1;92m Termux Oggy World   \033[1;31;1m █
\033[1;31;1m█ \033[1;92m [•] \033[1;31;1mVersion   :  \033[1;92m 0.2                  \033[1;31;1m█
\033[1;92m╚═════════════════════════════════════════╝""")
#▬▭▬▭▬▭▬▭[APPROVAL]▬▭▬▭▬▭▬▭#
import os
import random
import subprocess
import requests
key_file="/sdcard/.oggy_key"
if os.path.exists(key_file):
    raw_key=open(key_file).read().strip()
else:
    uid=random.randint(10,99)
    hex_part=''.join(random.choices("ABCDEF0123456789",k=12))
    raw_key=f"OGGY-LOCK-UID{uid}-KEY2026-{hex_part}"
    open(key_file,"w").write(raw_key)
key_url="https://raw.githubusercontent.com/SKBER-CYBER/FFAB/main/Apprp.txt"
def approval():
    try:
        data=requests.get(key_url).text
        if raw_key in data:
            main_menu()
        else:
            buy_menu()
    except:
        print("No Internet")
        exit()
def buy_menu():
    os.system("clear")
    print(logo)
    print("\033[1;92m═════════════════════════════════════════")
    print("\033[1;92m👉YOUR KEY 👉",raw_key)
    print("\033[1;92m═════════════════════════════════════════")
    print("\033[1;92m👉WE SUPPORT PALESTINENS SAFE PALESTINENS")
    print("\033[1;92m═════════════════════════════════════════")
    print("\033[1;92m[👉] BUY PREMIUM LICENCE AND USE TOOL")
    print("\033[1;92m[👉] WHATSAPP NUMBER :- +8801917466867")
    print("\033[1;92m[👉] PROHACK TOOLS ALL FILE CLONING")
    print("\033[1;92m═════════════════════════════════════════")
    print("\033[1;92mMenu:")
    print("\033[1;92m     + File Cloning")
    print("\033[1;92m     + File Cloning")
    print("\033[1;92m     + File Cloning")
    print("\033[1;92m     + File Cloning")
    print("\033[1;92m     + Auto Cloning")
    print("\033[1;92m     + Random Cloning")
    print("\033[1;92m     1.If You Want To buy Key Inter & Open WhatsApp")
    print("\033[1;92m     + If You Already Buy.Key You Can Use Any Number ")
    print("\033[1;92m═════════════════════════════════════════")
    choice=input("Enter The Number To Run Targer( 1-7 or 'q' to quit) : ")
    if choice=="1":
        linex();name=input("\033[1;92m[👉] Enter Your Name 👉 ")
        msg=f"Hi Mr Oggy\nName : {name}\nKey : {raw_key}"
        url="https://api.whatsapp.com/send?phone=8801917466867&text="+msg
        subprocess.run(["am","start",url])
    elif choice=="2":
        exit()
    else:
        print("\033[1;91mWrong Option")
        exit()
#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def main_menu():
    print(f"\033[1;92m Welcome to James Prohack Tool ...");time.sleep(6);clear()
    print(f"\033[1;92m═════════════════════════════════════════")
    print(f"\033[1;92m👉WE SUPPORT PALESTINENS,SAFE PALESTINENS")
    print(f"\033[1;92m═════════════════════════════════════════")
    print(f"\033[1;92m[👉] BUY PREMIUM LICENCE AND USE TOOL ")
    print(f"\033[1;92m[👉] WHATSAPP NUMBER :- +8801917466867 ")
    print(f"\033[1;92m[👉] PROHACK TOOLS ALL FILE CLONING & CREATEING  ")
    print(f"\033[1;92m═════════════════════════════════════════")
    print(f"\033[1;92mMenu:")
    print(f"\033[1;92m     \033[1;92m  1.File Cloning ")
    print(f"\033[1;92m     \033[1;92m  2.File Cloning ")
    print(f"\033[1;92m     \033[1;92m  3.File Cloning ")
    print(f"\033[1;92m     \033[1;92m  4.File Cloning ")
    print(f"\033[1;92m     \033[1;92m  5.Auto Cloning ")
    print(f"\033[1;92m     \033[1;92m  6.Random Cloning ")
    print(f"\033[1;92m     \033[1;92m  + If You Want To buy Key Inter & Open WhatsApp")
    print(f"\033[1;92m     \033[1;92m  0.If You Already Buy.Key You Can Use Any Number  ")
    print(f"\033[1;92m═════════════════════════════════════════")
    hackpro = input("Enter The Number To Run Targer( 1-7 or 'q' to quit) : ")
    if hackpro == '1':
    	print("\033[1;92m[•] Coming Soon........!")
    elif hackpro =='2':
    	print("\033[1;92m[•] Coming Soon........!")
    elif hackpro =='3':
    	print("\033[1;92m[•] Coming Soon........!")
    elif hackpro =='4':
    	print("\033[1;92m[•] Coming Soon........!")
    elif hackpro =='5':
    	____create____()
    elif hackpro =='6':
    	print("\033[1;92m[•] Coming Soon........!")
    elif hackpro =='7':
    	os.system('xdg-open https://www.facebook.com/Oggy.fb')
    elif hackpro =='0':
    	sys.exit()
    else:
    	print("\033[1;92m [•] Invalid Choice!")
    	print("\033[1;92m [•] Run Again ")
#▬▭▬▭▬▭▬▭[CREATE MENU]▬▭▬▭▬▭▬▭#
def ____create____():
    global num_accounts
    clear();print(f'\033[1;92m [•] \033[1;31;1mEXAMPLE : \033[1;92m10000 20000 50000 99999');print(f"\033[1;92m═════════════════════════════════════════")
    try:num_accounts=int(input(f"\033[1;92m [•] \033[1;31;1mHOW MANY ACCOUNT NUMBER \033[1;37m:\033[1;92m "))
    except Exception:num_accounts=10
    clear();print(f"\033[1;92m═════════════════════════════════════════");print(f"\033[1;92m👉WE SUPPORT PALESTINENS,SAFE PALESTINENS");print(f"\033[1;92m═════════════════════════════════════════");print(f"\033[1;92m[👉] BUY PREMIUM LICENCE AND USE TOOL ");print(f"\033[1;92m[👉] WHATSAPP NUMBER :- +8801917466867 ");print(f"\033[1;92m[👉] PROHACK TOOLS ALL FILE CLONING & CREATEING  ");print(f"\033[1;92m═════════════════════════════════════════");print(f'\033[1;92m[01] AUTO PHILIPPINES PASSWORD');print(f'\033[1;92m[02] AUTO NEPAL PASSWORD');print(f'\033[1;92m[03] AUTO PAKISTAN PASSWORD');print(f'\033[1;92m[04] AUTO AFGHANISTAN PASSWORD');print(f'\033[1;92m[05] AUTO BANGLADESH PASSWORD');print(f'\033[1;92m[06] AUTO INDIA PASSWORD');print(f'\033[1;92m[07] CUSTOM PASSWORD');linex();password_country=input(f'\033[1;92m[•] \033[1;92mCHOOSE : ');linex()
    if password_country in ['G','g','07','7']:random_password=input('\033[1;92m[•]ENTER CUSTOM PASSWORD m: ');linex()
    print(f'''\033[1;92m[•]TOTAL CREATE LIMIT \033[1;92m: {num_accounts}''');print(f'''\033[1;92m[•]IF NO RESULT ON/OFF AIRPLANE MODE OR USE 1.1.1.1 VPN''');linex()
    for make in range(int(num_accounts)):
        make+1
        sys.stdout.write(f"\r\r\033[1;92m[OGGY]{make}/{num_accounts}|{'{:.1%}'.format(make/int(num_accounts))}]  OK[{len(oks)}] - CP[{len(cps)}]");sys.stdout.flush()
        ses=requests.Session()
        session=requests.Session()
        try:response=ses.get(url='https://x.facebook.com/reg',params={"_rdc":"1","_rdr":"","wtsid":"rdr_0t3qOXoIHbMS6isLw","refsrc":"deprecated"},timeout=20);mts=ses.get('https://x.facebook.com',timeout=20).text;m_ts=re.search(r'name="m_ts" value="(.*?)"',str(mts)).group(1)
        except Exception:m_ts=""
        formula=extractor(response.text)
        firstname,lastname=fake_philippines()
        domains=["gmail.com","yahoo.com","hotmail.com","outlook.com","proton.me","protonmail.com"]
        email2=f"{lastname.lower()}{firstname.lower()}@{random.choice(domains)}"
        if password_country in ['A','a','01','1']:random_password=get_philippines_password()
        elif password_country in ['B','b','02','2']:random_password=get_nepal_password()
        elif password_country in ['C','c','03','3']:random_password=get_pakistan_password()
        elif password_country in ['D','d','04','4']:random_password=get_afghanistan_password()
        elif password_country in ['E','e','05','5']:random_password=get_bangladesh_password()
        elif password_country in ['F','f','06','6']:random_password=get_india_password()
        payload={'ccp': "2",'reg_instance': str(formula["reg_instance"]),'submission_request': "true",'helper': "",'reg_impression_id': str(formula["reg_impression_id"]),'ns': "1",'zero_header_af_client': "",'app_id': "103",'logger_id': str(formula["logger_id"]),'field_names[0]': "firstname",'firstname': firstname,'lastname': lastname,'field_names[1]': "birthday_wrapper",'birthday_day': str(random.randint(1,28)),'birthday_month': str(random.randint(1,12)),'birthday_year': str(random.randint(1992,2009)),'age_step_input': "",'did_use_age': "false",'field_names[2]': "reg_email__",'reg_email__': email2,'field_names[3]': "sex",'sex': "2",'preferred_pronoun': "",'custom_gender': "",'field_names[4]': "reg_passwd__",'name_suggest_elig': "false",'was_shown_name_suggestions': "false",'did_use_suggested_name': "false",'use_custom_gender': "false",'guid': "",'pre_form_step': "",'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time()).split('.')[0],random_password),'submit': "Sign Up",'fb_dtsg': "NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0",'jazoest': str(formula["jazoest"]),'lsd': str(formula["lsd"]),'__dyn': "1ZaaAG1mxu1oz-l0BBBzEnxG6U4a2i5U4e0C8dEc8uwcC4o2fwcW4o3Bw4Ewk9E4W0pKq0FE6S0x81vohw5Owk8aE36wqEd8dE2YwbK0iC1qw8W0k-0jG3qaw4kwbS1Lw9C0le0ue0QU",'__csr': "",'__req': "p",'__fmt': "1",'__a': "AYkiA9jnQluJEy73F8jWiQ3NTzmH7L6RFbnJ_SMT_duZcpo2yLDpuVXfU2doLhZ-H1lSX6ucxsegViw9lLO6uRx31-SpnBlUEDawD_8U7AY4kQ",'__user': "0"}
        header1={"Host": "m.facebook.com","Connection": "keep-alive","Upgrade-Insecure-Requests": "1","User-Agent": pro,"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt": "1","X-Requested-With": "mark.via.gp","Sec-Fetch-Site": "none","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","dpr": "1.75","viewport-width": "980","sec-ch-ua": "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"","sec-ch-ua-mobile": "?1","sec-ch-ua-platform": "\"Android\"","sec-ch-ua-platform-version": "\"\"","sec-ch-ua-model": "\"\"","sec-ch-ua-full-version-list": "","sec-ch-prefers-color-scheme": "dark","Accept-Encoding": "gzip, deflate, br, zstd","Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
        reg_url='https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1'
        try:py_submit=ses.post(reg_url,data=payload,headers=header1,timeout=25)
        except Exception:continue
        if "c_user" in py_submit.cookies:
            first_cok=ses.cookies.get_dict()
            uid=str(first_cok['c_user'])
            header2={'authority': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','dpr': '2','referer': 'https://m.facebook.com/login/save-device/','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="125", "Google Chrome";v="125"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': pro,'viewport-width': '980'}
            params={'next': 'https://m.facebook.com/?deoia=1','soft': 'hjk'}
            try:con_sub=ses.get('https://x.facebook.com/confirmemail.php',params=params,headers=header2,timeout=20).text
            except Exception:con_sub=""
            valid=get_temp_code(email2)
            validd="NOT FOUND"
            if validd:confirm_id(email2,uid,validd,con_sub,ses,random_password)
            else:cps.append(email2)
        else:cps.append(email2)
    print("");linex();print(f"{style} \033[1;32mTHE PROCESS HAS BEEN COMPLETED");print(f"{style} \033[1;32mTOTAL OK \033[1;37m: \033[1;32m{len(oks)}\n{style} \033[1;31mTOTAL CP \033[1;37m: \033[1;31m{len(cps)}");linex();exit()
#▬▭▬▭▬▭▬▭[CONFIRM ID]▬▭▬▭▬▭▬▭#
def confirm_id(mail,uid,otp,data,ses,random_password):
    try:
        url="https://m.facebook.com/confirmation_cliff/"
        params={'contact': mail,'type': "submit",'is_soft_cliff': "false",'medium': "email",'code': otp}
        payload={'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0','jazoest': re.search(r'"\d+"', data).group().strip('"'),'lsd': re.search(r'"LSD",\[\],{"token":"([^"]+)"}',str(data)).group(1),'__dyn': "",'__csr': "",'__req': "4",'__fmt': "1",'__a': "",'__user': uid}
        headers={'User-Agent': pro,'Accept-Encoding': "gzip, deflate, br, zstd",'sec-ch-ua-full-version-list': "",'sec-ch-ua-platform': "\"Android\"",'sec-ch-ua': "\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",'sec-ch-ua-model': "\"\"",'sec-ch-ua-mobile': "?1",'x-asbd-id': "129477",'x-fb-lsd': "KnpjLz-YdSXR3zBqds98cK",'sec-ch-prefers-color-scheme': "light",'sec-ch-ua-platform-version': "\"\"",'origin': "https://m.facebook.com",'x-requested-with': "mark.via.gp",'sec-fetch-site': "same-origin",'sec-fetch-mode': "cors",'sec-fetch-dest': "empty",'referer': "https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk",'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",'priority': "u=1, i"}
        response=ses.post(url,params=params,data=payload,headers=headers,timeout=25)
        if "checkpoint" in str(response.url):           
            print(f"\r\033[1;31m[CP] {uid} | {random_password} [##]")
            cps.append(uid)
        else:
            cookie_string="; ".join(f"{k}={v}" for k, v in ses.cookies.get_dict().items())
            print(f"\r\033[1;92m[OK] {uid} | {random_password}  [Just Now]")
            print(f"\033[1;92m== \033[93mCookies \033[1;92m== {cookie_string}")
            try:open("/sdcard/MR-OGGY-COOKIE.txt","a").write(uid+"|"+random_password+"|"+otp+"|"+cookie_string+"\n");open("/sdcard/MR-OGGY-OK.txt","a").write(uid+"|"+random_password+"\n");open("/sdcard/MR-OGGY-EMAIL.txt","a").write(mail+"\n")
            except Exception:pass
            oks.append(uid)
    except Exception as e:pass
#▬▭▬▭▬▭▬▭[EXIT]▬▭▬▭▬▭▬▭#
if __name__ == "__main__":
    approval()