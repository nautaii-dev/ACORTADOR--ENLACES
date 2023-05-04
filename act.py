import pyshorteners

# 🌐 Crea una instancia del acortador de enlaces

s = pyshorteners.Shortener()

# 🖥️ Pide al usuario que introduzca la URL

url = input("Introduce la URL que quieres acortar: ")

# 🔄 Imprime un mensaje de procesamiento

print("Procesando la URL...")

# 🔗 Acorta la URL

short_url = s.tinyurl.short(url)

# 🎉 Imprime la URL acortada

print(f"¡Tu URL acortada es: {short_url}!")

#SEXO😈
