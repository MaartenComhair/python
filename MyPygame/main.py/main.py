def round_list (Float_lijst):
    situatie_1_rounded = []
    for item in Float_lijst:
        situatie_1_rounded.append(round(item,1))
    return situatie_1_rounded



def simulatie_hypothecaire_lening (lening, jaren, rente, start_periode, eind_periode, extra=0, maand=0):

    duur = jaren * 12
    rente_p = rente / 100
    rente_m = rente_p / 12
    mensualiteit = lening * (rente_m * (1 + rente_m)**duur) / ((1 + rente_m)**duur - 1)

    totale_kost = 0
    totale_kost_2 = 0
    interest_kosten_max = 0
    interest_kosten_2 = 0
    maanden_max = 0
    maanden_betaald = 0
    kapitaal_kosten = 0
    
    interest_lijst = []
    kapitaal_lijst = []


    #for loop voor berekening gegevens bij lening met volledige duurloop.
    for i in range(1, jaren*12 + 1):

        interest = lening * rente_m
        kapitaal = mensualiteit - interest
        maanden_max = jaren * 12 

        lening = lening - kapitaal - extra
        interest_kosten_max = interest_kosten_max + interest
        totale_kost = totale_kost + interest + kapitaal + extra
        

        interest_lijst.append(interest)
        kapitaal_lijst.append(kapitaal)

        #print(interest)
        #print(kapitaal)

        if i == maand:
            print(F"Deze maand betaalt u {round(interest,1)} euro interest & u stort {round(kapitaal,1)} euro terug")
   
        if lening < 0:
            break

    
    #for loop voor berekening interest bij lening met deelse duurloop.

    for j in range(len(interest_lijst)):
        if j >= start_periode * 12 and j < eind_periode * 12:
            maanden_betaald = maanden_betaald + 1
            interest_kosten_2 = interest_kosten_2 + interest_lijst[j]
            kapitaal_kosten = kapitaal_kosten + kapitaal_lijst[j]

        extra_betaald = extra * maanden_betaald
        totale_kost_2 = interest_kosten_2 + kapitaal_kosten + extra_betaald

    return mensualiteit, totale_kost, interest_kosten_max, maanden_max, extra_betaald, totale_kost_2, interest_kosten_2, kapitaal_kosten, maanden_betaald



voorvoegsels = ['mensualiteit',
                'maximale totale kost',
                'maximale totale interest kosten',
                'maximale aantal maanden',
                'totale som extra afgelost',
                'totale kost deels afbetaald',
                'interest kosten van deelse afbetaling',
                'kapitaal kosten van deelse afbetaling',
                'aantal maanden effectief betaald',
                ]

  
situatie_1 = round_list(
    simulatie_hypothecaire_lening(
        lening= 275000,
        jaren= 25,
        rente= 3.0,
        start_periode= 0,
        eind_periode= 10,
        extra=0))

#lijst --> dict + voorvoegsels
situatie_1_dict = dict(zip(voorvoegsels,situatie_1))

print("Lening 1: \n")
for key, value in situatie_1_dict.items():
    print(f"{key}: {value}")


situatie_2 = round_list(
    simulatie_hypothecaire_lening(
        lening= 275000,
        jaren= 25,
        rente= 3.5,
        start_periode= 0,
        eind_periode= 10,
        extra= 0))

#lijst --> dict + voorvoegsels
situatie_2_dict = dict(zip(voorvoegsels,situatie_2))

print()
print("lening2: \n")

for key, value in situatie_2_dict.items():
    print(f"{key}: {value}")



def hypothecaire_lening_vergelijken(situatie_1, situatie_2):

    verschil_interest = situatie_1['interest kosten van deelse afbetaling'] - situatie_2['interest kosten van deelse afbetaling']
    return verschil_interest

vergelijking_interest = hypothecaire_lening_vergelijken(situatie_1_dict,situatie_2_dict)
print(round(vergelijking_interest,1))






