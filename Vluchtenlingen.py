import time
import os

os.system("cls")

intro = 1;
vraag1 = 0;
antwoord1 = 0;
vraag2 = 0;
antwoord2 = 0;
vraag3 = 0;
antwoord3 = 0;
vraag4 = 0;
antwoord4 = 0;
vraag5 = 0;
antwoord5 = 0;
vraag6 = 0;
antwoord6 = 0;
vraag7 = 0;
antwoord7 = 0;
vraag8 = 0;
antwoord8 = 0;
vraag9 = 0;
antwoord9 = 0;
vraag10 = 0;
antwoord10 = 0;
vraag11 = 0;
antwoord11 = 0;
vraag12 = 0;
antwoord12 = 0;
vraag13 = 0;
antwoord13 = 0;
vraag14 = 0;
antwoord14 = 0;
vraag15 = 0;
antwoord15 = 0;
vraag16 = 0;
antwoord16 = 0;
vraag17 = 0;
antwoord17 = 0;
vraag18 = 0;
antwoord18 = 0;

while intro == 1:
    print("Het is oorlog in je land en je moet vluchten, het in namelijk heel onveilig")
    vraag1 = 1;
    intro = 0;
    break
    
while vraag1 == 1:
    print("Ga je vluchten?")
    antwoord1 = input("A - ja of B - nee : ").upper()
    break

while antwoord1 == 'A':
    vraag2 = 1; 
    break

while antwoord1 == 'B':
    vraag11 = 1;
    break

while vraag11 == 1:
    os.system("cls")
    print('\n'"Je kiest ervoor om niet te vluchten, uiteindelijk is dat geen optie en moet je toch vluchten maar omdat je later ging vluchten dan de rest gaat dat niet zo makkelijk meer")
    antwoord11 = input("A - Je gaat je dorp proberen uit te lopen met een masker op hopen dat ze je niet zien of B - Je gaat via de achterkant wegrennen hopen dat niemand je ziet of achtervolgt : ").upper()
    break

while antwoord11 == 'A': 
    print('\n'"Ze hadden je door en kan niet meer terug, je wordt neergeschoten") 
    break

while antwoord11 == 'B':
    vraag12 = 1;
    break

while vraag12 == 1:
    os.system("cls")
    print('\n'"Vluchten via de achterdeur heeft je veilig weggekregen niemand heeft je achtervolgt en je krijgt nu een baan aangeboden in Irak")
    antwoord5 = input("A - Je neemt de baan niet aan en blijft bij je familie of B - Je neemt de baan en gaat alleen naar Irak : ").upper()
    break
   
while vraag2 == 1:
    os.system("cls")
    print('\n'"Er staat een militair met een sniper buiten je huis, ga je naar buiten of wacht je binnen?")
    antwoord2 = input("A - Ik ga naar buiten of B - Ik blijf binnen tot het donker word : ").upper()
    break

while antwoord2 == 'A':
    print("U dead")
    break

while antwoord2 == 'B':
    vraag3 = 1;
    break

while vraag3 == 1:
    os.system("cls")
    print('\n'"Slim, het wachten is het waard je kan weg. Ga je vervolgens naar familie toe of ren je ergens random heen?")
    antwoord3 = input("A - Je gaat bij familie slapen of B - Je gaat weg uit deze buurt : ").upper()
    break

while antwoord3 == 'A':
    vraag4 = 1;
    break

while antwoord3 == 'B':
    vraag13
    break 

while vraag13 == 1:
    os.system("cls")
    print('\n'"Je heb nu nergens naar toe te gaan en vervolgens zien de militairen jou en pakken je op")
    break

while vraag4 == 1:
    os.system("cls")
    print('\n'"Gezellig, De volgende ochtend wordt er omgeroepen dat je weg moet uit je huis anders wordt je neergeschoten")
    antwoord4 = input("A - Je gaat uit je huis want je vind het te onveilig of B - Je blijft in je families huis : ").upper()
    break

while antwoord4 == 'A': 
    vraag5 = 1;
    break

while antwoord4 == 'B':
    print("Niet slim om te blijven zoals al was gezegd zou je neergeschoten worden!")
    break

while vraag5 == 1:
    os.system("cls") 
    print('\n'"Goedzo je bent weggegaan uit het huis, je bent nu dakloos en weet vrij weinig te doen maar je krijgt opeens werk aangeboden in Irak maar je moet wel je familie achterlaten ervoor doe je dat?")
    antwoord5 = input("A - Je neemt de baan niet aan en blijft bij je familie of B - Je neemt de baan en gaat alleen naar Irak : ").upper()
    break

while antwoord5 == 'A':
    vraag14 = 1;
    break

while antwoord5 == 'B':
    vraag6 = 1;
    break

while vraag14 == 1:
    os.system("cls")
    print('\n'"Je blijft gezellig bij je familie alleen je kan niks betalen en ook nergens heen, je moet nu gaan bedelen of ergens anders een baan vinden")
    antwoord14 = input("A - Je gaat bedelen of B - Je gaat ergens anders een baan proberen te vinden : ").upper()
    break

while antwoord14 == 'A':
    vraag15 = 1;
    break

while antwoord14 == 'B':
    print('\n'"Dit gaat niet en je heb je familie laten zitten")
    break

