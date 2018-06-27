import telepot
import json
from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

#!/usr/bin/python
#coding: UTF-8

load = open("token.json")   # Lendo o Json que contém o token do bot
token = json.loads(load.read()) # Inserindo o token bot a variavel "token"
bot = telepot.Bot(token['token'])   # Inserindo o token no Bot

'''SOBRE: condicoes
Pega o a interacao do usuario (via mensagem ou botao), e faz alguma tomada de acao
'''

def condicoes(chatID, msg):

            S_CM_salvar = False
            S_GL_salvar = False
            S_ST_salvar = False
            #while (msg != 'sair'):
            if(msg == '/start'):
                        inicio(chatID, bot)
                        
########################## SERIES ##########################

            ### Escolha Principal ###
            elif(msg == "Series"):
                    bot.sendMessage(
                        chatID,
                        "Funções Disponiveis para séries",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Salvar Episódio", callback_data='SE')],
                                [InlineKeyboardButton(text="Verificar Episódio", callback_data='VE')],
                                [InlineKeyboardButton(text="Episódio Salvo", callback_data='ES')],
                            ]
                        )
                    )

            ### END Escolha Principal ###

            ### Verificar Episodio salvo ###

            elif (msg == 'ES'):
                    txt1 = open('Atualizacao/CriminalMinds/EPCM.txt','r')       #Abre o arquivo que armazena o episódio salvo
                    txt2 = open('Atualizacao/Glitch/EPGL.txt','r')              #Abre o arquivo que armazena o episódio salvo
                    txt3 = open('Atualizacao/StrangerThings/EPST.txt','r')      #Abre o arquivo que armazena o episódio salvo
                    bot.sendMessage(chatID,txt1.read(),'Markdown')          #Exibe o episódio salvo
                    bot.sendMessage(chatID,txt2.read(),'Markdown')          #Exibe o episódio salvo
                    bot.sendMessage(chatID,txt3.read(),'Markdown')          #Exibe o episódio salvo
                    txt1.close()
                    txt2.close()
                    txt3.close()
                    inicio(chatID,bot)

            ### END Verificação de episodio salvo ###
                        
            ### Salvar Episódios ###
            elif(msg == 'SE'):
                        bot.sendMessage(
                        chatID,
                        "Series disponiveis no momento",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Criminal Minds", callback_data='S_CM')],
                                [InlineKeyboardButton(text="Glitch", callback_data='S_GL')],
                                [InlineKeyboardButton(text="Stranger Things", callback_data='S_ST')]
                            ]
                        )
                        )
                
            ### Salvar EP Criminal Minds ###                

            elif(msg == 'S_CM'):    #Solicita confirmação de série
                   bot.sendMessage(
                        chatID,
                        "Serie selecionada: Criminal Minds",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Continuar", callback_data='S_CM_salvar')],
                                [InlineKeyboardButton(text="Cancelar", callback_data='Series')],
                            ]
                        )
                        )
            elif(msg == 'S_CM_salvar'):     #Seleção de temporadas
                        bot.sendMessage(
                        chatID,
                        "Temporada Disponíveis",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Temporada 1", callback_data='CM_T1_salvar')],
                                [InlineKeyboardButton(text="Temporada 2", callback_data='CM_T2_salvar')],
                            ]
                        )
                        )


            elif (msg == 'CM_T1_salvar'):       #Seleção de episódios da temporada selecionada
                        bot.sendMessage(
                        chatID,
                        "Episódios Disponíveis (Criminal Minds 1 Temp)",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Episodio 1", callback_data='CM Temporada 1 Episodio 1')],
                                [InlineKeyboardButton(text="Episodio 2", callback_data='CM Temporada 1 Episodio 2')],
                                [InlineKeyboardButton(text="Episodio 3", callback_data='CM Temporada 1 Episodio 3')],
                                [InlineKeyboardButton(text="Episodio 4", callback_data='CM Temporada 1 Episodio 4')],
                                [InlineKeyboardButton(text="Episodio 5", callback_data='CM Temporada 1 Episodio 5')],
                                [InlineKeyboardButton(text="Episodio 6", callback_data='CM Temporada 1 Episodio 6')],
                                [InlineKeyboardButton(text="Episodio 7", callback_data='CM Temporada 1 Episodio 7')],
                                [InlineKeyboardButton(text="Episodio 8", callback_data='CM Temporada 1 Episodio 8')],
                                [InlineKeyboardButton(text="Episodio 9", callback_data='CM Temporada 1 Episodio 9')],
                                [InlineKeyboardButton(text="Episodio 10", callback_data='CM Temporada 1 Episodio 10')],
                                [InlineKeyboardButton(text="Episodio 11", callback_data='CM Temporada 1 Episodio 11')],
                                [InlineKeyboardButton(text="Episodio 12", callback_data='CM Temporada 1 Episodio 12')],
                                [InlineKeyboardButton(text="Episodio 13", callback_data='CM Temporada 1 Episodio 13')],
                                [InlineKeyboardButton(text="Episodio 14", callback_data='CM Temporada 1 Episodio 14')],
                                [InlineKeyboardButton(text="Episodio 15", callback_data='CM Temporada 1 Episodio 15')],
                                [InlineKeyboardButton(text="Episodio 16", callback_data='CM Temporada 1 Episodio 16')],
                                [InlineKeyboardButton(text="Episodio 17", callback_data='CM Temporada 1 Episodio 17')],
                                [InlineKeyboardButton(text="Episodio 18", callback_data='CM Temporada 1 Episodio 18')],
                                [InlineKeyboardButton(text="Episodio 19", callback_data='CM Temporada 1 Episodio 19')],
                                [InlineKeyboardButton(text="Episodio 20", callback_data='CM Temporada 1 Episodio 20')],
                                [InlineKeyboardButton(text="Episodio 21", callback_data='CM Temporada 1 Episodio 21')],
                                [InlineKeyboardButton(text="Episodio 22", callback_data='CM Temporada 1 Episodio 22')],
                                [InlineKeyboardButton(text="Episodio 23", callback_data='CM Temporada 1 Episodio 23')],
                                [InlineKeyboardButton(text="Episodio 24", callback_data='CM Temporada 1 Episodio 24')],
                            ]
                        )
                        )
            
            #Atualiza o episódio salvo de acordo com a seleção
            elif(msg == 'CM Temporada 1 Episodio 1'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 2'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 3'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 4'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'TCM emporada 1 Episodio 5'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 6'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 7'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 8'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 9'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()

            elif(msg == 'CM Temporada 1 Episodio 10'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 11'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 12'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 13'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 14'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 15'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 16'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 17'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 18'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 19'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 20'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 21'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 22'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 23'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 24'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif (msg == 'CM_T2_salvar'):       #Seleção de episódios da temporada selecionada
                        bot.sendMessage(
                        chatID,
                        "Episódios Disponíveis (Criminal Minds 2 Temp)",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Episodio 1", callback_data='CM Temporada 2 Episodio 1')],
                                [InlineKeyboardButton(text="Episodio 2", callback_data='CM Temporada 2 Episodio 2')],
                                [InlineKeyboardButton(text="Episodio 3", callback_data='CM Temporada 2 Episodio 3')],
                                [InlineKeyboardButton(text="Episodio 4", callback_data='CM Temporada 2 Episodio 4')],
                                [InlineKeyboardButton(text="Episodio 5", callback_data='CM Temporada 2 Episodio 5')],
                                [InlineKeyboardButton(text="Episodio 6", callback_data='CM Temporada 2 Episodio 6')],
                                [InlineKeyboardButton(text="Episodio 7", callback_data='CM Temporada 2 Episodio 7')],
                                [InlineKeyboardButton(text="Episodio 8", callback_data='CM Temporada 2 Episodio 8')],
                                [InlineKeyboardButton(text="Episodio 9", callback_data='CM Temporada 2 Episodio 9')],
                                [InlineKeyboardButton(text="Episodio 10", callback_data='CM Temporada 2 Episodio 10')],
                                [InlineKeyboardButton(text="Episodio 11", callback_data='CM Temporada 2 Episodio 11')],
                                [InlineKeyboardButton(text="Episodio 12", callback_data='CM Temporada 2 Episodio 12')],
                                [InlineKeyboardButton(text="Episodio 13", callback_data='CM Temporada 2 Episodio 13')],
                                [InlineKeyboardButton(text="Episodio 14", callback_data='CM Temporada 2 Episodio 14')],
                                [InlineKeyboardButton(text="Episodio 15", callback_data='CM Temporada 2 Episodio 15')],
                                [InlineKeyboardButton(text="Episodio 16", callback_data='CM Temporada 2 Episodio 16')],
                                [InlineKeyboardButton(text="Episodio 17", callback_data='CM Temporada 2 Episodio 17')],
                                [InlineKeyboardButton(text="Episodio 18", callback_data='CM Temporada 2 Episodio 18')],
                                [InlineKeyboardButton(text="Episodio 19", callback_data='CM Temporada 2 Episodio 19')],
                                [InlineKeyboardButton(text="Episodio 20", callback_data='CM Temporada 2 Episodio 20')],
                                [InlineKeyboardButton(text="Episodio 21", callback_data='CM Temporada 2 Episodio 21')],
                                [InlineKeyboardButton(text="Episodio 22", callback_data='CM Temporada 2 Episodio 22')],
                                [InlineKeyboardButton(text="Episodio 23", callback_data='CM Temporada 2 Episodio 23')],
                                [InlineKeyboardButton(text="Episodio 24", callback_data='CM Temporada 2 Episodio 24')],
                            ]
                        )
                        )
             
            #Atualiza o episódio salvo de acordo com a seleção
            elif(msg == 'CM Temporada 2 Episodio 1'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 2'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 3'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 4'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'TCM emporada 1 Episodio 5'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 6'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 7'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 8'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 9'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()

            elif(msg == 'CM Temporada 2 Episodio 10'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 11'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 12'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 13'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')   
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 14'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')   
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 15'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 16'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 17'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 18'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 19'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 20'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 21'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 22'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 2 Episodio 23'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')   
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'CM Temporada 1 Episodio 24'):
                    txt = open('Atualizacao/CriminalMinds/EPCM.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            ### END Salvar Criminal Minds ###

            ### Seleção da Serie Glitch ###

            elif(msg == 'S_GL'):    #Solicita confirmação de série
                   bot.sendMessage(
                        chatID,
                        "Series selecionada: Glitch",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Continuar", callback_data='S_GL_salvar')],
                                [InlineKeyboardButton(text="Cancelar", callback_data='Series')],
                            ]
                        )
                        )
            elif(msg == 'S_GL_salvar'):     #Seleção de temporadas
                        bot.sendMessage(
                        chatID,
                        "Temporada Disponíveis",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Temporada 1", callback_data='GL_T1_salvar')]
                            ]
                        )
                        )


            elif (msg == 'GL_T1_salvar'):       #Seleção de episódios da temporada selecionada
                        bot.sendMessage(
                        chatID,
                        "Episódios Disponíveis (Glitch 1 Temp)",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Episodio 1", callback_data='GL Temporada 1 Episodio 1')],
                                [InlineKeyboardButton(text="Episodio 2", callback_data='GL Temporada 1 Episodio 2')],
                                [InlineKeyboardButton(text="Episodio 3", callback_data='GL Temporada 1 Episodio 3')],
                                [InlineKeyboardButton(text="Episodio 4", callback_data='GL Temporada 1 Episodio 4')],
                                [InlineKeyboardButton(text="Episodio 5", callback_data='GL Temporada 1 Episodio 5')],
                                [InlineKeyboardButton(text="Episodio 6", callback_data='GL Temporada 1 Episodio 6')],
                                [InlineKeyboardButton(text="Episodio 7", callback_data='GL Temporada 1 Episodio 7')],
                                [InlineKeyboardButton(text="Episodio 8", callback_data='GL Temporada 1 Episodio 8')],
                                [InlineKeyboardButton(text="Episodio 9", callback_data='GL Temporada 1 Episodio 9')],
                                [InlineKeyboardButton(text="Episodio 10", callback_data='GL Temporada 1 Episodio 10')],
                                [InlineKeyboardButton(text="Episodio 11", callback_data='GL Temporada 1 Episodio 11')],
                                [InlineKeyboardButton(text="Episodio 12", callback_data='GL Temporada 1 Episodio 12')],
                            ]
                        )
                        )
            
            #Atualiza o episódio salvo de acordo com a seleção
            elif(msg == 'GL Temporada 1 Episodio 1'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 2'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 3'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 4'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'TCM emporada 1 Episodio 5'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 6'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 7'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')  
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 8'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 9'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+') 
                    txt.write(msg)
                    txt.close()

            elif(msg == 'GL Temporada 1 Episodio 10'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 11'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'GL Temporada 1 Episodio 12'):
                    txt = open('Atualizacao/Glitch/EPGL.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            ### END Salvar Glitch ###

           ### Salvar Stranger Things ###
            elif(msg == 'S_ST'):    #Solicita confirmação de série
                   bot.sendMessage(
                        chatID,
                        "Series selecionada: Stranger Things",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Continuar", callback_data='S_ST_salvar')],
                                [InlineKeyboardButton(text="Cancelar", callback_data='Series')],
                            ]
                        )
                        )
            elif(msg == 'S_ST_salvar'):     #Seleção de temporadas
                        bot.sendMessage(
                        chatID,
                        "Temporada Disponíveis",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Temporada 1", callback_data='ST_T1_salvar')],
                                [InlineKeyboardButton(text="Temporada 2", callback_data='ST_T2_salvar')],
                            ]
                        )
                        )

            elif (msg == 'ST_T1_salvar'):       #Seleção de episódios da temporada selecionada
                        bot.sendMessage(
                        chatID,
                        "Episódios Disponíveis (Stranger Things 1 Temp)",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Episodio 1", callback_data='ST Temporada 1 Episodio 1')],
                                [InlineKeyboardButton(text="Episodio 2", callback_data='ST Temporada 1 Episodio 2')],
                                [InlineKeyboardButton(text="Episodio 3", callback_data='ST Temporada 1 Episodio 3')],
                                [InlineKeyboardButton(text="Episodio 4", callback_data='ST Temporada 1 Episodio 4')],
                                [InlineKeyboardButton(text="Episodio 5", callback_data='ST Temporada 1 Episodio 5')],
                                [InlineKeyboardButton(text="Episodio 6", callback_data='ST Temporada 1 Episodio 6')],
                                [InlineKeyboardButton(text="Episodio 7", callback_data='ST Temporada 1 Episodio 7')],
                                [InlineKeyboardButton(text="Episodio 8", callback_data='ST Temporada 1 Episodio 8')],]))
                    
            #Atualiza o episódio salvo de acordo com a seleção
            elif(msg == 'ST Temporada 1 Episodio 1'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 1 Episodio 2'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 1 Episodio 3'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 1 Episodio 4'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')   
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'TCM emporada 1 Episodio 5'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+') 
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 1 Episodio 6'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 1 Episodio 7'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 1 Episodio 8'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif (msg == 'ST_T2_salvar'):       #Seleção de episódios da temporada selecionada
                        bot.sendMessage(
                        chatID,
                        "Episódios Disponíveis (Stranger Things 2 Temp)",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Episodio 1", callback_data='ST Temporada 2 Episodio 1')],
                                [InlineKeyboardButton(text="Episodio 2", callback_data='ST Temporada 2 Episodio 2')],
                                [InlineKeyboardButton(text="Episodio 3", callback_data='ST Temporada 2 Episodio 3')],
                                [InlineKeyboardButton(text="Episodio 4", callback_data='ST Temporada 2 Episodio 4')],
                                [InlineKeyboardButton(text="Episodio 5", callback_data='ST Temporada 2 Episodio 5')],
                                [InlineKeyboardButton(text="Episodio 6", callback_data='ST Temporada 2 Episodio 6')],
                                [InlineKeyboardButton(text="Episodio 7", callback_data='ST Temporada 2 Episodio 7')],
                                [InlineKeyboardButton(text="Episodio 8", callback_data='ST Temporada 2 Episodio 8')],
                                [InlineKeyboardButton(text="Episodio 9", callback_data='ST Temporada 2 Episodio 9')],]
                        )
                        )
                    
            #Atualiza o episódio salvo de acordo com a seleção
            elif(msg == 'ST Temporada 2 Episodio 1'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 2 Episodio 2'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 2 Episodio 3'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 2 Episodio 4'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'TCM emporada 1 Episodio 5'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 2 Episodio 6'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 2 Episodio 7'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 2 Episodio 8'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            elif(msg == 'ST Temporada 2 Episodio 9'):
                    txt = open('Atualizacao/StrangerThings/EPST.txt','r+')    
                    txt.write(msg)
                    txt.close()
                    inicio(chatID,bot)

            ### END Salvar Stranger Things ###

            

            ### Verificar Episódios, ver as sinopses dos episodios ###
            elif(msg == 'VE'):
                        bot.sendMessage(
                        chatID,
                        "Series disponiveis no momento",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Criminal Minds", callback_data='CM')],
                                [InlineKeyboardButton(text="Glitch", callback_data='GL')],
                                [InlineKeyboardButton(text="Stranger Things", callback_data='ST')]
                            ]
                        )
                        )

            ### Escolha de Criminal Minds ###
            elif(msg == 'CM'):
                    bot.sendMessage(
                        chatID,
                        "Temporadas Disponiveis",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Temporada 1", callback_data='CMTP1')],
                                [InlineKeyboardButton(text="Temporada 2", callback_data='CMTP2')]
                            ]
                        )
                    )
                    
            elif(msg == 'CMTP1'):
                    txt = open('Sinopses/CriminalMinds/cm1.md','r')    #Abre o arquivo que vai falar sobre os eps das séries
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif(msg == 'CMTP2'):
                    txt = open('Sinopses/Criminal/cm2.md','r')    #Abre o arquivo que vai falar sobre os eps das séries
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()
                    
            ### Escolha de Stranger Things ###
            elif(msg == 'ST'):
                    bot.sendMessage(
                        chatID,
                        "Temporadas Disponiveis",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Temporada 1", callback_data='TP1')],
                                [InlineKeyboardButton(text="Temporada 2", callback_data='TP2')]
                            ]
                        )
                    )
            elif(msg == 'TP1'):
                    txt = open('Sinopses/StrangerThing/st1.md','r')    #Abre o arquivo que vai falar sobre os eps das séries
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif(msg == 'TP2'):
                    txt = open('Sinopses/StrangerThing/st2.md','r')    #Abre o arquivo que vai falar sobre os eps das séries
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()
            

            ### Escolha de Glitch ###
            elif(msg == 'GL'):
                    bot.sendMessage(
                        chatID,
                        "Temporadas Disponiveis",
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[
                                [InlineKeyboardButton(text="Temporada 1", callback_data='GLTP1')],
                                [InlineKeyboardButton(text="Temporada 2", callback_data='GLTP2')]
                            ]
                        )
                    )
            elif(msg == 'GLTP1'):
                    txt = open('Sinopses/Glitch/g1.md','r')    #Abre o arquivo que vai falar sobre os eps das séries
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()

            elif(msg == 'GLTP2'):
                    txt = open('Sinopses/Glitch/g2.md','r')    #Abre o arquivo que vai falar sobre os eps das séries
                    bot.sendMessage(chatID,txt.read(),'Markdown')
                    txt.close()
            ####################################

