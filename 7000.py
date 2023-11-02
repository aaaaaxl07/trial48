from os import path
from urllib.request import urlopen
import os, sys, re, requests, bs4, time, random, json, string, uuid,base64,zlib,pip,urllib,urllib3
from bs4 import BeautifulSoup
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')

######METHOD PROTECT######
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;91m[!] ALL YOUR FILES WILL REMOVE IF YOU TRY AGAIN! ');exit()
        else:exit()
    except:exit()
####### MODULES KILLER #######
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
elif "open().write" in x:
	clr()
elif "write" in x:
	clr()
elif "logging.info" in x:
	clr()
elif "logging" in x:
	clr()
elif "printf" in x:
	clr()
elif "echo" in x:
	clr()
elif "os.system" in x:
	clr()
elif "system" in x:
	clr()
else:
    pass
from requests import sessions 
x = open(sessions.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
elif "open().write" in x:
	clr()
elif "write" in x:
	clr()
elif "logging.info" in x:
	clr()
elif "logging" in x:
	clr()
elif "printf" in x:
	clr()
elif "open" in x:
	clr()
elif "echo" in x:
	clr()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
elif "open().write" in x:
	clr()
elif "write" in x:
	clr()
elif "open" in x:
	clr()
elif "logging.info" in x:
	clr()
elif "printf" in x:
	clr()
elif "echo" in x:
	clr()
elif "system" in x:
	clr()
elif "os.system" in x:
	clr()
######METHOD PROTECTION END###### 

#Key1

def clear():
	os.system('clear')
def back():
	login()

ah="ALEX-"
imt="-GENERATOR=="
ak=" RPW-"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w')
	kok.write(myid+imt)
	kok.close()
def login():
	try:
		token = open('.token.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			public_menu()
		except KeyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo4)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		Public()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)

def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
ugen = []
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uas=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uas)

