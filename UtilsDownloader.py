#!/usr/bin/python3
import requests
import bs4


def download_file(url, name):
    try:
        r = requests.get(url, stream=True, timeout=10)
        with open(name, 'wb') as f:
            for chunk in r.iter_content(1000):
                f.write(chunk)
    except Exception as exc:
        print('%s : There was a problem: %s Download has failed.' % (name, exc))
    else:
        print(name, ": Successfully downloaded", sep='')


def wordsearch(text, slen, elen=None): 
    textList = []
    for c in text:
        if c.isdigit():
            textList.append(int(c))
        else:
            textList.append(c)

    if elen == None:
        elen = slen

    if textList.index(slen):
        x = textList.index(slen)
        y = textList.index(elen, x + 1)
        token = "".join(str(i) for i in textList[x:y + 1])
        token = token.strip("'")
        return token


def adwDownload(url, name):
    adwPage = requests.get(url).text
    adwSoup = bs4.BeautifulSoup(adwPage, "lxml")

    Soup = adwSoup.script.string
    Souplist = Soup.splitlines()
    for i in Souplist:
        if "var downloadToken = " in i:
            token = wordsearch(i, '\'')
    download_file(url + token, name)
    
def main():
    URLs = {'http://cdn.superantispyware.com/SUPERAntiSpyware.exe': "SuperAntiSpyware.exe",
            'https://downloads.malwarebytes.com/file/mbam_current': "Malwarebytes.exe",
            'http://files.avast.com/iavs9x/avast_free_antivirus_setup_online.exe': "Avast.exe",
            'http://www.adlice.com/partners/09-download-roguekiller-direct': "Roguekiller.exe",
            "https://downloads.malwarebytes.com/file/jrt/": "JRT.exe"
            }

    for k, v in URLs.items():
        download_file(k, v)

    adwDownload("https://toolslib.net/downloads/finish/1-adwcleaner/1032/get/", "Adwcleaner.exe")

main()
