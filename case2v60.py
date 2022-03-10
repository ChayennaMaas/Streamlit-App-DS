#!/usr/bin/env python
# coding: utf-8

# # Case 2: Blogpost- Fromula 1

# Groep: Anna de Geeter, Daan Handgraaf, Chayenna Maas, Iris van de Velde

# In[68]:


#pip install streamlit


# In[2]:


#import libraries
import pandas as pd
import numpy as np
import random
import requests
import datetime

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


# # Dataframe: Formula 1

# In[3]:


# driverstandings
url='https://ergast.com/api/f1/2021/1/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings1=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings1['location']='Sakhir'


# In[4]:


# driverstandings
url='https://ergast.com/api/f1/2021/2/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings2=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings2['location']='Emola'


# In[5]:


# driverstandings
url='https://ergast.com/api/f1/2021/3/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings3=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings3['location']='portimao'


# In[6]:


# driverstandings
url='https://ergast.com/api/f1/2021/4/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings4=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings4['location']='Montmelo'


# In[7]:


# driverstandings
url='https://ergast.com/api/f1/2021/5/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings5=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings5['location']='Monte-Carlo'


# In[8]:


# driverstandings
url='https://ergast.com/api/f1/2021/6/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings6=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings6['location']='Baku'


# In[9]:


# driverstandings
url='https://ergast.com/api/f1/2021/7/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings7=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings7['location']='Le Castellet'


# In[10]:


# driverstandings
url='https://ergast.com/api/f1/2021/8/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings8=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings8['location']='Spielberg, Styrian'


# In[11]:


# driverstandings
url='https://ergast.com/api/f1/2021/9/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings9=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings9['location']='Spielberg, Austrian'


# In[12]:


# driverstandings
url='https://ergast.com/api/f1/2021/10/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings10=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings10['location']='Silverstone'


# In[13]:


# driverstandings
url='https://ergast.com/api/f1/2021/11/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings11=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings11['location']='Budapest'


# In[14]:


# driverstandings
url='https://ergast.com/api/f1/2021/12/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings12=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings12['location']='Spa'


# In[15]:


# driverstandings
url='https://ergast.com/api/f1/2021/13/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings13=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings13['location']='Zandvoort'


# In[16]:


# driverstandings
url='https://ergast.com/api/f1/2021/14/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings14=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings14['location']='Monza'


# In[17]:


# driverstandings
url='https://ergast.com/api/f1/2021/15/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings15=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings15['location']='Sochi'


# In[18]:


# driverstandings
url='https://ergast.com/api/f1/2021/16/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings16=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings16['location']='Istanbul'


# In[19]:


# driverstandings
url='https://ergast.com/api/f1/2021/17/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings17=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings17['location']='Austin'


# In[20]:


# driverstandings
url='https://ergast.com/api/f1/2021/18/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings18=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings18['location']='Mexico City'


# In[21]:


# driverstandings
url='https://ergast.com/api/f1/2021/19/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings19=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings19['location']='Sao Paulo'


# In[22]:


# driverstandings
url='https://ergast.com/api/f1/2021/20/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings20=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings20['location']='Al Daayen'


# In[23]:


# driverstandings
url='https://ergast.com/api/f1/2021/21/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings21=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings21['location']='Jeddah'


# In[24]:


# driverstandings
url='https://ergast.com/api/f1/2021/22/results.json?limit=440'
driver_standings= requests.get(url).json()

driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings22=pd.json_normalize(driver_standings_list, record_path='Results')
driver_standings22['location']='Abu Dhabi'


# In[25]:


#Combine and rename dataframe
driver_standings=pd.concat([driver_standings1, driver_standings2,driver_standings3,driver_standings4, driver_standings5, driver_standings6, driver_standings7, driver_standings8, driver_standings9, driver_standings10, driver_standings11, driver_standings12, driver_standings13, driver_standings14, driver_standings15, driver_standings16, driver_standings17, driver_standings18, driver_standings19, driver_standings20, driver_standings21, driver_standings22])
driver_standings=driver_standings.drop(labels=['positionText', 'Driver.code', 'FastestLap.AverageSpeed.units', 
                                               'Driver.url', 'Constructor.url', 'Driver.permanentNumber', 
                                               'Driver.driverId', 'Constructor.constructorId', 'Constructor.nationality'], 
                                       axis=1)
