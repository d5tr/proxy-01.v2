import random
from colorama import Fore
import requests
import time
import threading

print('''


██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗      ██████╗  ██╗  ██╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝     ██╔═████╗███║  ██║   ██║╚════██╗
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝█████╗██║██╔██║╚██║  ██║   ██║ █████╔╝
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝ ╚════╝████╔╝██║ ██║  ╚██╗ ██╔╝██╔═══╝ 
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║        ╚██████╔╝ ██║██╗╚████╔╝ ███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝         ╚═════╝  ╚═╝╚═╝ ╚═══╝  ╚══════╝
                                                                               
              Make by ---> @D_5TR
              Team ---> @ZER0ONE_01
              
[+] I hope USE THIS TOOL FOR CYBER SECURITY , NOT FOR SABOTAGE ...  

''')



prox = int(input(f"{Fore.BLUE}[{Fore.RED}!{Fore.BLUE}]How prox :"))

first = int(input('[!] Enter First Numbers :'))




for _ in range(prox):
    #random proxy @d_5tr

     ss = "1234567890"

     s1 = "".join(random.choice(ss) for _ in range(2))

     s2 = "".join(random.choice(ss) for _ in range(2))

     s3 = "".join(random.choice(ss) for _ in range(2))

     s4 = "".join(random.choice(ss) for _ in range(2))

     s5 = "".join(random.choice(ss) for _ in range(2))

     s6 = "".join(random.choice(ss) for _ in range(2))

     s7 = "".join(random.choice(ss) for _ in range(2))

     end = str(first)+'.'+str(s1)+str(s2)+'.'+str(s3)+str(s4)+'.'+str(s5)+str(s6)

     with open('proxy.txt','a') as s :
         s.write(end + '\n')

print(Fore.LIGHTBLUE_EX+'[+] Done Make >>',prox)
time.sleep(3)
print(Fore.WHITE+'[@] Wait Loding To Start Checker 1 ...')
time.sleep(3)
print('<--- START --->')
# part 2
file0 = open('proxy.txt','r')

files = file0.readlines()
# checker part 1 @d_5tr
for filex in files:
    filex = str(filex).strip()
    req = requests.get(f'https://ipinfo.io/{filex}').status_code

    if req == 200 :
        print(Fore.LIGHTGREEN_EX+'[+] Good Proxy >>>',filex)

        with open('good_proxy.txt','a') as good :
            good.write(filex + '\n')

    elif req == 404 :
        print(Fore.LIGHTRED_EX+'[-] Bad Proxy !!')

    else:
        print(Fore.YELLOW+'[?] know [?]')

# part 2
print(Fore.WHITE+'[@] Wait Loding To Start Checker 2 ... ')
time.sleep(3)

print('<--- Start --->')
#checker part 2 @d_5tr
r = requests.session()
proxy = open('good_proxy.txt', 'r').read().splitlines()

loghead = {
    'Host': 'www.instagram.com',
    'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64;rv: 87.0) Gecko / 20100101Firefox / 87.0',
    'Accept': '* / *',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'X-CSRFToken': 'aSII4PZ8OZZ2XBqYlNNHNFK1Z1BphCVC',
    'X-Instagram-AJAX': '192f05fecd26',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': 'hmac.AR3Mzj_5DgFkWcc9xROX8fYAkhy32oHrg7mOXQyg5w9rBHs7',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequestContent - Length: 274',
    'Origin': 'https//www.instagram.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.instagram.com/',
    'Cookie': 'ig_did=0DC19561-61BE-4A52-ADD1-03984BF455F6;mid=YBAnmQALAAHiYKh4a5RUSgw-ZvfH;ig_nrcb=1;shbid=5188;shbts=1617106294.4676127;rur=NAO;csrftoken=aSII4PZ8OZZ2XBqYlNNHNFK1Z1BphCVC',
    'TE': 'Trailers',

}


def chackproxy():
    while True:
        proxylist = []
        for pro in proxy:
            proxylist.append(pro)
            run = str(random.choice(proxylist))

        try:
            red = {
                'http': 'http://{}'.format(run),
                'https': 'https://{}'.format(run)

            }
            r.proxies = red
            url = 'https://www.instagram.com/accounts/login/ajax/'
            logdata = {
                "username": "d5tr",
                "enc_password": "#PWD_INSTAGRAM_BROWSER:10:1617281915:AWlQAJ21GW4F00dfy0iz65B+3w87lq0VbKAcWSK38AK/Hg14Vt46PRknmYCpn73XkhNZ3nnzKrAK4JiZ1n6aWVeEw8ZtOIbLjysr+xg8ak08toEiRqQclaXacD0E4pBwkCCym/P56dKNj8n4QNc=",

            }

            re = r.post(url, headers=loghead, data=logdata).text

            if ('"status":"ok"') in re:
                print(Fore.GREEN+'[+] GOOD PROXY --->', run)
                with open('good_proxy_part2.txt', 'a') as  good:
                    good.write(run + '\n')


            else:
                print(Fore.RED+'[-] BAD PROXY !!')


        except requests.exceptions.ConnectionError:
            print(Fore.RED+'[-] BAD PROXY !!')


thred = []

for i in range(prox):
    thred1 = threading.Thread(target=chackproxy)
    thred1.start()
    thred.append(thred1)

for x1 in thred:
    x1.join()


