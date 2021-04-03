from datetime import datetime, timezone, timedelta
import statistics, subprocess, time, json, os 


# Variável que irá armazenar todos os testes numa lista para o cálculo da média
Testes_Ping = []
Testes_Jitter = []
Testes_Download = []
Testes_Upload = []


# Irá buscar os servidores mais próximos usando o aplicativo do speedtest local
servers =  json.loads(subprocess.Popen('speedtest -L -f json', shell=True, stdout=subprocess.PIPE).stdout.read())    
server_list = servers['servers']    


# Obtendo o horário atual para salvar no nome do arquivo log
now = datetime.now().strftime("%Y-%m-%d-%H_%M_%S")


# Cria a pasta 'log' se não existir
if not os.path.isdir('log/'):
    os.mkdir('log/')


# Função que escreve no arquivo na pasta 'log', cada teste possui o seu arquivo com data
def escreve_log(texto=None):
    with open("log/"+str(now)+'.txt','a') as arquivo:
        arquivo.write(texto+'\n')


# Loop de Repetição com pausa de 5min. entre os testes
while True:
    # Imprimindo lista de servidores próximos
    print(f'Os {len(server_list)} servidores próximos a você:')
    escreve_log(f'Os {len(server_list)} servidores próximos a você:')

    for i in server_list:
        print(f"Server: {server_list.index(i)+1}, Id: {i['id']}, Provedor: {i['name']}, Cidade: {i['location']}")
        escreve_log(f"Server: {server_list.index(i)+1}, Id: {i['id']}, Provedor: {i['name']}, Cidade: {i['location']}")


    # Testando todos os servidores da lista
    for i in server_list:
        print(f"\n>>>>>> Testando Conexão com o Server: {server_list.index(i)+1}, Id: {i['id']}, Provedor: {i['name']}, Cidade: {i['location']} <<<<<<")
        escreve_log(f"\n>>>>>> Testando Conexão com o Server: {server_list.index(i)+1}, Id: {i['id']}, Provedor: {i['name']}, Cidade: {i['location']} <<<<<<")
        
        TesteId = json.loads(subprocess.Popen(f"speedtest -s {i['id']} -f json", shell=True, stdout=subprocess.PIPE).stdout.read())
            
        # Nome do seu provedor de Internet
        print(f"Seu Provedor de Internet: {TesteId['isp']}")
        escreve_log(f"Seu Provedor de Internet: {TesteId['isp']}")

        # Obtendo a data e horário do teste e convertendo o fusohorário
        tempo = datetime.strptime(servers['timestamp'], '%Y-%m-%dT%H:%M:%SZ').astimezone(timezone(timedelta(hours=-6)))
        print(f"Horário: {tempo.strftime('%d/%m/%Y %H:%M')}")
        escreve_log(f"Horário: {tempo.strftime('%d/%m/%Y %H:%M')}")
        
        # Obtendo o ping do teste
        print(f"Ping: {TesteId['ping']['latency']} ms")
        Testes_Ping.append(TesteId['ping']['latency'])
        escreve_log(f"Ping: {TesteId['ping']['latency']} ms")
        
        # Obtendo o Jitter do teste
        print(f"Jitter: {TesteId['ping']['jitter']} ms")
        Testes_Jitter.append(TesteId['ping']['jitter'])
        escreve_log(f"Jitter: {TesteId['ping']['jitter']} ms")
        
        # Obtendo a velocidade de Download e convertendo para Megabit
        print(f"Download: {round(TesteId['download']['bandwidth']*8/1000/1000,2)} Mb/s")
        Testes_Download.append(TesteId['download']['bandwidth'])
        escreve_log(f"Download: {round(TesteId['download']['bandwidth']*8/1000/1000,2)} Mb/s")

        # Obtendo a velocidade de Upload e convertendo para Megabit
        print(f"Upload: {round(TesteId['upload']['bandwidth']*8/1000/1000,2)} Mb/s")
        Testes_Upload.append(TesteId['upload']['bandwidth'])
        escreve_log(f"Upload: {round(TesteId['upload']['bandwidth']*8/1000/1000,2)} Mb/s")

        # O resultado do teste fica salvo nos servidores da SpeedTest
        print(f"Resultado no SpeedTest: {TesteId['result']['url']}")
        escreve_log(f"Resultado no SpeedTest: {TesteId['result']['url']}")

    # Calculando a média de todos os testes!
    print("\n>>> Calculando a média da conexão! <<<")
    escreve_log("\n>>> Calculando a média da conexão! <<<")

    print(f"A média de Ping foi: {round(sum(Testes_Ping)/len(Testes_Ping),2)} ms")
    escreve_log(f"A média de Ping foi: {round(sum(Testes_Ping)/len(Testes_Ping),2)} ms")

    print(f"A média de Jitter foi: {round(sum(Testes_Jitter)/len(Testes_Jitter),2)} ms")
    escreve_log(f"A média de Jitter foi: {round(sum(Testes_Jitter)/len(Testes_Jitter),2)} ms")

    print(f"A média de Download foi: {round(sum(Testes_Download)/len(Testes_Download)*8/1000/1000,2)} Mb/s")
    escreve_log(f"A média de Download foi: {round(sum(Testes_Download)/len(Testes_Download)*8/1000/1000,2)} Mb/s")

    print(f"A média de Upload foi: {round(sum(Testes_Upload)/len(Testes_Upload)*8/1000/1000,2)} Mb/s")
    escreve_log(f"A média de Upload foi: {round(sum(Testes_Upload)/len(Testes_Upload)*8/1000/1000,2)} Mb/s")

    # Delay de 5 min. para o próximo teste
    print('\nAguardando 5 min. para o próximo teste!\n')
    time.sleep(300)
    # Atualizando o horário atual para escrever em um novo arquivo
    now = datetime.now().strftime("%Y-%m-%d-%H_%M_%S")