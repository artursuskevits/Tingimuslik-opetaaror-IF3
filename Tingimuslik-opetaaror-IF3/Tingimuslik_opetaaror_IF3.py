from math import *

#try: #task 1
#    name = (input("what is your name? "))
#    if name.lower() == "juku" :
#        print("Lähme kinno")
#        vanus = int(input("kui vana sa oled? "))
#        if vanus>=0 or vanus <=100:
#            print("viga andmetega")
#        elif vanus <6:
#            print("tasuta")
#        elif vanus>=6 and vanus <=14:
#            print("lastepilet")
#        elif vanus>=15 and vanus <65:
#            print("täispilet")
#        elif vanus>=65:
#            print("sooduspilet")
#    else:
#        print("Otsime Juku")
#except:
#    print("Vale Andmetüb") 
   

#nimi1 = input("mis on sinu nimi ?") #task2
#nimi2 = input("ja mis on sinu nimi? ")
#if nimi1.isalpha() and nimi2.isalpha():
#    if nimi1.lower()=="dilan" and nimi2.lower()=="artur":
#        print(f"{nimi1} ja {nimi2} istute koos ")
#    elif nimi1.lower()=="artur" and nimi2.lower()=="dilan":
#        print(f"{nimi1} ja {nimi2} istute koos ")
#    else:
#        print("wrong names")
#else:
#    print("viga!")


#try: #task3
#    a = float(input("külje pikkus a? ")) 
#    b = float(input("külje pikkus b? "))
#    if a>0 and b>0:
#        S=round(a*b,2)
#        print(f"põrandapind = {S}m2")
#        answer = int(input("soovite remonti teha? 1-jah, other-ei?"))
#        if answer==1:
#            metr=float(input("kui palju on ruutmeeter"))
#            if a>0:
#                cost= round(S*metr,2)
#                print (f"remont costa={cost} eurot")
#            else:
#                print("viga")
#        else:
#            print("kui kahju")
#    else:
#        print("viga")
#except:
#    print("viga")

#try: #task4
#    maksab = float(input("mis hinna on ? "))
#    if maksab >0:
#        if maksab > 700:
#            hinna = (maksab*0.7,2)
#            print(f"Soodushind on {hinna} ")
#        else:
#            print("viga")
#    else: 
#        print("viga")
#except:
#    print("viga")

#try: #task5
#    temperatuur = float(input("mis temepreatuur on? "))
#    if temperatuur >18:
#        print("see on hea temperatuur")
#    else:
#        print("see ei ole hea temperatuur")
#except:
#    print("viga")



#try: #task7
#    sugu= int(input("kas sa oled tüdrukud 1-JAH, OTHER - NO"))
#    if sugu==1:
#        pikkus = float(input("mis on sinu pikkus? "))
#        if pikkus <100 or pikkus >250:
#            print("vale pikkus")
#        elif pikkus >100:
#            print ("sa oled madal")
#        elif pikkus >=160 and pikkus <=180:
#            print ("sa oled keskmine")
#        elif pikkus >180:
#            print ("sa oled kõrge")
#    else:
#        pikkus = float(input("mis on sinu pikkus? "))
#        if pikkus <100 or pikkus >250:
#            print("vale pikkus")
#        elif pikkus >100:
#            print ("sa oled madal")
#        elif pikkus >=170and pikkus <=185:
#            print ("sa oled keskmine")
#        elif pikkus >190:
#            print ("sa oled kõrge")
#except:
#    print("viga")

#try: #task6
#    pikkus = float(input("mis on sinu pikkus? "))
#    if pikkus <100 or pikkus >250:
#       print("see ole viga")
#    elif  pikkus >100 and pikkus<160:
#       print ("sa oled madal")
#    elif pikkus >=160 and pikkus <=180:
#       print ("sa oled keskmine")
#    elif pikkus >180 and pikkus <=250:
#       print ("sa oled kõrge")
#except:
#    print("viga")

