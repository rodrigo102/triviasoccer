import time
p1 = input("Em que ano o Palmeiras ganhou o mundial de clubes?\na)1950\nb)1951\nc)Palmeiras não tem mundial\n")
p2 = input("Quantas copas do mundo tem a seleção da Argentina? \na)3 \nb)2 \nc)1\n")
p3 = input("Quem fez o gol da vitória do Uruguai na copa do mundo de 1950? \na)Schiaffino \nb)Ghiggia \nc)Máspoli \n")
p4 = input("Quem é o atual treinador do grêmio? \na)Renato Gaúcho \nb)Renato Rocha \nc)Renato Abreu \n")
p4 = input("Qual é o nome do ex-melhor jogador do mundo que é conhecido nas redes sociais como 'O bruxo'?\na)Zidane \nb)Kaká \nc)Ronaldinho Gaúcho \n")
p5 = input("Quem é o jornalisra esportivo famoso nas redes sociais por liberar decretos bem humorados na sexta feira? \na) André Rizek \nb)Alê Oliveira \nc)Cleber Machado \n")
p6 = input("Que tradicional time fica localizado no bairo da Mooca, em São Paulo? \na)Juventus \nb)Grêmio da Mooca \nc)Linense \n")
p7 = input("Quem marcou o último gol da seleção brasileira na copa do mundo de 2010? \na)Robinho \nb)Luís Fabiano \nc)Graffite \n")
p8 = input("Em que ano foi disputado o primeiro campeonato inglês de futebol? \na)1890 \nb)1888 \nc)1915 \n")
p9 = input("Quem marcou o lendário gol do titulo da champions league para o Manchester United na temporada 98/99? \na)Solskjær \nb)Sherringham \nc)Beckham \n")
p10 = input("Quem levantou a taça da copa do mundo de 2002? \na)Ronaldo \nb)Robinho \nc)Cafú \n")

if   p1 == "a":
     a = 0
elif p1 == "b":
     a = 0
else:
     a = 1
if   p2 == "a":
     b = 0
elif p2 == "b":
     b = 1
else:
     b = 0
if   p3 == "a":
     c = 0
elif p3 == "b":
     c = 1
else:
     c = 0
if   p4 == "a":
     d = 0
elif p4 == "b":
     d = 0
else:
     d = 1
if   p5 == "a":
     e = 0
elif p5 == "b":
     e = 1
else:
     e = 0
if   p6 == "a":
     f = 1
elif p6 == "b":
     f = 0
else:
     f = 0
if   p7 == "a":
     g = 1
elif p7 == "b":
     g = 0
else:
     g = 0
if   p8 == "a":
     h = 0
elif p8 == "b":
     h = 1
else:
     h = 0
if   p9 == "a":
     i = 1
elif p9 == "b":
     i = 0
else:
     i = 0
if   p10 == "a":
     j = 0
elif p10 == "b":
     j = 0
else:
     j = 1

pf = a + b + c + d + e + f + g + h + i + j
if    pf >=0 and pf <=4 :
      print ("Sua pontuação foi: ", pf, "Você sabe pouco sobre a história de as lendas do futebol, estude mais!")
elif pf >=5 and pf <=8:
      print ("Sua pontuação foi: ", pf, "Quase lá, você conhece o básico sobre o futebol e suas lendas")
else:
      print ("Sua pontuação foi: ", pf, "Oloco bicho, sabe mais de futebol que o lendário PVC. Parabéns!")
time.sleep(5)
     
     
 
    
    
    
           

           
