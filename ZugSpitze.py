import math as mt

class main:
#definicje i stale
    k = 1.38*pow(10,-23) #stała boltzmana
    e = 1.6*pow(10,-19)  #ładunek elementarny
    dane = {}            #slownik danych o dystansach składowych
    ladunki = {}         #słownik danych o definicji układu
    ll = 0               #liczba ladunków
    m1 = False           #marker w funk. wprowadz_definicje()
    x = 0                #współżędne badanego punktu
    y = 0
    z = 0
    Ex = 0               #wartoci  składowych wektorów natężenia pola
    Ey = 0
    Ez = 0
    Ew = 0

        #funkcje pomocnicze
    def czy_calkowita(self,badana): # sprawdza czy liczba jest całkowita
        try:
            badana = int(badana)
            return(badana)
        except (ValueError, TypeError):
            return self.czy_calkowita(self, input("Zły argument! Podaj liczbe calkowita\n"))
            
    def czy_rzeczywista(self,badana): #sprawdza, czy wpisano liczbę rzeczywistą
        try:
            badana = float(badana)
            return(badana)
        except (ValueError, TypeError):
            return self.czy_rzeczywista(self, input("Zły argument! Podaj liczbe rzeczywista\n"))
        
    def wprowadz_definicje(self,m1):  # wprowadza definicje ładunków do słownika  
        
        if self.m1 == True:
            d=input('czy chcesz zdefiniowac nowy uklad do badań ?\n [T/N] ')
           
            if ord(d) == ord('T') or ord(d) == ord('t'): #opcja T
                self.m1 = False
                self.wprowadz_definicje(m1)
            elif ord(d) == ord('N') or ord(d) == ord('n'): #opcja N
                    print('\npodaj wspolzedne badanego punktu')
                    self.x=main.czy_rzeczywista(self,input('nowe x\n'))
                    self.y=main.czy_rzeczywista(self,input('nowe y\n'))
                    self.z=main.czy_rzeczywista(self,input('nowe z\n'))
            else:
                self.wprowadz_definicje(m1)
        else:
            mll = False
            while mll == False:    
                self.ll= main.czy_calkowita(self,input('podaj liczbę ładunków\n'))
                if self.ll >> 0 :
                    mll = True
                else: 
                    print('podaj liczbę większą od zera')
            self.ll=int(self.ll)
            for i in range(0,self.ll):
                i = str(i)
                self.ladunki['etykieta'+i]=input('nazwa \n')
                self.ladunki[self.ladunki['etykieta'+i]+'ladunek'] = main.czy_calkowita(self,input('podaj wartosc ladunku jako wielokrotnosc "e"\n' ))
                self.ladunki[self.ladunki['etykieta'+i]+'x'] = main.czy_rzeczywista(self,input('podaj wartosc x\n'))
                self.ladunki[self.ladunki['etykieta'+i]+'y'] = main.czy_rzeczywista(self,input('podaj wartosc y\n'))
                self.ladunki[self.ladunki['etykieta'+i]+'z'] = main.czy_rzeczywista(self,input('podaj wartosc z\n'))
                i = int(i)
            print('\npodaj wspolrzedne badanego punktu')
            self.x=(main.czy_rzeczywista(self,input('x\n')))
            self.y=(main.czy_rzeczywista(self,input('y\n')))
            self.z=(main.czy_rzeczywista(self,input('z\n')))
            
        
            self.m1 = True
        return(self.ladunki, self.x, self.y, self.z, self.ll, self.m1)
        
        
        
    def dystans(self,ladunki,x, y, z, ll):  # oblicza dystans między punktami jako serię wektorów składowych i zapisuje do słownika.
        for i in range(0,self.ll):
            i=str(i)
            self.dane['rx'+self.ladunki['etykieta'+i]] = self.x - self.ladunki[self.ladunki['etykieta'+i]+'x']
            self.dane['ry'+self.ladunki['etykieta'+i]] = self.y - self.ladunki[self.ladunki['etykieta'+i]+'y']
            self.dane['rz'+self.ladunki['etykieta'+i]] = self.z - self.ladunki[self.ladunki['etykieta'+i]+'z']
            i=int(i)
        return(self.dane)    
     
    
    def oblicz_skladowe(self,dane, ladunki, x, y, z, ll, k, e): #obicza składowe wartoci Natężenia pola w badanym punkcie
        for i in range(0,ll):
            i=str(i)
            if dane['rx'+self.ladunki['etykieta'+i]] != 0:
                self.Ex= self.Ex + ((self.k*self.e*self.ladunki[self.ladunki['etykieta'+i]+'ladunek']) / dane['rx'+self.ladunki['etykieta'+i]])
            else :
                pass
            if self.dane['ry'+self.ladunki['etykieta'+i]] != 0:
                self.Ey= self.Ey + ((self.k*self.e*self.ladunki[self.ladunki['etykieta'+i]+'ladunek']) / dane['ry'+self.ladunki['etykieta'+i]])
            else :
                pass
            if  self.dane['rz'+self.ladunki['etykieta'+i]] != 0:
                self.Ez= self.Ez + ((self.k*self.e*self.ladunki[self.ladunki['etykieta'+i]+'ladunek']) / dane['rz'+self.ladunki['etykieta'+i]])
            else :
                pass
            i = int(i)
            return (self.Ex, self.Ey, self.Ez)
        
    def oblicz_wypadkowe(self, Ex, Ey, Ez): #oblicza wypadkowe natężenie pola elektrycznego w badanym punkcie
        self.Ew = mt.sqrt(pow(self.Ex,2)+pow(self.Ey,2)+pow(self.Ez,2))
        
        return (self.Ew)
    
    def wynik(self, Ex, Ey, Ez, Ew):
        print('wektor wypadkowy E = ' + str(self.Ew) + '\n wektory składowe:\nEx = '+ str(self.Ex) +'\nEy = ' + str(self.Ey) +'\nEz = '+str(self.Ez))
        return()


   #ciąg obliczeniowy
class last:
    m2 = True
    def end(self):
         d = input('Czy to już wszystko co mogę dla Ciebie zrobić ?[T/N]')
             
         if ord(d) == ord('T') or ord(d) == ord('t'):#t
             last.m2 = False
             print('dziękuję za współpracę')
         elif ord(d) == ord('N') or ord(d) == ord('n'):#n
             pass
         else:
             last.end(self) 
    def gotowiec(self):
        while self.m2 == True:
            main.wprowadz_definicje(main,main.m1)
            main.dystans(main,main.ladunki, main.x, main.y,main.z, main.ll)    
            main.oblicz_skladowe(main,main.dane, main.ladunki, main.x, main.y,main.z, main.ll, main.k, main.e)
            main.oblicz_wypadkowe(main,main.Ex, main.Ey, main.Ez) 
            main.wynik(main,main.Ex, main.Ey, main.Ez, main.Ew)
            last.end(last)
           
# last.gotowiec(last)