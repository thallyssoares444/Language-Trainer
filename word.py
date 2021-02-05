from random import randint
from time import sleep 
from pathlib import Path




#functio principal 

def train():
    print('''[ 1 ]Revisar palavras salvas \n[ 2 ]Aprender novas Palavras''')
    c = int(input('Qual você quer? '))
    def delete(a,p): 
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
    #verifica se a pessoa ja conhece essa palavra 
    def know_word(a,p):           
        
        alreadKnow = input('Você já conhece essa palavra?[s/n] ')  
        #valida o input
        while (alreadKnow != 's') and (alreadKnow != 'n'):
            print('Por Favor digite [s/n]')
            alreadKnow = input('Você já conhece essa palavra?[s/n] ')
        #apagar a palavra 
        if alreadKnow == 's':
            delete(a,p)            
    #adiciona a palavra como favorita 
    def favorite(p):
        addFavorite = input('Deseja adicionar essa palavra aos Favoritos?[s/n] ')
        while(addFavorite != 's') and (addFavorite != 'n'):
            print('Por Favor digite [s/n]')
            addFavorite = input('Deseja adicionar essa palavra aos Favoritos?[s/n] ')
        
        if addFavorite == 's':           
            nome_arquivo = input('Qual vai ser o nome do arquivo?(lembre de colocar ".txt" no final)')
            arquivo = open(nome_arquivo, 'w+')
            print('Arquivo criado')
            conteudo = arquivo.readlines()
            conteudo.append(p)
            arquivo = open(nome_arquivo, 'w')
            arquivo.writelines(conteudo )
            arquivo.close()
            sleep(5)
            print('Palavra Adicionada')

        else:
            print('Ok,palavra não adicionada.')
    #pega os arquivos com as palavras 
    def get_text(m):
        if m == 1:
            m = 'revisar palavras salvas'
        else:
            m = 'aprender novas palavras'
        print(f'Você escolheu {m}.')
        sleep(2)
        print('Vamos começar a sessão de treino.')
        sleep(2)

        count = 0
        if m == 'aprender novas palavras':
            print('''[ 1 ]ALEMÃO \n[ 2 ]FRANCÊS \n[ 3 ]JAPONÊS''')
            l2 = int(input('Qual idioma gostaria de aprender palavras novas? '))
            #verifica o idioma escolhido
            if l2 == 1:
                l2 = 'Alemão'
            elif l2 == 2:
                l2 = 'Francês'
            else:
                l2 = 'Japonês'

            if l2 == 'Japonês':
                print('''[ 1 ]HIRAGANA \n[ 2 ]KATAKANA \n[ 3 ]KANJI \n[ 4 ]NOVAS PALAVRAS ''')
                japanChoose = int(input('Qual você quer? '))
            m = 'aprender novas palavras'
            #verifica o idoma escolhido
            quantPalavra = int(input('Quantas palavras gostaria de aprender hoje? '))
            if l2 == 'Alemão':
                #verifica o que a pessoa vai estudar 
                while count <= quantPalavra:                              
                    text = open('texts/germanWord.txt','r')
                    with open('texts/germanWord.txt') as f:
                        total = sum(1 for t in f)                                                                          
                        textShow = text.readlines()[randint(0,total)+1]
                    print(textShow)
                    know_word(text,textShow)
                    favorite(textShow)
                    sleep(2)
            elif l2 == 'Francês':
                
                while count <= quantPalavra:                              
                    text = open('texts/frenchWord.txt','r')
                    with open('texts/frenchWord.txt') as f:
                        total = sum(1 for t in f)                                     
                        textShow = text.readlines()[randint(0,total)+1]
                    print(textShow)
                    know_word(text,textShow)
                    favorite(textShow)
                    sleep(2)
            else:
                if japanChoose == 1:
                    japanChoose == 'hiragana'
                elif japanChoose == 2:
                    japanChoose == 'katakana'
                elif japanChoose == 3:
                    japanChoose == 'kanji'
                else:
                    japanChoose == 'novas palavras'

                print(f'Vamos começar os estudos de {japanChoose}')
                sleep(2)

                if japanChoose == 'hiragana':
                    while count <= quantPalavra:                              
                        text = open('texts/japanHiragana.txt','r')
                        with open('texts/japanHiragana.txt') as f:
                            total = sum(1 for t in f)                                     
                            textShow = text.readlines()[randint(0,total)+1]
                        print(textShow)
                        know_word(text,textShow)
                        favorite(textShow)
                        sleep(2)
                elif japanChoose == 'katakana':
                    while count <= quantPalavra:                              
                        text = open('texts/japanKatakana.txt','r')
                        with open('texts/japanKatakana.txt') as f:
                            total = sum(1 for t in f)                                     
                            textShow = text.readlines()[randint(0,total)+1]
                        print(textShow)
                        know_word(text,textShow)
                        favorite(textShow)
                        sleep(2)
                elif japanChoose == 'kanji':
                    while count <= quantPalavra:                              
                        text = open('texts/japanKanji.txt','r')
                        with open('texts/japanKanji.txt') as f:
                            total = sum(1 for t in f)                                     
                            textShow = text.readlines()[randint(0,total)+1]
                        print(textShow)
                        know_word(text,textShow)
                        favorite(textShow)
                        sleep(2)
                else:
                    while count <= quantPalavra:                              
                        text = open('texts/japanWord.txt','r')
                        with open('texts/japanWord.txt') as f:
                            total = sum(1 for t in f)                                     
                            textShow = text.readlines()[randint(0,total)+1]
                        print(textShow)
                        know_word(text,textShow)
                        favorite(textShow)
                        sleep(2)
        else:
            m = 'revisar palavras salvas'
            print('Insira o nome do seu arquivo de palavras favoritas (Com o ".txt" no final)')
            nome_arquivo = input('Nome do arquivo: ')
            try: 
                arquivo = open(nome_arquivo, 'r+')
                count = 0 
                quantPalavra = int(input('Quantas palavras gostaria de aprender hoje? '))
                while count < quantPalavra:
                    with open(f'{nome_arquivo}.txt') as f:
                        total = sum(1 for t in f)
                        conteudo = arquivo.readlines()[randint(0,total)+1] 
                    print(conteudo)             
                    delete(arquivo,conteudo)

            except FileNotFoundError:
                print('Arquivo não encontradado.Por favor digite um nome valido')
                nome_arquivo = input('Nome do arquivo: ')

                arquivo = open(nome_arquivo, 'r+')
                count = 0 
                quantPalavra = int(input('Quantas palavras gostaria de aprender hoje? '))
                while count < quantPalavra:
                    with open('data.txt') as f:
                        total = sum(1 for t in f)
                        conteudo = arquivo.readlines()[randint(0,total)+1] 
                    print(conteudo)
                    delete(arquivo,conteudo)

    get_text(c)

print('Bem Vindo,esse programa ira lhe ajudar no aprendizado de Idiomas.')
sleep(3)
print('O intuito desse programa é lhe ajudar a revisar ou aprender novas palavras de acordo com o idioma que você estiver aprendendo.')
sleep(6)
print('Vamos começar!')
sleep(2)
train()