driver_standings=driver_standings.rename(columns={'Driver.givenName': 'name', 'Driver.familyName': 'surname', 
                                                 'Driver.dateOfBirth': 'DoB', 'Driver.nationality': 'nationality', 
                                                  'Constructor.name': 'Constructor', 'Time.millis': 'time [ms]', 'Time.time': 'time',
                                                 'FastestLap.lap': 'fastest lap', 'FastestLap.Time.time': 'fastestLap time', 
                                                 'FastestLap.AverageSpeed.speed': 'fastest lap avr.speed', 
                                                  'FastestLap.rank': 'fastest lap rank'})


# In[26]:


driver_standings.info()


# In[27]:


driver_standings.isna().sum().sort_values(ascending=False)


# NaN waardes gaan geen probleem worden met onze analyse, vandaar dat deze niet worden meegenomen.

# # Plots: Formule 1

# In[28]:


st.title('Overzicht formule 1 seizoen: 2021 ')


# In[29]:


st.write(
'Auteurs: Anna de Geeter, Daan Handgraaf, Chayenna Maas, Iris van de Velde'
)


# In[30]:


st.image('https://gadgetgekkie.bladecdn.net/wp-content/uploads/2021/07/F1-2021-1-1068x601.jpg')


# In[31]:


st.write(
'Welkom op op onze blog! Op deze pagina zal er een korte analyse worden gedaan ' 
'over de verkregen resultaten van het afgelopen seizoen van de formule 1!'
)

st.write(
'In deze blog wordt uitgelegd waar verkregen dataset waarmee is gewerkt vandaan komt. '
'Ook worden de resultaten per coureur en per team op iedere grandprix locatie met elkaar vergeleken.'
)

st.write(
'In het kopje status wordt worden de gereden races verder onder de loop genomen, hierbij wordt voornamelijk '
'besproken of de coureur is gefinished of dat de coureur bij een bepaalde race een ongeluk, pech enz. had, dit '
'zal dan ook in de plot vallen onder "not finished". '
'Ook worden de snelste laptijden per coureur per wedstrijd met elkaar vergeleken.'
)

st.write(
'Als laatst hebben we een dataframe gemaakt om de begin(grid) posities en eindposities met elkaar te vergelijken, om '
'zo in te zien welke driver het meest is geklommen of juist is gezakt in positie. '
'Daarbij zullen alle gemaakt plots interactief zijn en kunnen worden aangepast door de lezer zelf, fijn lees plezier!'
)


# In[32]:


st.header('Verkregen dataset')


# In[33]:


st.write(
'De dataset, die is gebruikt voor de analyses komt van de Ergast Developer API (http://ergast.com/mrd/). '
'Om uiteindelijk bij de gewenste dataset te komen heb je de volgende url nodig: '
'http[s]://ergast.com/api/<series>/<season>/<round>/... '
'Waarbij op de plek van series "F1" komt te staan, op de plek van "season" kan je selecteren welk jaar je wilt '
'en op de plek van "round" kun je specificeren welke race je wilt bekijken. Als laatste kun je op de plek van de puntjes '
'specificeren welke data je wilt, in ons geval willen wij daar "results" hebben.'
)

st.write(
'Het enige vervelende hieraan is dat wanneer je dataset uit meerdere bladzijdes bestaat komt er een limiet op te staan, wanneer '
'je dan de .json file wilt krijg je alleen de gegevens tot die limiet. De limiet staat op 30, dit betekent dat je maar 30 resultaten. '
'krijgt. '
'De aanpassing die je dan moet doen is kijken naar hoeveel resultaten de dataset heeft in totaal en dit aanpassen in de url. '
'In ons geval had de dataset "results" in het seizoen 2021 440 resultaten en hebben de url als volgt op deze manier aangepast:'
'https://ergast.com/api/f1/2021/1/results?limit=440. Dit overschrijft het standaard limiet en wordt het mogelijk om er een json file van de te maken.'
)