logo4 = """\33[1;32m

                 █████╗ ██╗  ██╗██╗     
                ██╔══██╗╚██╗██╔╝██║     
                ███████║ ╚███╔╝ ██║     
                ██╔══██║ ██╔██╗ ██║     
                ██║  ██║██╔╝ ██╗███████╗
                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
\33[1;32m-------------------------------------------------------- 
  Owner      :  Alexander Grayson
  Facebook   :  AlexanderGraysonRecovery.IAmLimitless
  Tool Type  :  RPW Facebook New Account Generator (Paid)
  Network    :  All Network
  Version    :  1.1
\33[1;32m--------------------------------------------------------"""
boy = ['Ethan Joseph', 'Benjamin Daniel', 'Aiden Michael', 'Liam Alexander', 'Andrew Joseph', 'Caleb Samuel', 'Jackson Benjamin', 'Matthew Benjamin', 'Daniel Joseph', 'Noah Samuel', 'Christopher Joseph', 'Samuel Benjamin', 'James Joseph', 'William Samuel', 'Logan Joseph', 'Michael Alexander', 'Nicholas Benjamin', 'Elijah Samuel', 'Henry Benjamin', 'Gabriel Joseph', 'Mason Samuel', 'David Joseph', 'Matthew Daniel', 'Daniel Christopher', 'Samuel Michael', 'Evan Benjamin', 'Liam Joseph', 'Alexander Benjamin', 'Andrew Samuel', 'Joseph Benjamin', 'Benjamin Michael', 'Caleb Christopher', 'Ethan Samuel', 'Nicholas Joseph', 'Aiden Benjamin', 'William Benjamin', 'Jackson Samuel', 'Daniel Michael', 'Christopher Samuel', 'Benjamin Alexander', 'Mason Joseph', 'Liam Christopher', 'Noah Benjamin', 'Logan Samuel', 'James Benjamin', 'Michael Benjamin', 'Elijah Joseph', 'David Benjamin', 'Henry Joseph', 'Gabriel Benjamin', 'Matthew Samuel','Liam Christopher', 'Benjamin Thomas', 'Elijah Alexander', 'Oliver James', 'William Joseph','Noah Daniel', 'Henry Benjamin', 'James Michael', 'Ethan Samuel', 'Samuel David','Daniel Andrew', 'Matthew Joseph', 'Joseph William', 'David Ethan', 'Andrew Thomas','Jackson William', 'Anthony Benjamin', 'Caleb Christopher', 'Dylan Samuel', 'Mason Michael','Christopher John', 'Benjamin Daniel', 'Aiden William', 'Owen Michael', 'Nathan James','Evan Daniel', 'Matthew Benjamin', 'Daniel Christopher', 'Logan James', 'William Benjamin','Ryan Joseph', 'Luke Samuel', 'Carter David', 'Oliver Henry', 'Jackson Daniel', 'Liam Michael','Gabriel William', 'Ethan Thomas', 'Andrew Joseph', 'Joseph Noah', 'Nicholas Thomas','Mason James', 'Benjamin Christopher', 'Samuel Christopher', 'Caleb Daniel', 'Henry James','David Alexander', 'Elijah Daniel', 'Anthony James', 'Daniel Joseph', 'Christopher David','Jackson Thomas','Ethan Parker', 'Liam Anderson', 'Mason Taylor', 'Aiden Mitchell', 'Lucas Bennett', 'Oliver Cooper', 'Carter Walker', 'Jackson Brooks', 'Noah Scott', 'Avery Foster', 'William Hayes', 'James Turner', 'Michael Bryant', 'Benjamin Carter', 'Daniel Russell', 'Alexander Parker', 'Matthew Foster', 'Henry Mitchell', 'Samuel Harrison', 'David Brooks', 'Joseph Anderson', 'John Davis', 'Nicholas Wright', 'Andrew Reed', 'Jonathan Stewart', 'Christopher Kelly', 'Gabriel Price', 'Caleb Butler', 'Nathaniel Hughes', 'Anthony Morgan', 'Nicholas Sullivan', 'Christopher Powell', 'Sebastian Price', 'Zachary Murphy', 'Matthew Bennett', 'Dominic Hill', 'William Ward', 'Isaac King', 'Landon Harrison', 'Eli Foster', 'Logan Turner', 'Luke Hayes', 'Owen Mitchell', 'Wyatt Cooper', 'Henry Reid', 'Elijah Anderson', 'William Turner', 'Samuel Bryant', 'Oliver Russell', 'Ethan Parker', 'Liam Anderson', 'Mason Taylor', 'Aiden Mitchell', 'Lucas Bennett', 'Oliver Cooper', 'Carter Walker', 'Jackson Brooks', 'Noah Scott', 'Avery Foster', 'William Hayes', 'James Turner', 'Michael Bryant', 'Benjamin Carter', 'Daniel Russell', 'Alexander Parker', 'Matthew Foster', 'Henry Mitchell', 'Samuel Harrison', 'David Brooks', 'Joseph Anderson', 'John Davis', 'Nicholas Wright', 'Andrew Reed', 'Jonathan Stewart', 'Christopher Kelly', 'Gabriel Price', 'Caleb Butler', 'Nathaniel Hughes', 'Anthony Morgan', 'Nicholas Sullivan', 'Christopher Powell', 'Sebastian Price', 'Zachary Murphy', 'Matthew Bennett', 'Dominic Hill', 'William Ward', 'Isaac King', 'Landon Harrison', 'Eli Foster', 'Logan Turner', 'Luke Hayes', 'Owen Mitchell', 'Wyatt Cooper', 'Henry Reid', 'Elijah Anderson', 'William Turner', 'Samuel Bryant', 'Oliver Russell',
'Henry Porter', 'Maxwell Gray', 'Theodore Baker', 'Harrison Carter', 'Ezra Foster', 'Nolan Thompson', 'Lincoln Adams', 'Miles Evans', 'Nathaniel Hayes', 'Julian Sullivan', 'Oliver Foster', 'Benjamin Griffin', 'Alexander Fisher', 'Wyatt Richards', 'Oscar Turner', 'Hudson Wright', 'Sebastian Knight', 'Landon Parker', 'Caleb Brooks', 'Eli Stewart', 'Lucas Harrison', 'Mason Reynolds', 'Owen Powell', 'Daniel Morgan', 'James Bennett', 'Matthew Walker', 'Ethan Reed', 'Logan Turner', 'Aiden Murphy', 'Nathaniel Turner', 'William Griffin', 'Samuel Hayes', 'Elijah Foster', 'Christopher Bryant', 'Avery Price', 'David Mitchell', 'Gabriel Evans', 'Jackson Parker', 'Joseph Adams', 'Liam Bennett', 'Michael Richards']

