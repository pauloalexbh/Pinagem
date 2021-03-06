#Esse modulo apresenta a pinagem a ser utilizada em meus projetos com o Raspberry Pi Zero W.
'''
Alias------BCM----Pinoxx**Pinoxx-----BCM-----Alias

3v3-xxxxxx-3V3----Pino01**Pino02-----5Vxxxxxxxx-5V
-----------GPIO02-Pino03**Pino04-----5Vxxxxxxxx-5V
-----------GPIO03-Pino05**Pino06----GNDxxxxxxx-GND
-----------GPIO04-Pino07**Pino08-GPIO14-----------
GND-xxxxxxxxx-GND-Pino09**Pino10-GPIO15-<-Campainha
IRIn->>>>>-GPIO17-Pino11**Pino12-GPIO18->>>-Portao
IROut-<<<<-GPIO27-Pino13**Pino14-GNDxxxxxxxxxx-GND
-----------GPIO22-Pino15**Pino16-GPIO23-<<<<-Porta
3v3-xxxxxxxxx-3V3-Pino17**Pino18-GPIO24-<<<-Tranca
-----------GPIO10-Pino19**Pino20----GND-xxxxxx-GND
-----------GPIO09-Pino21**Pino22-GPIO25-----------
-----------GPIO11-Pino23**Pino24-GPIO08-----------
GND-xxxxxxxxx-GND-Pino25**Pino26-GPIO7------------
I2C-xxxxxxxxx-I2C-Pino27**Pino28-I2C-xxxxxxxxx-I2C
-----------GPIO5-Pino29**Pino30-GND-xxxxxxxxxx-GND
-----------GPIO06-Pino31**Pino32-GPIO12-----------
-----------GPIO13-Pino33**Pino34-GND-xxxxxxxxx-GND
-----------GPIO19-Pino35**Pino36-GPIO16-----------
-----------GPIO26-Pino37**Pino38-GPIO20-----------
GND-xxxxxxxxx-GND-Pino39**Pino40-GPIO21-----------
'''

define setmode = board

define IRIn = 11 #lirc.py
define IROut = 13 #lirc.py

define Porta = 16 #interrupcao_porta.py
define Tranca = 18 #interrupcao_porta.py

define Campainh = 10 #interfoneRasp.py
define Portao = 12 #interfoneRasp.py
