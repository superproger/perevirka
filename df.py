from time import strftime, gmtime
import  urllib2 , os , csv , numpy
import pandas as pd
pdict={1:'Vinnytsya',2:'Volyn',3:"Dnipropetrovs'k",4:"Donets'k",5:'Zhytomyr',6:'Transcarpathia',7:'Zaporizhzhya',8:"Ivano-Frankivs'k",9:'Kiev',10:'Kirovohrad',
      11:"Luhans'k",12:"L'viv",13:'Mykolayiv',14:'Odessa',15:'Poltava',16:'Rivne',17:'Sumy',18:"Ternopil'",19:'Kharkiv',20:'Kherson',21:"Khmel'nyts'kyy",
      22:'Cherkasy',23:'Chernivtsi',24:'Chernihiv',25:'Crimea',26:"Sevastopol'"}
zdict = {'Volyn': 25, 'Kiev': 12, "L'viv": 15, 'Chernivtsi': 3, 'Odessa': 17, 'Chernihiv': 2, 'Kherson': 9, 'Sumy': 21, 'Cherkasy': 1, 'Zhytomyr': 27, 'Transcarpathia': 23, 'Mykolayiv': 16, 'Kirovohrad': 13, 'Poltava': 18, "Dnipropetrovs'k": 5, "Donets'k": 6, "Khmel'nyts'kyy": 10, 'Kharkiv': 8, "Luhans'k": 14, 'Zaporizhzhya': 26, "Ternopil'": 22, 'Vinnytsya': 24, "Sevastopol'": 20, 'Rivne': 19, 'Crimea': 4, "Ivano-Frankivs'k": 7}
fdict = {}
def frame(filedir):
    i=0
    for filename in os.listdir(filedir):
        if filename.endswith('.csv'):
            if i<len(zdict):
                df = pd.read_csv('%s%s' %(filedir,filename), index_col=False, header=1)
                fdict[zdict.keys()[i]] = df
            i+=1
    #return fdict.keys()
def dani(num):
    print pdict[num]
    return fdict[pdict[num]]
    
def rik(year,num):
        df=dani(num)
        print df[(df['year']==year)]
        print ('max & min')
        print df[(df['VHI']==max(df['VHI']))]
        print df[(df['VHI']==min(df['VHI']))]
def pos(num):
        da=dani(num)
        df=list(da['VHI'])
        dk=list(da['week'])
        dm=list(da['year'])
        i=0
        while i < len(df):
                if df[i]<=15:
                        print df[i],dk[i],dm[i]
                i+=1
def pom(num):
        da=dani(num)
        df=list(da['VHI'])
        dk=list(da['week'])
        dm=list(da['year'])
        i=0
        while i < len(df):
                if df[i]<=35:
                        print df[i],dk[i],dm[i]
                i+=1
def zpom():
        i=1
        while i<27:
                pom(i)
                i+=1
def zpos():
        i=1
        while i<27:
                pos(i)
                i+=1
a=frame('data//')
