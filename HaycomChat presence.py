CLIENT_ID = '1345804754684481606' 

from pypresence import Presence
import time
from datetime import datetime

RPC = Presence(CLIENT_ID)
RPC.connect()

start_date = datetime(2025, 3, 25, 13, 26)  # Année, Mois, Jour, Heure, Minute
start_time = int(start_date.timestamp()) 

# Test du Rich Presence avec un temps fictif
RPC.update(
    details="HaycomChat",  # Affiche le nom de l'app et l'outil
    state="Teste et correction de la beta",  # le statut
    large_image="logo_complete",  #grande image
    large_text="90%",  # Nom du survole de la souris sur grand image
    #small_image="",  # petite image
    small_text="Testing",  # Un autre texte
    start=start_time,  # Fake timer en vert sur Discord
    buttons=[{
        'label': "Pas encore disponible",  # Texte du bouton
        'url': 'https://www.google.com'  # https://shattereddisk.github.io/rickroll/rickroll.mp4
    }]
)

print(" Rich Presence personnalisé affiché !")

while True:
    time.sleep(15)
