class Keyword:
    """Clase para manejar las palabras clave y sus posiciones."""
    all_keywords = []  # Almacena todas las palabras clave

    def __init__(self, keywords, posicion=None):
        self.keywords = keywords
        self.posicion = posicion

    def save(self):
        """Guarda el estado del objeto (simulado)."""
        # Aquí podría ir una lógica para persistir datos, por ejemplo, en una base de datos.
        print(f"Guardado: {self.keywords} con posición {self.posicion}")

    @classmethod
    def get_all(cls):
        """Devuelve todas las palabras clave almacenadas."""
        return cls.all_keywords

    @classmethod
    def add_keyword(cls, keyword):
        """Añade una nueva palabra clave."""
        cls.all_keywords.append(keyword)




def carga_keywords():
    """Carga nuevas palabras clave."""
    keywords = []
    while True:
        kw = input("Introduce una palabra clave (o deja vacío para finalizar): ").strip()
        if not kw:
            break
        keywords.append(Keyword(kw))
        Keyword.add_keyword(Keyword(kw))
    return keywords


def comprueba_keywords(keyword, dominio):
    """
    Comprueba la posición de una palabra clave en un dominio.
    Esta función es un simulador y devuelve un valor aleatorio.
    """
    import random
    return random.randint(1, 150)  # Simula una posición entre 1 y 150


def muestra_keywords(keywords):
    """Muestra las palabras clave en bloques de 20."""
    contador = 0
    for kw in keywords:
        print(f'KW: {kw.keywords} > {kw.posicion}')
        contador += 1
        if contador == 20:
            contador = 0
            input('Presiona Enter para continuar...')


def keywords_como_lista_de_valores(keywords):
    """Devuelve una lista de tuplas con las palabras clave y sus posiciones."""
    return [(kw.keywords, kw.posicion) for kw in keywords]

#Se ejecutara el programa
def run():
    """Función principal que ejecuta el programa."""
    keywords = Keyword.get_all()
    dominio = 'j2logo.com'

    while True:
        muestra_menu()
        opcion = input('Selecciona una opción > ')
        try:
            opcion = int(opcion)
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if opcion == 0:
            break
        elif opcion == 1:
            keywords = carga_keywords()
        elif opcion == 2:
            muestra_keywords(keywords)
        elif opcion == 3:
            for kw in keywords:
                posicion = comprueba_keywords(kw.keywords, dominio)
                kw.posicion = posicion if posicion < 100 else None
                kw.save()
        else:
            print('Opción no válida')


# Ejecución del programa
if __name__ == "__main__":
    run()
