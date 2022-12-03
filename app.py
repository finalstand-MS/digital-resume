from pathlib import Path

import csv
import cv2
import pyglet
import streamlit  as st
#HTML importer
import codecs 
from PIL import Image
import webbrowser

# ---- PATH SETTINGS ----

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"



resume_file = current_dir / "assets" / "Schakelaar 21-11-2022 CV.pdf"
profile_pic = current_dir / "assets" / "MS-768x768.jpeg"


# ---- html_header ----

# to open/create a new html file in the write mode

# ---- GENERAL SETTINGS ----

PAGE_TITLE = "Digital CV | Merijn Schakelaar"
PAGE_ICON = ":wave:"
NAME = "Merijn Schakelaar"
DESCRIPTION = """
Zorgbedrijfskundige.
"""
EMAIL = "mschakelaar@gmail.com"
MTEL = "0621822744"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/merijn-schakelaar-25767791/",
    "Twitter": "https://twitter.com/MSchakelaar",
}

PERSOONSGEGEVENS = ["Merijn Schakelaar", "Van Speykstraat 44a", "06-21822744", "mschakelaar@gmail.com","19-09-1994", "Groningen"]
LYVUP = {'werkzaamheden':
            {'Customer Value Propositions ontwikkelen': ['Van een product uit de wetenschap een commercieel product maken. Zo stond er binnen twee week een verkoopklaar product.', 'In de gezondheidszorg kan het een puzzel zijn om achter de échte klant te komen. Wie betaalt, wie gebruikt en wie profiteert? Door brainstorming hebben we een strategie ontwikkeld.'],
            'Ontwikkelprocess versnellen': ['Development proces verbeteren en versnellen. Procesoptimalisatie. Bijv: het toevoegen van iterative ontwikkelcyclussen.  Eerder testen van concepten i.c.m. marktvraag.'],
            'Branding': ['Ontwikkelen van nieuwe website-feel & look. De transitie ontwerpen en uitvoeren van een informatieve website naar een commerciele website.', 'Schrijven van content-uitingen. de balans vinden tussen een boodschap die aansluit bij commerciele klanten en klanten uit de gezondheidszorg.']
            }
        }

#FINALSTAND_WERKZAAMHEDEN=[]
#RIJKSUNIVERSITEIT_WERKZAAMHEDEN=[]
#BELSIMPEL_WERKZAAMHEDEN=[]




PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "",
}

# ---- start pagina ----

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=330)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download CV",    
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write("Tel:", MTEL)

# ---- whitespace ----
whitespace=st.markdown('##')
whitespace=st.markdown('##')
# ---- samenvatting ----

col1samenvatting, col2samenvatting, col3samenvatting = st.columns([8,10,8],gap="small")

col_samenvattingh1=" Merijn"
col_samenvattingh2="Werkervaring"
col_samenvattingh3="Eigenschappen"
col_samenvatting1="Ik ben een leergierige jongen. Ik ga graag open en rechtstreeks om met mijn teamgenoten. Wees niet bang om mij op te zadelen met veel nieuwe informatie, dat vind ik alleen maar leuk en uitdagend!"
col_samenvatting2="In mijn korte carriere heb ik bedrijven van verschillende omvangen meegemaakt en bekeken vanuit meerdere lenzen. Startup, scale-up, MKB en grote instituten. Daarmee heb ik een solide werkbasis ontwikkeld."
col_samenvatting3="Vaardig met computers. O.a. python, C, VBA, html/css code schrik ik niet van. Master in bedrijfskunde met focus op gezondheidszorg. Daarnaast bachelor bedrijskunde afgerond met een focus op technology management."

with col1samenvatting:
   st.header(col_samenvattingh1)
   st.write(col_samenvatting1)

with col2samenvatting: 
    st.header(col_samenvattingh2)   
    st.write(col_samenvatting2)

with col3samenvatting:
    st.header(col_samenvattingh3)
    st.write(col_samenvatting3)

# ---- whitespace ----

whitespace=st.markdown('##')
whitespace=st.markdown('##')
whitespace=st.markdown('##')

# ---- persoonsgegevens button ----

if st.button('Persoonsgegevens'):
    i = 0
    while i < len(PERSOONSGEGEVENS):
        st.write(PERSOONSGEGEVENS[i])
        i = i + 1
    st.button('Close')
else: st.write()


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")