st.write(
'Om het .json file te krijgen kan er simpel .json achter de url worden geplakt om zo deze te gebruiken in jouw data analyse. '
'Pas wel op dat wanneer je in je url "?limit=<getal>" hebt staan dat de .json hier nog voor moet.'    
)

st.write(
'Het json file bestond uit een dataset waarbij veel in elkaar gestopte libraries voorkwamen, dit moest daarom ook ' 
'eerst goed worden gezet voordat de gewenste dataframe tevoorschijn kwam. '
'Dit kon bereikt worden door de pd.json_normalize te gebruiken en daarbij het gewenste record_path te specificeren. '
)


# In[34]:


code=''' 
#Verkregen dataset
url='https://ergast.com/api/f1/2021/1/results.json?limit=440'
driver_standings= requests.get(url).json()

#Omzetten naar een dataframe
driver_standings_list = driver_standings['MRData']['RaceTable']['Races']
driver_standings=pd.json_normalize(driver_standings_list, record_path='Results')
'''
st.code(code)


# In[35]:


st.write(
'Om de dataset klaar te stomen voor gebruik zijn de kolommen die niet zijn ' 
'gebruikt weggelaten en zijn er enkele kolommen hernoemt om deze in het '
'latere stadia beter te erkennen en te gebruiken voor de hier op volgende plots.')


# In[36]:


code6='''
driver_standings=pd.concat([driver_standings1, driver_standings2,driver_standings3,driver_standings4, driver_standings5, driver_standings6, driver_standings7, driver_standings8, driver_standings9, driver_standings10, driver_standings11, driver_standings12, driver_standings13, driver_standings14, driver_standings15, driver_standings16, driver_standings17, driver_standings18, driver_standings19, driver_standings20, driver_standings21, driver_standings22])
driver_standings=driver_standings.drop(labels=['positionText', 'Driver.code', 'FastestLap.AverageSpeed.units', 
                                               'Driver.url', 'Constructor.url', 'Driver.permanentNumber', 
                                               'Driver.driverId', 'Constructor.constructorId', 'Constructor.nationality'], axis=1)

driver_standings=driver_standings.rename(columns={'Driver.givenName': 'name', 'Driver.familyName': 'surname', 
                                                 'Driver.dateOfBirth': 'DoB', 'Driver.nationality': 'nationality', 
                                                  'Constructor.name': 'Constructor', 'Time.millis': 'time [ms]', 'Time.time': 'time',
                                                 'FastestLap.lap': 'fastest lap', 'FastestLap.Time.time': 'fastestLap time', 
                                                 'FastestLap.AverageSpeed.speed': 'fastest lap avr.speed', 
                                                  'FastestLap.rank': 'fastest lap rank'})'''
st.code(code6)


# In[37]:


driverstandings_sep=driver_standings.drop(labels=['name', 'DoB', 'nationality', 'time [ms]', 'time', 'fastest lap rank', 'fastest lap avr.speed'], axis=1)
st.dataframe(driverstandings_sep, width=1200)


# In[38]:


st.header('Team resultaten')


# In[39]:


st.write(
'In deze lijnplot is te zien hoe de coureurs onderling binnen een team presteren. '
'Door te kijken naar de resultaten per coureur in een team kan er worden gekeken '
'hoe goed zij aan elkaar gewaagd zijn. Ze rijden immers met dezelfde machine zou je '
'zeggen.'

' Het constructorteam kan geselecteerd worden via het dropdown menu om zo de resultaten '
'van de teamgenoten te zien.')


# In[40]:


code3='''
#Maak dropbdown list aan
constructor_list = driver_standings['Constructor'].unique()
Constructor = st.selectbox(label = "Kies een team", options=constructor_list)
query = f"Constructor=='{Constructor}'"

df_filtered = driver_standings.query(query)

#Maak line plot om weer te geven
fig= px.line(df_filtered, x='location', y='points', color='surname',  symbol='Constructor', 
             title='<b>verzicht punten per team<b>', height=800, width=800)

fig.update_xaxes(tickangle=45)
fig.update_layout(xaxis_title='', yaxis_title='Punten', legend_title_text='Driver & Constructor')

st.plotly_chart(fig, use_container_width=True)'''

st.code(code3)


# In[41]:


driver_standings['points']=pd.to_numeric(driver_standings['points'])