##########################################################################################################

            elif (msg == 'Voltar'):
                    inicio(chatID, bot)

'''SOBRE: callback
O parametro desta funcao eh um Json enviado do message_loop com os campos referente a interacao feita via a chave 'callback_query', ou seja, esta funcao eh responsavel por
por pegar o que foi emitido pelo usuario (texto iniline_keyboard) e seu respectivo ID, e repassar para a funcao 'condicoes' e que sera processado a requisicao
e sera emitido o devido comportamento que o usuario quer em relacao ao bot
'''
def callback(msg):
            query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")
            #Forma facilitada pela biblioteca "telepot" de quebrar inserir as informacoes para as respectivas variaveis
            #Ou seja, pega o Json com a chave callback_queryt' e quebra as informacoes em tres jogando o valor de 'text' para a variavel tipoMsg,
            #assim por adiante...

            chatID = from_id
            #ID do usuario que apertou o botao

            texto = query_data
            #o valor do botao que foi apertado

            print(chatID)

            bot.answerCallbackQuery(query_id, text="Espere, estou trabalhando nisso!")
            #retorna um POP-UP para o usuario quando ele digitou alguma coisa

            print("callback query", query_id, from_id, query_data)

            condicoes(chatID, texto)
            # pega o que foi clicado pelo usuario (callback_data) e seu ID manda para a funcao 'condicoes' que vai processar o clique


