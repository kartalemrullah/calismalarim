dosya = open("kayit.txt", "w")
listeid = []
listead = []
listesad = []
listesinif = []
listeyas = []
listecinsiyet = []
while True:
  a = int(input("yeni kayit islemi icin 1'e\nkayit silme islemi icin 2'e\nkayit sorgulama islemi icin 3'e basiniz:")) 
  if a==1: 
     print ("kayit islemini sectiniz")
     id = int(input("id giriniz:"))
     listeid = listeid + [id]
     
     ad = str(input("adinizi giriniz:"))
     listead = listead + [ad]
     
     sad = str(input("soyadinizi giriniz:"))
     listesad = listesad + [sad]
     
     sinif = int(input("sinifinizi giriniz:"))
     listesinif = listesinif + [sinif]
     
     yas = int(input("yasinizi giriniz :"))
     listeyas = listeyas + [yas]
     
     cinsiyet = str(input("cinsiyetinizi yaziniz:"))
     listecinsiyet = listecinsiyet + [cinsiyet]

  elif a==2:
        print ("kayit silme islemini sectiniz")
        kesin = int(input("silmek için eminseniz 1 yaziniz :"))
        if kesin==1:
          id = int(input("id giriniz:"))
          listeid.remove(id)
  
          ad = str(input("adinizi giriniz:"))
          listead.remove(ad)  

          sad = str(input("soy adinizi giriniz:"))
          listesad.remove(sad)
  
          sinif = int(input("sinifinizi giriniz:"))
          listesinif.remove(sinif)
  
          yas = int(input("yasinizi giriniz:"))
          listeyas.remove(yas)
  
          cinsiyet = str(input("cinsiyetinizi giriniz:")) 
          listecinsiyet.remove(cinsiyet)
    
  elif a==3:
      print ("kayit sorgulama islemini sectiniz")
      id = int(input("sorgulamak istenilen id giriniz:"))
      ad = str(input("sorgulamak istediginiz ismi giriniz:"))
      if id in listeid and ad in listead:
        print ("bu kisi kayitlidir.")
      else:
          print ("kayit bulunamamistir.") 
 
 
 dosya.write(
   listeid = []
   listead = []
   listesad = []
   listesinif = []
   listeyas = []
   listecinsiyet = [])
   listesinif = []
   listeyas = []
   listecinsiyet = [] )
