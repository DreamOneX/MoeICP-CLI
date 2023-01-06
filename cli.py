import requests
import sys
import re
from lxml import etree

# 初始化
ver = "1.0.0"
xname = "/html/body/div/div[2]/div/div/div[1]/div[2]/text()"
xnum = "/html/body/div/div[2]/div/div/div[5]/div[2]/text()"
xdomain = "/html/body/div/div[2]/div/div/div[2]/div[2]/text()"
xdesc = "/html/body/div/div[2]/div/div/div[4]/div[2]/text()"
xhome = "/html/body/div/div[2]/div/div/div[3]/div[2]/a/@href"
xowner = "/html/body/div/div[2]/div/div/div[6]/div[2]/text()"
xuptime = "/html/body/div/div[2]/div/div/div[7]/div[2]/text()"
xstatus = "/html/body/div/div[2]/div/div/div[8]/div[2]/text()"
xpic = "/html/head/meta[11]/@content"

def init():
    args = sys.argv[1]
    if args == "help":
        banner()
        helppage()
        sys.exit(0)
    elif args == "version":
        banner()
        print("\n", ver)
        sys.exit(0)

    # 判断是否输入了萌号/域名
    if len(sys.argv) > 2:
        num = sys.argv[2]
    else:
        num = input("请输入萌号/域名：")
    # 初始化爬虫
    url = "https://icp.gov.moe/?keyword=" + num
    headers = {
        'User-Agent': 'MoeICP-CLI/' + ver
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    global html
    html = etree.HTML(resp.text)
    # ~~屎山~~部分
    args = sys.argv[1]
    if args == "info":
        global needinfo
        needinfo = 1
        getname()
        getnumber()
        getdomain()
        getdescription()
        gethome()
        getowner()
        getuptime()
        getstatus()
        getpic()
        getinfo()
    elif args == "name":
        getname()
    elif args == "domain":
        getdomain()
    elif args == "desc":
        getdescription()
    elif args == "home":
        gethome()
    elif args == "owner":
        getowner()
    elif args == "uptime":
        getuptime()
    elif args == "status":
        getstatus()
    elif args == "number":
        getnumber()
    elif args == "pic":
        getpic()
    else:
        print("Invaid argment!")
        sys.exit(-1)

def getname():
    data = html.xpath(xname)
    if needinfo == 1:
        global xnametext
        xnametext = data[0]
    else:
        print(data[0])

def getnumber():
    data = html.xpath(xnum)
    text = data[0]
    compileint = re.compile('\d+')
    inttext = compileint.findall(text)
    if needinfo == 1:
        global xnumbertext
        xnumbertext = inttext[0]
    else:
        print(inttext[0])

def getdomain():
    data = html.xpath(xdomain)
    if needinfo == 1:
        global xdomaintext
        xdomaintext = data[0]
    else:
        print(data[0])

def getdescription():
    data = html.xpath(xdesc)
    if needinfo == 1:
        global xdescriptiontext
        xdescriptiontext = data[0]
    else:
        print(data[0])

def gethome():
    data = html.xpath(xhome)
    if needinfo == 1:
        global xhometext
        xhometext = data[0]
    else:
        print(data[0])

def getowner():
    data = html.xpath(xowner)
    if needinfo == 1:
        global xownertext
        xownertext = data[0]
    else:
        print(data[0])

def getuptime():
    data = html.xpath(xuptime)
    if needinfo == 1:
        global xuptimetext
        xuptimetext = data[0]
    else:
        print(data[0])

def getstatus():
    data = html.xpath(xstatus)
    if needinfo == 1:
        global xstatustext
        xstatustext = data[0]
    else:
        print(data[0])

def getpic():
    data = html.xpath(xpic)
    if needinfo == 1:
        global xpiclink
        xpiclink = data[0]
    else:
        print(data[0])

def banner():
    banner = '''
    ___  ___          _____ _____ ______       _____  _     _____ 
    |  \/  |         |_   _/  __ \| ___ \     /  __ \| |   |_   _|
    | .  . | ___   ___ | | | /  \/| |_/ /_____| /  \/| |     | |  
    | |\/| |/ _ \ / _ \| | | |    |  __/______| |    | |     | |  
    | |  | | (_) |  __/| |_| \__/\| |         | \__/\| |_____| |_ 
    \_|  |_/\___/ \___\___/ \____/\_|          \____/\_____/\___/ 
    '''
    print(banner)

def helppage():
    pass
    print("Usage of", sys.argv[0] + ":")
    print(sys.argv[0], "[参数 萌备或者域名]")
    print("  help    查看帮助")
    print("  version 查看当前版本")
    print("  name    查询萌备名称")
    print("  domain  查询萌备域名")
    print("  desc    查询萌备描述")
    print("  home    查询萌备主页")
    print("  owner   查询萌备所有者")
    print("  uptime  查询萌备更新时间")
    print("  status  查询萌备状态")
    print("  number  查询萌备萌号")
    print("  pic     获取萌备图片链接")
    print("\n例子:")
    print("     " + sys.argv[0] + " info")
    print("     " + sys.argv[0] + " info 20230000")
    print("     " + sys.argv[0] + " help")
    print("     " + sys.argv[0] + " version")

def getinfo():
    print("网站名称：", xnametext)
    print("网站域名：", xdomaintext)
    print("网站首页：", xhometext)
    print("网站信息：", xdescriptiontext)
    print("萌备案号：萌ICP备" + xnumbertext + "号")
    print("所有者：", xownertext)
    print("更新时间：", xuptimetext)
    print("状态：", xstatustext)
    print("图片链接：", xpiclink)
    sys.exit(0)

if __name__ == "__main__":
    init()