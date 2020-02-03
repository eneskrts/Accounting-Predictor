
import sqlite3
import matplotlib.pyplot as plt


import pandas as pd

db=sqlite3.connect("db_1.db")
veriler = pd.read_sql_query("SELECT ay,kazanc FROM satislar",db)

aylar=veriler.iloc[:,0]
satislar=veriler.iloc[:,1]

m,c=0,0
L=0.0001
n=len(aylar)

for i in range(1000):
    y_tahmin=m*aylar+c
    D_m=(-2/n)* sum(aylar*(satislar-y_tahmin))
    D_c=(-2/n)* sum(satislar-y_tahmin)
    m=m-L*D_m
    c=c-L*D_c

kullanici_ay=30
y=m*kullanici_ay+c 
#print("tahmin",y)

plt.scatter(aylar,satislar,color='blue')
y_t=m*aylar+c 
plt.plot(aylar,y_t,color="red")
def tahmin_et(ay=10):
    return m*ay+c

def ciz():
    return aylar,satislar,y_t
def calc_r(x,y):
    n=len(x)
    r=(n*(sum(x*y))-sum(x)*sum(y))/(((n*(sum(x**2))-(sum(x)**2))*(n*sum(y**2)-sum(y)**2))**0.5)
    return r
def yazdir():
    y_gercek=satislar
    y_tahmin=m*aylar+c
    r=calc_r(y_tahmin,y_gercek)
    #print(f"Programın başarımı % {(r**2)*100}")
    return (r**2)*100


if __name__=='__main__':

    tahmin_et()
    ciz()
    yazdir()
    plt.show()