constructor_list = driver_standings['Constructor'].unique()
Constructor = st.selectbox(label = "Kies een team", options=constructor_list)
query = f"Constructor=='{Constructor}'"

df_filtered = driver_standings.query(query)
fig= px.line(df_filtered, x='location', y='points', color='surname',  symbol='Constructor', 
             title='<b>Overzicht punten per team<b>', height=800, width=850)

fig.update_xaxes(tickangle=45)
fig.update_layout(xaxis_title='', yaxis_title='Punten', legend_title_text='Driver & Constructor')

st.plotly_chart(fig, use_container_width=True)


# In[42]:


st.write(
'Hamilton en Verstappen waren het afgelopen seizoen de voornaamste titelkandidaten ' 
'en dit is ook te zien in de onderlinge verhoudingen binnen Mercedes en Red Bull. ')
st.write(
'Bottas (mercedes) en Perez(RedBull) zijn de tweede rijders binnen hun team.' 
' In de plot is te zien dat Bottas wat meer gewaagd is aan zijn teamgenoot dan ' 
'wanneer je Pérez vergelijkt met Verstappen. Pérez eindigde afgelopen seizoen ' 
'alleen hoger dan verstappen bij een resultaat van 0 punten van zijn teamgenoot.')
st.write(
'Bij Mclaren valt op dat de drivers redelijk aan elkaar gewaagd zijn.' 
' Norris eindigde weliswaar vaker boven Ricciardo, maar Ricciardo heeft de race op ' 
'Monza gewonnen. '
'Sainz en Leclerc van Ferrari zijn goed aan elkaar gewaagd en zie je dat hun punten ' 
'aantal elkaar afwisselen.')
st.write(    
'Binnen AlphaTauri is op te merken dat Gasly veruit een beter seizoen heeft gereden ' 
'dan ploeggenoot Tsunoda, met pieken van 15 of 12 punten. '
' Dit is echter het eerste seizoen van Tsunoda, dus wellicht gaan wij meer van zijn '
'potentie zien in de opvolgende seizoenen!')
st.write(
'Astin Martin heeft 2 rijders, die ook wel aan elkaar gewaagd zijn qua punten al valt ' 
'de score van Vettel meer op door zijn 2e plek (18 punten) in Baku. ')
st.write(
'De coureurs van Alpha Romeo zijn dit seizoen weinig in de punten terecht gekomen, ' 
'wel valt het op dat Raïkkönen dit seizoen meer punten heeft binnengehaald dan zijn teamgenoot. ' 
' Verder moest Kubica 2x invallen voor Kimi door een COVID besmetting.')
st.write(
'Ook de drivers van Alpine zijn goed tegen elkaar opgewassen, met een uitschieter van Ocon '
'naar de 1e plek in Budapest. ')
st.write(
'Williams heeft dit seizoen ook maar een enkele keer binnen kunnen halen. 4x Russel en 2x latifi. '
'Desondanks de resultaten van Russel krijgt hij komend seizoen de kans om zich te bewijzen in het '
'hoofdteam van Mercedes.') 
st.write(
'De huidige wagen van Williams kan niet op tegen de overige  teams om punten binnen te krijgen. ' 
'Dit ligt voornamelijk aan het kleine budget of moeten ze toch flink werken aan hun rij strategie? '
'Haas is dit seizoen het meest constant geweest wat betreft het aantal punten per race.' 
' Dat is ook niet moeilijk, aangezien ze dit seizoen geen punten wisten te bemachtigen.')


# In[43]:


st.header('Coureur(s) resultaten onder de loop')


# In[44]:


st.write(
'Nu dat de resultaten per team vergeleken zijn met elkaaris het tijd om de resultaten per coureur '
'onder de loop te nemen')
st.write(
'De hieronder weergegeven plot werkt als volgt; In de multiselect tool kunnen de locatie van ' 
'iedere wedstrijd worden geselecteerd. Wanneer er meer dan 1 locatie is geselecteerd komt er onder ' 
'aan de plot een slider te voorschijn. Deze slider zorgt er voor dat je makkelijk van locatie naar ' 
'locatie kan "sliden" om de resultaten per driver te bekijken en met elkaar te vergelijken'
)
st.write(
'Als default optie zijn de eerste race en de laatste race geselecteerd, maar deze kun je '
'natuurlijk weg halen en anders locaties selecteren'
)