girl = ['Olivia Grace', 'Emma Rose', 'Ava Lily', 'Charlotte Faith', 'Sophia Hope', 'Amelia Joy', 'Mia Harper', 'Harper Violet', 'Evelyn Claire', 'Abigail Belle', 'Emily Grace', 'Elizabeth Faith', 'Sofia Jade', 'Ella Grace', 'Madison Faith', 'Scarlett Grace', 'Avery Faith', 'Mila Rose', 'Lily Joy', 'Chloe Grace', 'Aria Faith', 'Grace Olivia', 'Nora Emily', 'Riley Hope', 'Zoe Lily', 'Victoria Rose', 'Hazel Belle', 'Luna Claire', 'Aurora Grace', 'Penelope Faith', 'Nova Joy', 'Eleanor Rose', 'Emilia Grace', 'Elizabeth Belle', 'Stella Joy', 'Aubrey Grace', 'Camila Faith', 'Layla Rose', 'Hannah Joy', 'Lila Grace', 'Madelyn Faith', 'Paisley Rose', 'Skylar Belle', 'Bella Grace', 'Lucy Hope', 'Ariana Faith', 'Samantha Rose', 'Leah Grace', 'Violet Belle', 'Natalie Joy', 'Aaliyah Grace','Natalie Wren', 'Hannah Aurora', 'Emma Faye', 'Lily Seraphina', 'Grace Isabella','Aria Celeste', 'Zoe Harper', 'Mia Lila', 'Aubrey Elise', 'Olivia Jade','Luna Ivy', 'Sophia Rose', 'Ella Violet', 'Avery Maeve', 'Madison Skye','Charlotte Ruby', 'Aurora Belle', 'Evelyn Hazel', 'Layla Quinn', 'Nora Pearl','Eleanor Joy', 'Hailey Ruby', 'Aria Maeve', 'Stella Celestia', 'Mila Skye','Chloe Seraphina', 'Abigail Isabella', 'Ava Primrose', 'Victoria Grace', 'Penelope Celeste','Lily Violet', 'Hazel Seraphina', 'Amelia Faye', 'Lila Harper', 'Aria Belle','Sophia Quinn', 'Aubrey Pearl', 'Zoe Celestia', 'Olivia Grace', 'Luna Ivy','Ella Rose', 'Emma Wren', 'Mia Skye', 'Natalie Violet', 'Grace Seraphina','Charlotte Maeve', 'Stella Ruby', 'Aurora Isabella', 'Lily Harper', 'Evelyn Joy','Aria Grace', 'Luna Violet', 'Aurora Jade', 'Scarlett Evangeline', 'Mila Rose', 'Stella Celeste', 'Amara Seraphina', 'Layla Skye', 'Vivienne Elise', 'Eleanor Ruby', 'Hazel Quinn', 'Aveline Ivy', 'Isla Belle', 'Nora Hazel', 'Willow Joy', 'Athena Pearl', 'Lila Maeve', 'Sophia Harper', 'Olivia Celestia', 'Isabella Claire', 'Ella Primrose', 'Grace Seraphina', 'Chloe Aurora', 'Lily Juliet', 'Ariana Eloise', 'Amelia Hope', 'Emily Florence', 'Scarlett Belle', 'Victoria Sage', 'Madeline Faye', 'Cora Everly', 'Harper Luna', 'Evelyn Aurora', 'Aria Willow', 'Luna Grace', 'Aurora Mae', 'Stella Violet', 'Vivienne Rose', 'Mila Jade', 'Layla Quinn', 'Scarlett Elise', 'Hazel Ruby', 'Aveline Seraphina', 'Isla Skye', 'Nora Celeste', 'Willow Seraphina', 'Athena Ivy', 'Lila Belle', 'Sophia Pearl', 'Olivia Maeve', 'Aria Grace', 'Luna Violet', 'Aurora Jade', 'Scarlett Evangeline', 'Mila Rose', 'Stella Celeste', 'Amara Seraphina', 'Layla Skye', 'Vivienne Elise', 'Eleanor Ruby', 'Hazel Quinn', 'Aveline Ivy', 'Isla Belle', 'Nora Hazel', 'Willow Joy', 'Athena Pearl', 'Lila Maeve', 'Sophia Harper', 'Olivia Celestia', 'Isabella Claire', 'Ella Primrose', 'Grace Seraphina', 'Chloe Aurora', 'Lily Juliet', 'Ariana Eloise', 'Amelia Hope', 'Emily Florence', 'Scarlett Belle', 'Victoria Sage', 'Madeline Faye', 'Cora Everly', 'Harper Luna', 'Evelyn Aurora', 'Aria Willow', 'Luna Grace', 'Aurora Mae', 'Stella Violet', 'Vivienne Rose', 'Mila Jade', 'Layla Quinn', 'Scarlett Elise', 'Hazel Ruby', 'Aveline Seraphina', 'Isla Skye', 'Nora Celeste', 'Willow Seraphina', 'Athena Ivy', 'Lila Belle', 'Sophia Pearl', 'Olivia Maeve',
'Penelope Grace', 'Hannah Violet', 'Sophie Camille', 'Leah Isolde', 'Evangeline Jane', 'Cecilia Mae', 'Avery Isabella', 'Natalia Everly', 'Ruby Seraphina', 'Violet Quinn', 'Zara Celestia', 'Athena Elise', 'Delilah Rose', 'Harlow Seraphina', 'Lucy Evangeline', 'Nina Belle', 'Astrid Juliet', 'Eloise Skye', 'Gemma Pearl', 'Maeve Harper', 'Juliet Ivy', 'Bianca Celeste', 'Seraphina Elara', 'Arabella Faye', 'Emery Willow', 'Elowen Maeve', 'Wren Seraphina', 'Mabel Celeste', 'Rosalie Mae', 'Serena Quinn', 'Cordelia Pearl', 'Elsie Aurora', 'Adeline Jade', 'Lila Seraphina', 'Fiona Grace', 'Tessa Celestia', 'Genevieve Ivy', 'Estelle Ruby', 'Harper Violet']

