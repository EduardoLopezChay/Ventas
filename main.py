print("*****Almacen el Buen Precio*******");
name=str(input("Ingrese su nombre : "))
year=int(input("Ingrese su año de nacimiento : "))

if(year <= 2004) :
  print("***",name,"por ser mayor el programa continua***")
  print("***El programa nesesita saber su venta del primer semestre y del segundo semestre del año 2021***")
  Sem_1=int(input("Ingrese su venta del primer semestre :"))
  Sem_2=int(input("Ingrese su venta del segundo semestre :"))
  suma=int(Sem_1+Sem_2);
  print(name,"Su venta total fue de :",suma)
  print("***El mejor semestre del año***")
  if Sem_1 > Sem_2 :
      mensaje=(name,"El Primer Sememestre te fue mucho mejor que el segunda semestre")
  elif Sem_2 > Sem_1 :
     mensaje=(name,"el segundo Sememestre te fue mucho mejor que el Primer semestre")
  print(mensaje)
  print("***Premio determinado por alcanzar una meta***")
  if (suma <=100000):
      med=("Medalla de bronce")
      pre=("un día libre para el vendedor")
  elif (suma<= 500000):
      med = ("Medalla de plata")
      pre =("un día libre con un bono de Q250")
  elif (suma <= 1000000):
      med = ("Medalla de oro ")
      pre=("un día libre con un bono de Q500")
  elif (suma > 1000000):
    med = ("Medalla de diamante para ventas superiores al millón de quetzales ")
    pre=("dos días libres y un bono de Q1,000.")
  print("Vendedor :",name);
  print("Ventas anuales :",suma)
  print("Mejor semestre :",mensaje)
  print("Medalla acreditada :",med)
  print("Premio :",pre)
else:
      print("***Gracis por participar***")
