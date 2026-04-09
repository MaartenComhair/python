def round_list (Float_lijst):
    situatie_1_rounded = []
    for item in Float_lijst:
        situatie_1_rounded.append(round(item,1))
    return situatie_1_rounded


def bereken_totaal(maanden_totaal, lening_totaal, mensualiteit, rente_m, extra_m, maand):
    interest_lijst = []
    kapitaal_lijst = []
    interest_kosten_max = 0
    totale_kost = 0
    #for loop voor berekening gegevens bij lening met volledige duurloop.
    for i in range(1, maanden_totaal + 1):

        interest_m = lening_totaal * rente_m
        kapitaal_m = mensualiteit - interest_m
        

        lening_totaal -= (kapitaal_m + extra_m)
        interest_kosten_max += interest_m
        totale_kost += interest_m + kapitaal_m + extra_m

        interest_lijst.append(interest_m)
        kapitaal_lijst.append(kapitaal_m)

        #print(interest)
        #print(kapitaal)

        if maand == i:
            print(F"Deze maand betaalt u {round(interest_m,1)} euro interest & u stort {round(kapitaal_m,1)} euro terug")

        if lening_totaal < 0:
            break

    return interest_lijst, kapitaal_lijst, interest_kosten_max, totale_kost
    
def simulatie_hypothecaire_lening (lening_totaal, jaren, rente, start_periode, eind_periode, extra_m=0, maand=0):

    totale_kost_periode = 0
    interest_kosten_periode = 0
    maanden_betaald = 0
    kapitaal_kosten = 0

    maanden_totaal = jaren * 12
    rente_p = rente / 100
    rente_m = rente_p / 12
    mensualiteit = lening_totaal * (rente_m * (1 + rente_m)**maanden_totaal) / ((1 + rente_m)**maanden_totaal - 1)

    interest_lijst, kapitaal_lijst, interest_kosten_max, totale_kost = \
        bereken_totaal(maanden_totaal, lening_totaal, mensualiteit, rente_m, extra_m, maand)

    
    #for loop voor berekening interest bij lening met deelse duurloop.
    for i in range(len(interest_lijst)):
        if i >= start_periode * 12 and i < eind_periode * 12:
            maanden_betaald += 1
            interest_kosten_periode += interest_lijst[i]
            kapitaal_kosten += kapitaal_lijst[i]

        extra_betaald = extra_m * maanden_betaald
        totale_kost_periode = interest_kosten_periode + kapitaal_kosten + extra_betaald

    return mensualiteit, totale_kost, interest_kosten_max, maanden_totaal, extra_betaald, totale_kost_periode, interest_kosten_periode, kapitaal_kosten, maanden_betaald

def print_lening_dict(lening_dict):
    for key, value in lening_dict.items():
        print(f"{key}: {value}")

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
        lening_totaal= 275000,
        jaren= 25,
        rente= 3,
        start_periode= 0,
        eind_periode= 10,
        extra_m=0))

#lijst --> dict + voorvoegsels
situatie_1_dict = dict(zip(voorvoegsels,situatie_1))

print("Lening 1: \n")
print_lening_dict(situatie_1_dict)


situatie_2 = round_list(
    simulatie_hypothecaire_lening(
        lening_totaal= 275000,
        jaren= 25,
        rente= 3.5,
        start_periode= 0,
        eind_periode= 10,
        extra_m= 0))

#lijst --> dict + voorvoegsels
situatie_2_dict = dict(zip(voorvoegsels,situatie_2))

print()
print("lening2: \n")
print_lening_dict(situatie_2_dict)



def hypothecaire_lening_vergelijken(situatie_1, situatie_2):

    verschil_interest = situatie_1['interest kosten van deelse afbetaling'] - situatie_2['interest kosten van deelse afbetaling']
    return verschil_interest

vergelijking_interest = hypothecaire_lening_vergelijken(situatie_1_dict,situatie_2_dict)
print(round(vergelijking_interest,1))