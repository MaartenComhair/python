def simulatie_hypothecaire_lening (lening, jaren, rente, periode, extra=0, maand=0):

    duur = jaren * 12
    rente_p = rente / 100
    rente_m = rente_p / 12
    mensualiteit = lening * (rente_m * (1 + rente_m)**duur) / ((1 + rente_m)**duur - 1)
    interest_kosten = 0
    maanden = 0
    totale_kost = 0
  

    
    for i in range(1 +periode*12, jaren*12 + 1):

        interest = lening * rente_m
        kapitaal = mensualiteit - interest    
        lening = lening - kapitaal - extra
        interest_kosten = interest_kosten + interest
        totale_kost = totale_kost + interest + kapitaal + extra
        extra_betaald = extra * jaren * 12
        maanden = maanden + 1

        #print(interest)
        #print(kapitaal)

        if i == maand:
            print(F"Deze maand betaalt u {round(interest,1)} euro interest & u stort {round(kapitaal,1)} euro terug")
   
        if lening < 0:
            break
    return mensualiteit, totale_kost, interest_kosten, extra_betaald, maanden


def round_list (situatie_1):
    situatie_1_rounded = []
    for item in situatie_1:
        situatie_1_rounded.append(round(item,1))
    return situatie_1_rounded

voorvoegsels = ['mensualiteit','totale kost','interest kosten','extra betaald', 'aantal maanden betaald']
  
situatie_1 = round_list(simulatie_hypothecaire_lening(lening=275000, jaren=20, rente=3.0, periode=0, extra=0))

#combine list + voorvoegsels
situatie_1_dict = dict(zip(voorvoegsels,situatie_1))
print(situatie_1_dict)

situatie_2 = round_list(simulatie_hypothecaire_lening(lening=275000, jaren=20, rente=3.0, periode=0, extra=0))

#combine list + voorvoegsels
situatie_2_dict = dict(zip(voorvoegsels,situatie_2))
print(situatie_2_dict)

interest_verschil = situatie_1[2] - situatie_2[2]
print(round(interest_verschil,1))


#originele versie met 1 periode