# In[45]:


code= '''#slider per stad
location_options= driver_standings['location'].unique().tolist()
location= st.multiselect('Welke grand prix locatie(s) wil je weergeven? ', location_options, ['Sakhir', 'Abu Dhabi'])
driver_standings_location = driver_standings[driver_standings['location'].isin(location)]

plot_spot = st.empty() #Houd de spot vast voor de grafiek

# Barplot driver_standings
fig=px.bar(driver_standings_location, x='surname', y='points', color='surname', height=800, width=800, animation_frame='location', 
           labels={'surname': '',"points": "Verkregen punten"})
fig.update_layout(title='<b>Ontvangen punten per driver<b>') 
fig.update_xaxes(tickangle=45)

with plot_spot:
    st.plotly_chart(fig)'''
    
st.code(code)


# In[46]:


#set values to numeric values
driver_standings['points']= pd.to_numeric(driver_standings['points'])

location_options= driver_standings['location'].unique().tolist()
location= st.multiselect('Welke grand prix locatie(s) wil je weergeven? ', location_options, ['Sakhir', 'Abu Dhabi'])
driver_standings_location = driver_standings[driver_standings['location'].isin(location)]

plot_spot = st.empty() #Houd de spot vast voor de grafiek

# Barplot driver_standings
fig=px.bar(driver_standings_location, x='surname', y='points', color='surname', height=800, width=800, animation_frame='location', 
           labels={'surname': '',"points": "Verkregen punten"})
fig.update_layout(title='<b>Ontvangen punten per driver<b>') 
fig.update_xaxes(tickangle=45)

with plot_spot:
    st.plotly_chart(fig)


# In[47]:


st.write(
'Wat eigenlijk al in het begin op valt is dat je Verstappen en Hamilton qua punten heel erg om ' 
'elkaar heen ziet dansen. Ook is het opvallend dat wanneer Verstappen en Hamilton voor een bepaalde '
'race geen punten hebben binnen gehaald, zij ook in die race tegen elkaar op zijn geknalt. '
)
st.write(
'Het is ook interessant om naar een bepaalde race te kijken waar Hamilton of Verstappen een keer '
'niet met de kroon er vandoor gingen. De race een Baku of in Monza gaf een spannende twist in het seizoen'
'Of bij Budapest waarbij Ocon er met de prijs er vandaar ging.'
)
st.write(
'Ook is het interessant om te zien dat de grands prix locatie met veel rechte lange stukken vaak door een '
'Mercedes wordt gewonnen, dit is ook niet meer dan logisch als je kijkt naar hun motor en de bouw van de ' 
'formule 1 auto. Waarbij de Honda motor, die in de Red bulls zitten nog wel veel verliest op de rechte stukken.'
)


# In[48]:


st.header('Drivers status per wedstrijd')


# In[49]:


st.write(
'In dit stukje word er een scatter plot weergeven waarbij er gezien kan worden welke drivers er aanwezig waren op welke locatie en of deze gefinished zijn of niet. '
'Ook de reden waarom een driver niet gefinished is word weer geven in de scatter plot, zo heeft ieder puntje een eigen kleur en staat dat voor een reden. '
'Met behulp van dit plot kan er in een oogopslag gezien worden wie er wel of niet gefinished zijn. '
'Ook kan er makkelijk gezien worden door welke reden een drivers het vaaksts niet finishen.')


# In[50]:


