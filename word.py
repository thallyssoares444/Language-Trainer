from random import randint
from time import sleep 
from pathlib import Path
import bd_update
#functio principal 
def train(l1):
    #verifica o idioma escolhido
    if l1 == 1:
        l1 = 'Alemão'
    elif l1 == 2:
        l1 = 'Francês'
    else:
        l1 = 'Japonês'
    
    #verifica se a pessoa ja conhece essa palavra 
    def know_word(a,p):        
            
        alreadKnow = input('Você já conhece essa palavra?[s/n] ')
        
        #valida o input
        while (alreadKnow != 's') and (alreadKnow != 'n'):
            print('Por Favor digite [s/n]')
            alreadKnow = input('Você já conhece essa palavra?[s/n] ')
        #apagar a palavra 
        if alreadKnow == 's':
            deleteWord = input('Deseja apagar essa palavra?[s/n] ')
            if deleteWord == 's':
                with open(f"{a}.txt", "r") as f:
                    lines = f.readlines()
                with open(f"{a}.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != p:
                            f.write(line)
                print('Palavra apagada com sucesso')
            else:
                print('OK.Essa palavra não vai ser apagada')             
    #adiciona a palavra como favorita 
    def favorite(p):
        addFavorite = input('Deseja adicionar essa palavra aos Favoritos?[s/n] ')
        while(addFavorite != 's') and (addFavorite != 'n'):
            print('Por Favor digite [s/n]')
            addFavorite = input('Deseja adicionar essa palavra aos Favoritos?[s/n] ')
        
        if addFavorite == 's':           
            try:               
                print('Insira o nome do seu arquivo de palavras favoritas')
                print('Caso não exista ele sera criado.(adicione ".txt")')
                nome_arquivo = input('Nome do arquivo: ')
                arquivo = open(nome_arquivo, 'r+')
                conteudo = arquivo.readlines()
                conteudo.append(p)
                arquivo = open(nome_arquivo, 'w')
                arquivo.writelines(conteudo)
                arquivo.close()
                print('Palavrada Adicionada')
            except FileNotFoundError:
                arquivo = open(nome_arquivo, 'w+')
                print('Arquivo criado pois nao existia')
                conteudo = arquivo.readlines()
                conteudo.append(p)
                arquivo = open(nome_arquivo, 'w')
                arquivo.writelines(conteudo )
                arquivo.close()
                print('Palavra Adicionada')

        else:
            print('Ok,palavra não adicionada.')
    #pega os arquivos com as palavras 
    def get_text(l2,n):
        count = 0
        #verifica o idoma escolhido
        if l2 == 'Alemão':
            #verifica o que a pessoa vai estudar 
            while count <= n:                              
                text = open('texts/germanVerb.txt','r')                                     
                textShow = text.readlines()[randint(0,100)+1]
                print(textShow)
                know_word(text,textShow)
                favorite(textShow)
                sleep(2)
        elif l2 == 'Francês':
            
            while count <= n:                              
                text = open('texts/frenchVerb.txt','r')                                     
                textShow = text.readlines()[randint(0,100)+1]
                print(textShow)
                know_word(text,textShow)
                favorite(textShow)
                sleep(2)
        else:
        
            while count <= n:                              
                text = open('texts/japanVerb.txt','r')                                     
                textShow = text.readlines()[randint(0,100)+1]
                print(textShow)
                know_word(text,textShow)
                favorite(textShow)
                sleep(2)

    print(f'Você escolheu {l1}')
    sleep(2)
    print('Vamos começar a sessão de treino')
    sleep(2)
    quantPalavra = int(input('Quantas palavras você quer aprender hoje? '))
    get_text(l1,quantPalavra)

print('''[ 1 ]ALEMÃO \n[ 2 ]FRANCÊS \n[ 3 ]JAPONÊS''')
lang = int(input('Qual idioma gostaria de estudar? '))
train(lang)



