import pyttsx3

# Inicialize o motor de síntese de fala
engine = pyttsx3.init()

# Texto que você deseja que seja lido em formato de audiobook
texto = "Este é um exemplo de como criar um audiobook usando a biblioteca pyttsx3."

# Configuração da voz e da velocidade de leitura (opcional)
engine.setProperty("rate", 150)  # Ajuste a velocidade conforme desejado

# Gere o audiobook lendo o texto
engine.say(texto)

# Aguarde até que a leitura seja concluída
engine.runAndWait()

# Encerre o motor de síntese de fala
engine.stop()