code4='''
#Maak scatter plots aan
fig1 = px.scatter(driver_standings,x=driver_standings['surname'],y=driver_standings['location'],
                  color='status', title='<b>Status rapport per driver<b>', height=800, width=800)
fig1.update_layout(xaxis_title='', yaxis_title='Locatie', legend_title_text='Status')
fig1.update_xaxes(tickangle=45)

finished = driver_standings[driver_standings['status']=='Finished']
fig2 = px.scatter(finished,x=finished['surname'],y=finished['location'], title='<b>Status rapport per driver<b>', 
height=800, width=800)
fig2.update_layout(xaxis_title='', yaxis_title='Locatie', legend_title_text='Status')
fig2.update_xaxes(tickangle=45)

not_finished = driver_standings[driver_standings['status'] !='Finished']

fig3 = px.scatter(not_finished,x=not_finished['surname'],y=not_finished['location'],color='status', 
                  title='<b>Status rapport per driver<b>', height=800, width=800
                  ,category_orders={'surname':['Hamilton','Verstappen','Bottas','Norris','Pérez','Leclerc','Ricciardo',
                                               'Sainz','Tsunoda','Stroll','Räikkönen','Gasly','Ocon','Alonso', 
                                               'Vettel','Giovinazzi','Schumacher',
                                               'Mazepin','Latifi','Russel','Kubica']})
fig3.update_xaxes(tickangle=45)
fig3.update_layout(xaxis_title='', yaxis_title='Locatie', legend_title_text='Status')

#Maak de checkboxen aan
if st.checkbox("Finished"):
    st.write(fig2)
elif st.checkbox("Not Finished"):
    st.write(fig3)
else:
     st.write(fig1)                                               

'''
st.code(code4)


# In[51]:


fig1 = px.scatter(driver_standings,x=driver_standings['surname'],y=driver_standings['location'],
                  color='status', title='<b>Status rapport per coureur<b>', height=800, width=800)

fig1.update_layout(xaxis_title='', yaxis_title='Locatie', legend_title_text='Status')
fig1.update_xaxes(tickangle=45)


# In[52]:


finished = driver_standings[driver_standings['status']=='Finished']
fig2 = px.scatter(finished,x=finished['surname'],y=finished['location'], title='<b>Status rapport per coureur<b>',
                  height=800, width=800)

fig2.update_layout(xaxis_title='', yaxis_title='Locatie', legend_title_text='Status')
fig2.update_xaxes(tickangle=45)


# In[53]:


not_finished = driver_standings[driver_standings['status'] !='Finished']

fig3 = px.scatter(not_finished,x=not_finished['surname'],y=not_finished['location'],color='status', 
                  title='<b>Status rapport per coureur<b>', height=800, width=800
                  ,category_orders={'surname':['Hamilton','Verstappen','Bottas','Norris','Pérez','Leclerc','Ricciardo',
                                               'Sainz','Tsunoda','Stroll','Räikkönen','Gasly','Ocon','Alonso',
                                               'Vettel','Giovinazzi','Schumacher','Mazepin','Latifi','Russel','Kubica']})

fig3.update_layout(xaxis_title='', yaxis_title='Locatie', legend_title_text='Status')
fig3.update_xaxes(tickangle=45)


# In[54]:


st.write('Kies de status: ')
if st.checkbox("Finished"):
    st.write(fig2)
elif st.checkbox("Not Finished"):
    st.write(fig3)
else:
     st.write(fig1)


# In[55]:


st.write(
'De standaard plot laat zien welke drivers er aanwezig waren bij iedere locatie. '
'Wanneer er bij een driver geen puntje staat op een bepaalde locatie dan was deze driver niet aanwezig. '
'Zo was Räikkönen bijvoorbeeld niet aanwezig bij de Race in Zandvoort en de race in Monza. ')

st.write(
'Als er op de finished knop geklikt word komt de scatterplot te voorschijn waarin gezien kan worden welke drivers zijn gefinished bij iedere locatie. '
'Helemaal links komt de driver te staan die het vaaksts gefinished is. '
'Dat was dit seizoen Hamilton. '
'Helemaal rechts komt de driver te staan die het minst gefinished is. Dit is Kubica. '
'Wel moet er bij vermeld worden dat Kumica bij 2 races geraced heeft en daarom is het niet gek dat hij maar 1 keer gefinished is. '
'Russel daarin tegen was wel bij iedere race aanwezig en van de 22 races is hij 4 keer gefinished. '
'Opvallend is dat Hamilton vaker is gefinished dan Verstappen, maar uiteindelijk is Verstappen wel degene die dit seizoen wereldkampioen werd. ')

st.write(
'Bij de not finished scatter plot kan er gezien worden dat de meeste bolletjes de blauwe kleur hebben voor van +1 Lap. '
'Dit betekend dat de meest voorkomende reden voor het niet finishen is dat drivers gelapped worden. '
'Voor de rest zijn er heel veel issues die maar 1 keer voorkomen, bijvoorbeeld een Mechanical Issue. '
'Dat is dit seizoen 1 keer voorgekomen bij Ocon op de race van Austin. ' )

