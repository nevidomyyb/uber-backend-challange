#Gerencia de log
import datetime

def checkArchiveExistence(arquivo):
    try: 
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createArchive(arquivo):
    try:
        a = open(arquivo, 'wt+')
    except:
        print("Falha ao criar arquivo")
    else:
        a.close()

def registerLog(arquivo, origem_log, mensagem):
    try:
        a = open(arquivo, 'at')
    except:
        print("Falha ao registrar log")
    else:
        hora_atual = datetime.datetime.now()
        a.write(f"{hora_atual}: [{origem_log}]: {mensagem}\n")
        a.close()