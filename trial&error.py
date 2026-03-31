def round_list (situatie_1):
    situatie_1_rounded = []
    for item in situatie_1:
        situatie_1_rounded.append(round(item,1))
    return situatie_1_rounded



def simulatie_hypothecaire_lening (lening, jaren, rente, start_periode=0, eind_periode=0, extra=0, maand=0):

    duur = jaren * 12
    rente_p = rente / 100
    rente_m = rente_p / 12
    mensualiteit = lening * (rente_m * (1 + rente_m)**duur) / ((1 + rente_m)**duur - 1)
    interest_kosten = 0
    interest_kosten_2 = 0
    maanden = 0
    totale_kost = 0
    interest_lijst = []
    kapitaal_lijst = []
    counter = 0

    #2 aparte for loops maken.
    #1ste vast met aantal jaren zodat de eerste loop volledig overheen heel de jaren loopt met de juiste mensualiteit.
    #Hierbij 2 lists maken: 1 van al de interest & 1 van al het kapitaal.

    #2de loop maken waarin er een begin- en eindperiode input wordt gebruikt als index (i) zodat vervolgens specifieke delen interesten & kapitaal kan worden opgeteld uit voorgaande 2 lijsten.



    for i in range(1, jaren*12 + 1):

        interest = lening * rente_m
        kapitaal = mensualiteit - interest    
        lening = lening - kapitaal - extra
        interest_kosten = interest_kosten + interest
        totale_kost = totale_kost + interest + kapitaal + extra
        extra_betaald = extra * jaren * 12
        maanden = maanden + 1
        interest_lijst.append(interest)
        kapitaal_lijst.append(kapitaal)

        #print(interest)
        #print(kapitaal)
        #print(round_list(interest_lijst))

        if i == maand:
            print(F"Deze maand betaalt u {round(interest,1)} euro interest & u stort {round(kapitaal,1)} euro terug")

        if lening < 0:
            break


    for j in range(len(interest_lijst)):
        if j >= start_periode * 12 and j < eind_periode * 12:
            #print(interest_lijst[j])
            counter = counter +1
            interest_kosten_2 = interest_kosten_2 + interest_lijst[j]
    print(counter)


    return mensualiteit, totale_kost, interest_kosten, extra_betaald, maanden, len(interest_lijst), interest_kosten_2




x = simulatie_hypothecaire_lening(lening=250000, jaren=25, rente=3, start_periode=0, eind_periode=20)
print(x)