st.write(
'Er kan geconcludeerd worden dat je niet persee wereldkampioen word als je het vaaksts finished. '
'De meest voorkomende reden voor het niet Finishen is wanneer je gelapped word. '
'De andere reden komen bijna altijd maar 1 keer voor.')


# In[56]:


st.header('De snelste lap tijden met elkaar vergelijken')


# In[57]:


st.write(
'In dit stukje worden de laptijden van allen wedstrijden per driver met elkaar vergeleken in de plot hieronder is niet alleen een scatter plot te zien, maar wordt er naast ook een ' 
'boxplot weergegeven. Deze kan ons meer inzicht geven in de gemiddelde slelste tijd en of een hele snelle lap tijd in vloed zou kunnen hebben op de uiteindelijke uitslag?'
)

st.write(
'Klopt het dan ook dat the "big three" de snelste laptijden hebben gereden?'
)

st.write(
'De plot kan met de multiselecter weergeven welke coureurs te met elkaar wilt vergelijken of alleen van een coureur weergegeven.'
)


# In[58]:


code2='''
#converteer de lap tijden zodat de plot deze erkent als een tijd
driver_standings['fastestLap time']= pd.to_datetime(driver_standings['fastestLap time'])

#Maak selectbox om de verschillende drivers te selecteren
driver_options= driver_standings['surname'].unique().tolist()
driver= st.multiselect('Welke driver(s) wil je weergeven? ', driver_options, ['Hamilton', 'Verstappen', 'Bottas'])
driver_standings_driver = driver_standings[driver_standings['surname'].isin(driver)]

plot_spot = st.empty() #Houd de spot vast voor de grafiek

#scatter en marginal plot om de snelste laps per driver per locatie met elkaar te vergelijken
fig=px.scatter(driver_standings_driver, x='location', y='fastestLap time', height=700, width=800, color='surname', 
               marginal_y='box', labels={'location': '', 'fastestLap time': 'Tijd [min]'})
fig.update_layout(title='<b>Snelste lap tijden per locatie<b>')
fig.update_xaxes(tickangle=45)

with plot_spot:
    st.plotly_chart(fig)

'''
st.code(code2)


# In[59]:


#converteer de lap tijden zodat de plot deze erkent als een tijd
driver_standings['fastestLap time']= pd.to_datetime(driver_standings['fastestLap time'])

#Maak selectbox om de verschillende drivers te selecteren
driver_options= driver_standings['surname'].unique().tolist()
driver= st.multiselect('Welke driver(s) wil je weergeven? ', driver_options, ['Hamilton', 'Verstappen', 'Bottas'])
driver_standings_driver = driver_standings[driver_standings['surname'].isin(driver)]


plot_spot = st.empty() #Houd de spot vast voor de grafiek

#scatter en marginal plot om de snelste laps per driver per locatie met elkaar te vergelijken
fig=px.scatter(driver_standings_driver, x='location', y='fastestLap time', height=700, width=800, color='surname', 
               marginal_y='box', labels={'location': '', 'fastestLap time': 'Tijd [min]'})
fig.update_layout(title='<b>Snelste lap tijden per locatie<b>')
fig.update_xaxes(tickangle=45)

with plot_spot:
    st.plotly_chart(fig)


# In[60]:


st.write(
'Wanneer je naar de plot kijkt en de coureurs vergelijkt die bijna altijd in de punten vallen '
'zoals Hamilton en Verstappen en de coureurs pakt die vaak niet in de punten vallen '
'zoals Latifi en Mazepin, klopt het ook wel en is het ook logisch dat Hamilton en Verstappen '
'vaker hoger eindigen op de punten lijst.'
)

st.write(
'Maar als je Hamiltion vergelijkt met Verstappen rijdt Hamilton minder vaak de snelste ronde en '
'en pakt Verstappen de titel voor snelste ronde, vooral op de tracks waar veel bochten in zitten. '
'Hier is het lange frame van de Mercedes auto niet voor opgewassen.'
)

