import sqlite3
import random
import time
import sys
import os
from colorama import init, Fore
from colorama import init, Fore, Back

init(convert=True, autoreset=True)
print("Aguarde...")
time.sleep(3)

while True:
    menu = ['Cadastrar', 'Login', 'Sair']
    cont = 0
    for x in menu:
        cont += 1
        print(f'[{cont}]{x}')
    resposta = int(input('O que deseja fazer: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    if resposta == 1:
        print('')
        nome = str(input('Nome: '))
        senha = str(input('Senha: '))
        banco = ''
        try:
            banco = sqlite3.connect('gerenciador_senhas.db')
            print(Fore.GREEN + 'Banco de dados acessado com sucesso!')
        except Exception as erro:
            print(Fore.RED + "Não foi possível acessar o banco de dados!")
            time.sleep(2)

        while True:
            try:
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE user (nome text, senha text)")
                cursor.execute("CREATE TABLE contas (site text, usuario text, senha text)")
                banco.commit()
                banco.close()

            except Exception as erro:
                banco.close()

            banco = sqlite3.connect("gerenciador_senhas.db")
            cursor = banco.cursor()
            cursor.execute("SELECT nome FROM user WHERE nome = '" + nome + "' ")
            banco.commit()
            validar = cursor.fetchall()
            lista = list(validar)
            if len(lista) != 0:
                print(Fore.YELLOW + "Nome já utilizado!")
                break

            banco.close()
            try:
                banco = sqlite3.connect("gerenciador_senhas.db")
                cursor = banco.cursor()
                cursor.execute("INSERT INTO user VALUES('" + nome + "', '" + senha + "')")
                banco.commit()
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.GREEN + "Sucesso ao enviar seus dados!")
                time.sleep(1)
                banco.close()
                break

            except Exception as erro:
                print(Fore.RED + "Falha ao enviar seus dados")
                time.sleep(2)
                break


    elif resposta == 2:
        try:
            banco = sqlite3.connect("gerenciador_senhas.db")
            cursor = banco.cursor()
            cursor2 = banco.cursor()
            os.system('cls' if os.name == 'nt' else 'clear')
            login = str(input("Nome: "))
            senha = str(input("Senha: "))
            cursor.execute("SELECT nome FROM user WHERE nome = '" + login + "'")
            cursor2.execute("SELECT senha FROM user WHERE nome = '" + login + "' ")
            banco.commit()
            login_valid = cursor.fetchall()
            senha_valid = cursor2.fetchall()
            for x in login_valid:
                c = x
            for b in c:
                d = b

            for x in senha_valid:
                e = x
            for f in e:
                g = f

        except Exception as erro:
            print(Fore.RED + "Erro ao logar!")

        os.system('cls' if os.name == 'nt' else 'clear')

        try:
            if login == d and senha == g:
                print(Fore.GREEN + "Login realizado com sucesso!")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                banco.close()
        except Exception as erro:
            time.sleep(2)
            print(Fore.RED + "Credenciais inválidas!")

        else:
             if login == d and senha == g:
                 print(Fore.GREEN + "Login realizado com sucesso!")
                 time.sleep(1)
                 os.system('cls' if os.name == 'nt' else 'clear')
                 time.sleep(1)
                 banco.close()
        

       

        while True:
                print(f"Bem-vindo(a) {login}")
                menu = ['Cadastrar credencial', 'Ver credenciais', 'Alterar credenciais', 'Alterar dados', 'Excluir conta', 'Sair']
                cont = 0
                for x in menu:
                    cont += 1
                    print(f'[{cont}]{x}')
                responda = int(input("Ação -> "))
                try:
                    banco = sqlite3.connect("gerenciador_senhas.db")
                    cursor = banco.cursor()

                except Exception as erro:

                    print(Fore.RED + "Erro ao se conectar!")
                    time.sleep(2)

                if responda == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    site = str(input("Nome do site: "))
                    usuario = str(input("Usuário: "))
                    escolha = str(input("Senha automática? ").upper())
                    if escolha == "SIM":

                        lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u' 'v', 'w', 'x', 'y', 'z']
                        especiais = ['!', '@', '#', '$', '%', '&', '*'] 
                        senha2 = []
                        qtd = int(input("Quantidade caracteres que sua senha terá: "))
                        for _ in range(1, qtd):
                            a = random.choice(lista)
                            b = random.choice(especiais)                            
                            senha2.append(a)
                            senha2.append(b)
                            senha = "".join(str(v) for v in senha2)
                        print(senha)
                        cursor.execute("INSERT INTO contas VALUES('" + site + "', '" + usuario + "', '" + senha + "')")
                        banco.commit()
                        print(Fore.GREEN + "Credencial cadastrada!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        banco.close()
                        continue


                    else:
                        senha = str(input("Senha Manual: "))
                        cursor.execute("INSERT INTO contas VALUES('" + site + "', '" + usuario + "', '" + senha + "')")
                        banco.commit()
                        print(Fore.GREEN + "Credencial cadastrada!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        banco.close()
                        continue

                elif responda == 3:
                    try:
                        alt = str(input('Qual credencial deseja aletrar? '))
                        cursor.execute("SELECT site FROM contas WHERE site = '"+alt+"'")
                        banco.commit()
                        retorno = cursor.fetchall()
                        for letra in retorno:
                            c = letra

                        for letra2 in c:
                            d = letra2

                        nomeuser = str(input("Novo usuário: "))
                        senhasite = str(input("Nova senha: "))
                        cursor.execute("UPDATE contas SET senha =  '" + senhasite + "' WHERE site = '" + d + "'")
                        cursor.execute("UPDATE contas SET usuario =  '" + nomeuser + "' WHERE site = '" + d + "'")
                        banco.commit()
                        banco.close()
                        print(Fore.GREEN + "DADOS ALTERADOS!")

                    except Exception as erro:
                        print(Fore.RED + "ERRO AO ALTERAR DADOS!")
                        print(erro)

                elif responda == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    a = cursor.execute("SELECT * FROM contas")
                    banco.commit()
                    a = cursor.fetchall()
                    for x in a:
                        print(x)          
                    time.sleep(2)
                    banco.close()
                    print('')
                    continue
                    

                elif responda == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    try:
                        cursor.execute("DROP TABLE contas")
                        cursor.execute("DROP TABLE user")
                        banco.commit()
                        banco.close()
                        os.remove('gerenciador_senhas.db')
                        print(Fore.GREEN + "Dados excluídos com sucesso!")
                        time.sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        """banco.close()"""
                        sys.exit()

                    except Exception as erro:
                        time.sleep(2)
                        print(erro)


                elif responda == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cursor.execute("DELETE FROM user")
                    cursor.execute("DELETE FROM contas")
                    banco.commit()
                    print(Fore.GREEN + "Dados excluídos com sucesso!")
                    time.sleep(1)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    banco.close()
                    sys.exit()

                

                elif responda == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    try:
                        nome = str(input("Novo nome: "))

                        cursor.execute("SELECT nome FROM user WHERE nome = '"+nome+"'")

                        cursor.execute("SELECT nome FROM user WHERE nome = '"+ nome +"' ")

                        validar = cursor.fetchall()
                        if len(validar) != 0:
                            while True:
                                print(Fore.YELLOW + "Nome já utilizado!") 
                                nome = str(input("Nome: "))
                                cursor.execute("SELECT nome FROM user WHERE nome = '"+nome+"'")
                                validar = cursor.fetchall()
                                if len(validar) == 0:
                                    break
                                else:
                                    continue 
                        else:
                            senha = str(input("Nova senha: "))  
                            cursor.execute("UPDATE user SET senha = '" + senha + "' WHERE nome = '" + login + "'")
                            banco.commit()

                            cursor.execute("UPDATE user SET nome = '"+nome+"' WHERE senha = '"+senha+"'")

                            cursor.execute("UPDATE user SET nome = '"+ nome +"' WHERE senha = '"+senha+"'")
                            banco.commit()
                            banco.close()
                            print(Fore.GREEN + "DADOS ALTERADOS COM SUCESSO!")
                            time.sleep(1)
                            sys.exit()

                    except Exception as erro:

                        print(Fore.RED + "Erro ao cadastrar novas informações!") 
                        continue
                    else:
                        senha = str(input("Nova senha: "))  
                        cursor.execute("UPDATE user SET senha = '" + senha + "' WHERE nome = '" + login + "'")
                        banco.commit()

                        cursor.execute("UPDATE user SET nome = '"+nome+"' WHERE senha = '"+senha+"'")

                        cursor.execute("UPDATE user SET nome = '"+ nome +"' WHERE senha = '"+senha+"'")
                        banco.commit()
                        banco.close()
                        print(Fore.GREEN + "DADOS ALTERADOS COM SUCESSO!")
                        time.sleep(1)
                        sys.exit()


                else:
                    time.sleep(2)
                    sys.exit()
                    
        
        else:
            print(Fore.RED + "Credenciais inválidas!")
            time.sleep(1)
    else:
        sys.exit()
