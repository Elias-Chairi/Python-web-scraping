from bs4 import BeautifulSoup
import requests
import csv
#Selenium brukes til å trykke på ting, men da må du ha chromedriver og path å shit

page = requests.get("https://f21.vgs.no")
soup = BeautifulSoup(page.text, 'html.parser')

liste_med_overskrifter = soup.select("h3 > span")
nyeste_oppslag = liste_med_overskrifter[1].text


with open("Sist_leste_oppslag.csv", newline='') as tekst_fil:
     filleser = csv.reader(tekst_fil)
     sjekk = ",".join(filleser.__next__())


if nyeste_oppslag == sjekk:
    print("Det har ikke skjedd noe nytt")

else:
    print("Det har kommet ett nytt oppslag!")
    print("Det nye opplsaget er: " + nyeste_oppslag)
    with open("Sist_leste_oppslag.csv", "w", newline='') as tekst_fil:
        filskriver = csv.writer(tekst_fil)
        filskriver.writerow([nyeste_oppslag])
