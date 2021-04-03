  #                                          Monitoramento da Velocidade da internet :signal_strength:

> Este é um Fork do projeto de Bárbara Guerbas no git: https://github.com/bguerbas/SpeedTest


> Status do Projeto: :heavy_check_mark: (Primeira etapa pronto)

### Tópicos :writing_hand:

- [Descrição do projeto](#descrição-do-projeto-file_folder)

- [Pré-requisitos](#pré-requisitos-pushpin)

- [Como rodar a aplicação](#como-rodar-a-aplicação-arrow_forward)

- [Observações](#observações-eyes)

- [Licença](#licença-grey_exclamation)



## Descrição do projeto :file_folder:

<p align="justify">
Este fork tem como ideal fazer os testes de velocidade através do [SpeedTest CLI](https://www.speedtest.net/pt/apps/cli) , que é uma versão do SpeedTest para desenvolvedor. O SpeedTest CLI é um aplicativo desenvolvido para todas as plataformas: MacOs, Linux, FreeBSD e Windows.
Portanto o SpeedTest CLI tem que ser instalado na sua máquina de teste, ou até mesmo num RaspBerry Pi.

O script em Python desenvolvido por mim consiste em coletar as informações retornadas em formato Json do SpeedTest CLI no SHELL (no meu caso, testado no Linux distribuição Fedora 33 e Python 3.9.2) que armazena num dicionário e vai gravando num arquivo de log na pasta "/log" de acordo com a coleta das informações. Na pasta log tem alguns exemplos dessa coleta. 
</p>

<p align="justify">
O SpeedTest CLI  tem a possibilidade de testar com os servidores próximos a você, através do comando "speedtest -L", No meu caso, ele mostrou 10 servidores próximos a mim na cidade de Feira de Santana.

O script Python ele testa a velocidade de conexão tanto de Download e Upload, mede ping e jitter em cada servidor e no final ele tira a média de todos os valores. No meu caso a média das conexões dos 10 servidores e faz todo o procedimento novamente após 5 minutos, gerando um novo arquivo de log. Esse valor pode ser ajustado no Time Sleep.
</p>



## Pré-requisitos :pushpin:

```
Ter o SpeedTest CLI instalado na máquina de testes,
seguir orientação do site: https://www.speedtest.net/pt/apps/cli
```
```
Ter o Python 3 ou superior instalado.
```

## Como rodar a aplicação :arrow_forward:

No terminal navegar até o diretório onde se encontram os arquivos e digitar:
```
python TesteDeVelocidade.py
```

## Observações :eyes:

A ideia do projeto surgiu através de um post da Bárbara no Linkedin: https://www.linkedin.com/posts/barbaragfigueiredostatistics_faz-um-tempo-que-tenho-notado-a-velocidade-activity-6783124228955766784-fUmv

Num primeiro momento será gerar o resultado em um arquivo de texto log, para avaliações individuais.
Num futuro próximo, tentarei criar um novo script que salve num Banco de Dados MySql.


## Licença :grey_exclamation:

The [MIT License]() (MIT)

Copyright :copyright: 2021 - TestSpeed