'''SOBRE: ir
O parametro desta funcao eh um Json enviado do message_loop com os campos referente a interacao via a chave 'chat', ou seja, esta funcao eh responsavel por
por pegar o que foi emitido pelo usuario (texto via mensagem) e seu respectivo ID, e repassar para a funcao  'condicoes' e que sera processado a requisicao
e sera emitido o devido comportamento que o usuario quer em relacao ao bot
'''
def ir(msg):
            #Forma facilitada pela biblioteca "telepot" de quebrar inserir as informacoes para as respectivas variaveis
            #Ou seja, pega o Json com a chave 'chat' e quebra as informacoes em tres jogando o valor de 'text' para a variavel tipoMsg,
            #assim por adiante...
            tipoMsg, tipoChat, chatID = telepot.glance(msg)

            texto = msg['text']     #variavel Auxiliar para receber a texto que o usuario digitou, fiz ela porque se eu chamasse --condicoes(chatID, msg['text'])--
                                    #tava dando erro

            condicoes(chatID, texto)    # pega o que foi digitado pelo usuario e seu ID manda para a funcao 'condicoes' que vai processar o a mensagem

'''SOBRE: inico
Esta funcao eh uma forma de facilitar o a primeira interacao ao usuario
'''
def inicio(chatID, bot):
            keyboard=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                #KeyboardButton(text="Atualizar Episodio"),
                                #KeyboardButton(text="Verificar Episodio"),
                                KeyboardButton(text="Ajuda"),
                                KeyboardButton(text="Series")
                            ]
                        ],resize_keyboard=True
                    )

            txt = open('Inicializacao/Hello.md','r')    #Abre o arquivo Hello.md com o atributo leitura
            bot.sendMessage(chatID,txt.read(),'Markdown',reply_markup=keyboard)
            txt.close()

''' SOBRE: message_loop
o message_loop eh o "listenen" das interacoes dos usuarios com o bot, ele retorna um Json, que quando uma interacao eh feita via mensagem,
recorre a chave 'chat' e redireciona o comportamento do bot para a funcao "ir", e quando uma interacao eh feita via inline_keyboard (callback_query)
recorre a chave callback
'''
bot.message_loop(
    {
        'chat': ir,
        'callback_query': callback,
    }
)

#responsavel por deixa o programa sempre em execucao, mas quando ocorre uma interacao, o message_loop e invocado, e quebra este laco infinito,
#e faz o comportamento requirido pelo usuario
while True:
            pass