def Subscription():
	key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
	clear()
	print(logo4)
	r1=str(urlopen("https://github.com/AlexGrayson-RPW/alex-approval/blob/main/approvalSheet.txt").read())
	if key1 in r1:
		os.system('clear')
		print(logo4)
	else:
		os.system("clear")
		print(logo4)
		print("\t \033[1;32m Please Get Approval First\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo4)
		print ("")
		print(" \033[1;32m Alexander Grayson's RPW Cloning Tool [Black Market] \033[1;37m\n")
		print(" \033[1;32m Note : THIS IS A PAID TOOL!   \033[1;37m")
		print ("")
		print(" [ Mode of Payment : GCASH ] ")
		print("")
		print(" Your key is not Approved. ")
		print("")
		print(" Copy and Send Key To Alexander Grayson")
		print ("")
		print (" Your Key : "+key1 )
		print ("")
		name = input(" Your Name : ")
		print ("")
		lol = input(" Your Email : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+key1
		os.system('am start https://m.me/AlexanderGraysonRecovery.IAmLimitless' + tks)
		Subscription()                                                                                 
Subscription()  

ok = []
cp = []
def menu():
    os.system('clear')
    print (logo4)
    print ('[1] New Account Generator')
    print (56*'-')
    sel = input('Select: ')
    if sel in['1', '01']:
        create().start()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] BRP Accounts')
        print ('[2] GRP Accounts')
        print (56*'-')
        gen = input('Choose: ')
        print (56*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example: 1000, 2000, 5000, 10000')
        print (56*'-')
        lim = int(input('Choose Quantity: '))
        os.system('clear')
        print (logo4)
        agent = random.choice(ugen)
        headers = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240","Google Chrome";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM) AppleWebKit/537.36 (KHTML%2C like Gecko) Silk/116.3.2 like Chrome/116.0.5845.187 Safari/537.36',
            'viewport-width': '980'
        }
        headers1 = {
            'authority': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.240","Google Chrome";v="116.0.5845.240"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM) AppleWebKit/537.36 (KHTML%2C like Gecko) Silk/116.3.2 like Chrome/116.0.5845.187 Safari/537.36'
        }
        print(' [•] Use airplane mode if no result. ')
        print(' [•] Use airplane mode if the result is all checkpoint accounts. ')
        print (56*'-')
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[ALEX-CREATING] {OO}{self.loop}/{str(lim)} | ALIVE: {len(ok)} | CHECKPOINT: {len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = random.choice(boy).split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = random.choice(girl).split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(11111,99999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://m.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://m.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://m.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;33m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://m.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;33m [CHECKPOINT] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m [ALEX-ALIVE] '+cok['c_user']+' | '+passw+' | '+coki+'\033[0;97m     ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (56*'-')
        print ('\033[1;32mTotal ids > ALIVE/' +str(len(ok)) + ' CHECKPOINT/' + str(len(cp)))
        print (56*'-')
        input('back')
        menu()
menu()