while vraag15 == 1:
    os.system("cls")
    print('\n'"Er komt een nieuwe smokkelaar naar je toe wat doe je?")
    antwoord15 = input("A - Je gaat niet mee maar nog meer bedelen gaat geen nut hebben B - Je gaat evengoed met hem mee : ").upper()
    break

while antwoord15 == 'A':
    print('\n'"Het is over je weet dat bedelen niet meer werkt en je kan nergens heen")
    break

while antwoord15 == 'B':
    vraag16 = 1; 
    break

while vraag16 == 1:
    os.system("cls")
    print('\n'"Je bent met de smokkelaar meegegaan en die is van plan je te brengen naar frankrijk met een pasporrt alleen omdat je weinig geld heb hou je schulden aan hem, wat doe je?")
    antwoord16 = input("A - Je bent van plan de smokkelaar te scammen wanneer je veilig bent of B - Je gaat netjes blijven en de smokkelaar uiteindelijk ze geld te geven wanneer je het heb : ").upper()
    break 

while antwoord16 == 'A':
    vraag17 = 1;
    break

while antwoord16 == 'B':
    vraag18 = 1;
    break

while vraag17 == 1:
    os.system("cls")
    print('\n'"Je bent ermee weggekomen met veel geluk maar je voeltje alsnog wel schuldig omdat de smokkelaar je heb geholpen")
    antwoord17 = input("A = Je bent van plan de smokkelaar op te bellen en hem evengoed het geld te geven of B = Je laat het zitten en zal gelukkig met je familie blijven wonen in Frankrijk : ").upper()
    break

while antwoord17 == 'A': 
    print('\n'"De smokkelaar is jouw dankbaar want hij was het vergeten")
    break

while antwoord17 == 'B': 
    print('\n'"Je leeft nu in een mooi huisje en heb een mooie toekomst")
    break

while vraag18 == 1:
    os.system("cls")
    print('\n'"je heb het geld gegeven aan de smokkelaar maar je heb niet veel geld om nu nog dingen te kunnen kopen")
    antwoord18 = input("A - Je vraagt of er korting kan zijn omdat je niet veel geld over houdt om dingen te kunnen betalen of B - Je geeft alles omdat je ruzie wilt voorkomen : ").upper()
    break

while antwoord18 == 'A':
    vraag19 = 1;
    break

while antwoord18 == 'B':
    print('\n'"Je loopt weg van de smokkelaar en weet dat je veel moet werken om geld te verdienen")
    break

while vraag6 == 1:
    os.system("cls")
    print('\n'"Slimme keuze je heb de baan genomen, je zal hier een tijdje moeten verblijven. Uiteindelijk kwam iedereen aan in Irak vervolgens kwam je een smokkelaar tegen, ga je naar hem toe of loop je door?")
    antwoord6 = input("A - Je gaat naar de smokkelaar en vraagt vervolgens wat de prijs is of B - Je loopt door zonder wat te zeggen : ").upper()
    break

while antwoord6 == 'A':
    vraag7 = 1;
    break

while antwoord6 == 'B':
    vraag
    break

while vraag7 == 1:
    os.system("cls")
    print('\n'"Je heb voor de smokkelaar gekozen, hij vraagt aan jou of je 15000 euro gaat betalen dan brengt hij jou naar Nederland neem jij de keuze aan?")
    antwoord7 = input("A - Je geeft de smokkelaar 15000 euro of B - Je vindt het te duur en loopt vervolgens weg : ").upper() 
    break

while antwoord7 == 'A':
    vraag8 = 1;
    break

while antwoord7 == 'B':
    print('\n'"Je heb gekozen niet mee te gaan en blijft je hele leven in Irak voor de rest van je leven")
    break

while vraag8 == 1:
    os.system("cls")
    print('\n'"Je heb 15000 euro gegeven en daardoor heb je nu een Nederlands paspoort. Je bent nu aan het reizen maar je moet stoppen omdat je naar de wc moet, ga je het zeggen of neem je het risico dat je in je broek plast?")
    antwoord8 = input("A - Je plast in je broek of B - Je vertelt hem dat je naar wc moet : ").upper()
    break

while antwoord8 == 'A':
    print('\n'"Ookal heb je nu in je broek geplast je bent veilig in Nederland aangekomen")
    break

while antwoord8 == 'B':
    vraag9 = 1;
    break

while vraag9 == 1:
    os.system("cls")
    print('\n'"Goedzo hij heeft je onderweg genoeg laten plassen. Je bent in Nederland aangekomen, wat nu?")
    antwoord9 = input("A - Je blijft bij de smokkelaar en kijkt wat hij gaat doen of B - Je gaat zelf onderzoeken waar je heen moet zodat je niet in problemen kan komen met de smokkelaar : ").upper()
    break

while antwoord9 == 'A':
    print('\n'"Je heb niks aan de smokkelaar hij laat je achter omdat hij doorgaat met werken")
    break

while antwoord9 == 'B': 
    vraag10 = 1;
    break
    
while vraag10 == 1:
    os.system("cls")
    print('\n'"Je heb gekozen om zelf rond te gaan, nu dus opzoek naar een toekomst met je familie in Nederland. Vervolgens ga je weer naar school toe en beleef je een mooie toekomst.") 
    break


    













	