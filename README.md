# Web-scraping-av-f21.vgs.no

Dette er et program som sjekker om det har kommet ett nytt oppslag på skolens nettside.

Fungerer slik:
  * Den sjekker det nyeste oppslaget på https://f21.vgs.no
  * Skriver ned overskriften til en csv fil
  * Så hvis overskriften er lik, skriver den at det har kommet ett nytt oppslag, hvis ikke skriver den at det ikke har skjedd noe siden sist.

Python modules som trengs (bruker python3):
  * from bs4 import BeautifulSoup
  * import requests
  * import csv

