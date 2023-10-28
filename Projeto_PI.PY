import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

# Configuração dos pinos GPIO
GPIO.setmode(GPIO.BCM)

# Pino do botão com pull-down
Fim = 21
Inicio = 20
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

# Configura o pino do botão como entrada com pull-down interno
GPIO.setup(Fim, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Inicio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(5, 1)
GPIO.output(6, 1)
GPIO.output(13, 0)
GPIO.output(19, 0)


# Função de tratamento de interrupção
def Volta(channel):
    if GPIO.input(Fim) == GPIO.HIGH:
        GPIO.output(19, 1)
        GPIO.output(13, 1)
        time.sleep(1)
        GPIO.output(5, 0)
        GPIO.output(6, 0)
        
def Deliga(channel):
    if GPIO.input(Inicio) == GPIO.HIGH:
        GPIO.output(13, 1)
        GPIO.output(19, 1)
        GPIO.output(5, 1)
        GPIO.output(6, 1)

# Configura a interrupção no pino para detectar borda de subida
GPIO.add_event_detect(Fim, GPIO.FALLING, callback=Volta, bouncetime=500)
GPIO.add_event_detect(Inicio, GPIO.FALLING, callback=Deliga, bouncetime=500)

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