st.write(
'Wat opvalt is dat Verstappen en Pérez wel dichtbij elkaar zitten qua "snelste lap tijd" maar dat '
'Verstappen dit toch vaker aantikt dan Pérez. Beide rijden met dezelfde auto of tenminste daar ga '  
'je vanuit. Heeft dit verschil te maken dat de twee coureurs een andere rijstrtegie hebben? Of zou '
'toch kunnen concluderen dat Verstappen beter is of wel sneller.'
)


# In[61]:


st.header('Start positie en eind positie onder de loop')


# In[62]:


st.write(
'In het dataframe is informatie te zien over de positie van elke racer in de wedstrijd. '
'In de kolom ‘Grid position’ is de startpositie van een racer te zien en in de '
'kolom ‘End position’ is te zien als hoeveelste de racer over de finish ging. '
'Het verschil hiertussen, dus hoeveel plekken een racer omhoog of omlaag is gegaan bij de '
'finish ten opzichte van zijn startpositie, is te zien in de kolom ‘Position Progress’. ' 
'Deze informatie kan bekeken worden voor elke wedstrijd van 2021, door een race te selecteren op de stad '
'waar deze plaatsvond, in het ‘Race City’-menu.'
)


# In[63]:


code5='''
#Creeër streamlit dataframe en radio buttons
race_options = driver_standings['location'].unique().tolist()
select_race_option = st.radio('Kies je locatie', race_options) #label='Race locatie', options = race_options)
grid_position_diff2= driver_standings[driver_standings['location']==select_race_option]


#Creeër dataframe voor grid, position, and grid/position progress
grid_position_diff2 = grid_position_diff2[['location', 'grid', 'position', 'surname']]
grid_position_diff2['grid'] = grid_position_diff2['grid'].astype(int)
grid_position_diff2['position'] = grid_position_diff2['position'].astype(int)


grid_position_diff2['position progress'] = grid_position_diff2['grid'] - grid_position_diff2['position']
grid_position_diff2['position progress'] = grid_position_diff2['position progress'].astype(str)
grid_position_diff2.rename({'surname': 'Driver', 'grid': 'Grid position', 'position': 'End position', 'position progress': 'Position Progress', 'location':'Location'}, axis = 1, inplace = True)
grid_position_diff2 = grid_position_diff2.set_index('Driver')

st.dataframe(grid_position_diff2, height=700)
'''

st.code(code5)


# In[64]:


#Creeër streamlit dataframe en radio buttons
race_options = driver_standings['location'].unique().tolist()
select_race_option = st.radio('Kies je locatie', race_options) #label='Race locatie', options = race_options)
grid_position_diff2= driver_standings[driver_standings['location']==select_race_option]


#Creeër dataframe voor grid, position, and grid/position progress
grid_position_diff2 = grid_position_diff2[['location', 'grid', 'position', 'surname']]
grid_position_diff2['grid'] = grid_position_diff2['grid'].astype(int)
grid_position_diff2['position'] = grid_position_diff2['position'].astype(int)


grid_position_diff2['position progress'] = grid_position_diff2['grid'] - grid_position_diff2['position']
grid_position_diff2['position progress'] = grid_position_diff2['position progress'].astype(str)
grid_position_diff2.rename({'surname': 'Driver', 'grid': 'Grid position', 'position': 'End position', 'position progress': 'Position Progress', 'location':'Location'}, axis = 1, inplace = True)
grid_position_diff2 = grid_position_diff2.set_index('Driver')

st.dataframe(grid_position_diff2, height=700)


# In[65]:


st.write(
'Opvallend zijn de soms grote verschillen tussen de start- en eindpositie van een racer bij '
'een bepaalde wedstrijd. Zo begon Gasly op plek 5 bij de eerste wedstrijd van 2021, in Sakhir, '
'maar eindigde hij hier op plaats 17. Alonso daalde ook flink, van plek 9 naar plek 19. '
)
    
st.write(
'Ook bij de wedstrijd in Spa valt er iets op. De racers met startpositie 1 t/m 6, eindigden allemaal '
'op dezelfde plek als waarop ze begonnen en de racers met startpositie 7 t/m 17 gingen allemaal één plek '
'omhoog ten opzichte van hun startpositie. '
)


# In[66]:


st.subheader('Bedankt voor het lezen van onze blog!')

