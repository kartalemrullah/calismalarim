import matplotlib.pyplot as plt

ksayisi = int(input("kac kisilik grafik olusturulacak:"))
listeboy = []
listekilo = []
i=0
j=0
while ksayisi > 0:
  i = int(input("boyunuzu giriniz:"))
  j = int(input("kilonuzu giriniz:"))
  listeboy.append (i)
  listekilo.append (j)
  ksayisi -=1
  i +=1
  j +=1

print (listeboy)
print (listekilo)


plt.plot(listeboy,listekilo)
plt.show()