#try: #task8
#    piim = int(input("sa tahad piima osta 1-yes, other-no? "))
#    if piim == 1:
#        piimost = float(input("kui palju piim maksab? "))
#        if piimost>0:
#            saia = int(input("sa tahad saia osta 1-yes, other - no? "))
#            if saia == 1:
#                saiaost = float(input("kui palju saia maksab? "))
#                if saiaost>0:
#                    leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#                    if leiba == 1 :
#                        leibaost = float(input("kui palju leiba maksab? "))
#                        if leibaost>0:
#                            summa= leibaost + piimost + saiaost
#                            print(f"sa kulutasid{summa} euro")
#                        print("viga")
#                    else:
#                        summa= piimost + saiaost
#                        print(f"sa kulutasid{summa} euro")
#                else:
#                    print("viga")
#            else:
#                leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#                if leiba == 1 :
#                    leibaost = float(input("kui palju leiba maksab? "))
#                    if leibaost>0:
#                        summa= leibaost + piimost
#                        print(f"sa kulutasid{summa} euro")
#                    else:
#                        print("viga")
#                else:
#                    summa= piimost
#                    print(f"sa kulutasid{summa} euro")
#        else:
#            print("viga")
#    else:
#        saia = int(input("sa tahad saia osta 1-yes, other - no? "))
#        if saia == 1:
#            saiaost = float(input("kui palju saia maksab? "))
#            if saiaost>0:
#                leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#                if leiba == 1 :
#                    leibaost = float(input("kui palju leiba maksab? "))
#                    if leibaost>0:
#                        summa= leibaost + saiaost
#                        print(f"sa kulutasid{summa} euro")
#                    else:
#                        print("viga")
#                else:
#                    summa= saiaost
#                    print("sa kulutasid{summa} euro")
#            else:
#                prins("viga")
#        else:
#            leiba = int(input("sa tahad leiba osta 1-yes, other - no? "))
#            if leiba == 1 :
#                leibaost = float(input("kui palju leiba maksab? "))
#                if leibaost>0:
#                    summa= leibaost
#                    print(f"sa kulutasid{summa} euro")
#                else:
#                    print("viga")
#            else: 
#                print("sa ei ostnud midagi")
#except:
#    print("viga")
    
#try:    #task 9
#    a=float(input("külje pikkus a?"))
#    b=float(input("külje pikkus b?"))
#    c=float(input("külje pikkus c?"))
#    d=float(input("külje pikkus d?"))
#    if a>0 and b>o and c>0 and d>0:
#        if a== b and b==c and c==d:
#            print("see on Ruut")
#        else:
#            print("see ei ole ruut")
#    else:
#        print("viga")
#except:
#    print("viga")

#try: #task 10
#    arv1 = float(input("kirjuta esimene number? "))
#    arv2 = float(input("kirjuta teine number? "))
#    mark= input("valige toiming +-*/")
#    if mark == "+":
#        summ = arv1+arv2
#        print(f"answer is {summ}")
#    elif mark == "/":
#        summ = arv1/arv2
#        print(f"answer is {summ}")
#    elif mark == "*":
#        summ = arv1*arv2
#        print(f"answer is {summ}")
#    elif mark == "-":
#        summ = arv1-arv2
#        print(f"answer is {summ}")
#    else:
#        print("viga")
#except:
#    print("viga")

#try: #task 11
#    aeg = int(input("mis on sinu sünniaasta? "))
#    if aeg>1900:
#        aeg2 = 2022-aeg
#        if aeg2 // 10:
#            print(f"sul on arve!")
#        else:
#            print(f"sul ei ole arve")
#    else("viga")
#except:
#    print("viga")

#try: #task 12
#    hind = int(input("kui palju toode maksab? "))
#    if hind >=10:
#        hind2 = round(hind * 0.8,2)
#        print(f"soodushind on {hind2}")
#    else:
#        hind2 = round(hind * 0.9,2)
#        print(f"soodushind on {hind2}")
#except :
#    print("viga!")

#try: #task 13
#    sugu = input("kas sa oled mees või naine? ")
#    if sugu == "naine":
#        print ("sa ei saa olla jalgpallimeeskonnas")
#    elif sugu == "mees":
#        aeg = int(input("kui vanu sa oled? "))
#        if aeg == 16 or aeg == 17 or aeg == 18:
#            print("sa oled jalgpallimeeskonnas")
#        else:
#            print("sa ei saa olla jalgpallimeeskonnas")
#    else:
#        print("viga")

#except :
#    print("viga")

