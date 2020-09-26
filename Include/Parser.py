import json
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt


class parser :

  def __init__(self):
    self.nomi = {""}

  def leggi(self):
    text = ""
    numeri = ""
    nomiConsentiti = ['Marco','Cella','ᛗᚫᛋᛏᚫᚻ (Master)','Zenkys','Stefanone','Digio']
    numeroMessaggiUtente = {'Marco':0,'Cella':0,'ᛗᚫᛋᛏᚫᚻ (Master)':0,'Zenkys':0,'Stefanone':0,'Digio':0}
    numeroStickersUtente = {'Marco':0,'Cella':0,'ᛗᚫᛋᛏᚫᚻ (Master)':0,'Zenkys':0,'Stefanone':0,'Digio':0}
    numeroImmaginiUtente = {'Marco':0,'Cella':0,'ᛗᚫᛋᛏᚫᚻ (Master)':0,'Zenkys':0,'Stefanone':0,'Digio':0}
    paroleNonConsentite = ['sono','anche','della','dello','l\'ho','come','quando','cosa','delle','solo','perché',
                           'tipo','quello','fatto','tutti','comunque','tutto','della','questa','quella','questo',
                           'hanno','però','così','essere','alla','dalla','aveva','cioè','stato','nella','avevo',
                           'prima','ancora','senza','dopo','quindi','fare','sempre','fosse','altro','allora','alle',
                           'forse','qualcosa','quelli','credo','fanno','faccio','avere','l\'altro','avete','perchè',
                           'erano','quale','quelle','quanto','sulla','aver','quel','nelle']
    with open('result.json',encoding='utf8') as f:
      data = json.load(f)

    for gruppo in data['chats']['list']:
      if gruppo['name']=="Blitz Krieg":
        for messaggi in gruppo['messages']:
          if(messaggi['type']=="message"):
            if (isinstance(messaggi['text'],str)):
              if(messaggi['from'] in nomiConsentiti):
                numeroMessaggiUtente[messaggi['from']] += 1
                if(messaggi['text']==""):
                    if('media_type' in messaggi and messaggi['media_type']=="sticker"):
                        numeroStickersUtente[messaggi['from']] += 1
                    if('photo' in messaggi):
                        numeroImmaginiUtente[messaggi['from']] += 1

                #temp = messaggi['text'].lower().split()
                #for string in temp:
                #  if(len(string)>3 and string not in paroleNonConsentite):
                #    text += string+" "

    #wordcloud = WordCloud(width=3200,height=1600).generate(text).to_file('blitzkrieg2.png')
    y_pos = np.arange(len(nomiConsentiti))
    plt.bar(y_pos, numeroMessaggiUtente.values())
    plt.xticks(y_pos, ['Marco\n'+str(numeroMessaggiUtente['Marco']),
                       'Cella\n'+str(numeroMessaggiUtente['Cella']),
                        'ᛗᚫᛋᛏᚫᚻ (Master)\n'+str(numeroMessaggiUtente['ᛗᚫᛋᛏᚫᚻ (Master)']),
                        'Zenkys\n'+str(numeroMessaggiUtente['Zenkys']),
                        'Stefanone\n'+str(numeroMessaggiUtente['Stefanone']),
                        'Digio\n'+str(numeroMessaggiUtente['Digio'])])
    plt.show()
    y_pos = np.arange(len(nomiConsentiti))
    plt.bar(y_pos, numeroStickersUtente.values())
    plt.xticks(y_pos, ['Marco\n' + str(numeroStickersUtente['Marco']),
                       'Cella\n' + str(numeroStickersUtente['Cella']),
                       'ᛗᚫᛋᛏᚫᚻ (Master)\n' + str(numeroStickersUtente['ᛗᚫᛋᛏᚫᚻ (Master)']),
                       'Zenkys\n' + str(numeroStickersUtente['Zenkys']),
                       'Stefanone\n' + str(numeroStickersUtente['Stefanone']),
                       'Digio\n' + str(numeroStickersUtente['Digio'])])
    plt.show()
    y_pos = np.arange(len(nomiConsentiti))
    plt.bar(y_pos, numeroImmaginiUtente.values())
    plt.xticks(y_pos, ['Marco\n' + str(numeroImmaginiUtente['Marco']),
                       'Cella\n' + str(numeroImmaginiUtente['Cella']),
                       'ᛗᚫᛋᛏᚫᚻ (Master)\n' + str(numeroImmaginiUtente['ᛗᚫᛋᛏᚫᚻ (Master)']),
                       'Zenkys\n' + str(numeroImmaginiUtente['Zenkys']),
                       'Stefanone\n' + str(numeroImmaginiUtente['Stefanone']),
                       'Digio\n' + str(numeroImmaginiUtente['Digio'])])
    plt.show()

    print("Messaggi Marco",numeroMessaggiUtente['Marco'])
    print("Messaggi Cella", numeroMessaggiUtente['Cella'])
    print("Messaggi ᛗᚫᛋᛏᚫᚻ (Master)", numeroMessaggiUtente['ᛗᚫᛋᛏᚫᚻ (Master)'])
    print("Messaggi Stefanone", numeroMessaggiUtente['Stefanone'])
    print("Messaggi Digio", numeroMessaggiUtente['Digio'])
    print("Sticker Marco", numeroStickersUtente['Marco'])
    print("Sticker Cella", numeroStickersUtente['Cella'])
    print("Sticker ᛗᚫᛋᛏᚫᚻ (Master)", numeroStickersUtente['ᛗᚫᛋᛏᚫᚻ (Master)'])
    print("Sticker Stefanone", numeroStickersUtente['Stefanone'])
    print("Sticker Digio", numeroStickersUtente['Digio'])
    print("Immagini Marco", numeroImmaginiUtente['Marco'])
    print("Immagini Cella", numeroImmaginiUtente['Cella'])
    print("Immagini ᛗᚫᛋᛏᚫᚻ (Master)", numeroImmaginiUtente['ᛗᚫᛋᛏᚫᚻ (Master)'])
    print("Immagini Stefanone", numeroImmaginiUtente['Stefanone'])
    print("Immagini Digio", numeroImmaginiUtente['Digio'])













