import random

class Pokemon:
    def __init__(self, nombre, tipo, nivel, vida, experiencia, evolucion=None):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        self.vida = vida
        self.experiencia = experiencia
        self.evolucion = evolucion

    def atacar(self, otro_pokemon):
        dano = random.randint(10, 20)
        otro_pokemon.defender(dano)
        self.ganar_experiencia(10)

    def defender(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0

    def ganar_experiencia(self, puntos):
        self.experiencia += puntos
        if self.experiencia >= 100:
            self.nivel += 1
            self.experiencia = 0
            print(f"{self.nombre} ha subido al nivel {self.nivel}!")
            self.evolucionar()

    def evolucionar(self):
        if self.evolucion and self.nivel >= 16:  # Ejemplo de nivel de evolución
            print(f"{self.nombre} está evolucionando a {self.evolucion}!")
            self.nombre = self.evolucion
            self.evolucion = None  # Solo una evolución por simplicidad

    def esta_vivo(self):
        return self.vida > 0

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pokemons = []
        self.pociones = 5

    def capturar_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def usar_pocion(self, pokemon):
        if self.pociones > 0:
            pokemon.vida += 20
            self.pociones -= 1
        else:
            print("No tienes pociones disponibles.")

def mostrar_estado_combate(jugador, oponente):
    print(f"Jugador: {jugador.nombre}")
    for pokemon in jugador.pokemons:
        print(f"{pokemon.nombre} - Vida: {pokemon.vida}")

    print(f"Oponente: {oponente.nombre}")
    for pokemon in oponente.pokemons:
        print(f"{pokemon.nombre} - Vida: {pokemon.vida}")

def mostrar_inventario(jugador):
    print("Inventario de Pokémon:")
    for pokemon in jugador.pokemons:
        print(f"{pokemon.nombre} - Nivel: {pokemon.nivel} - Vida: {pokemon.vida}")
    print(f"Pociones: {jugador.pociones}")

def revisar_combates():
    # Implementar la lógica para revisar combates anteriores
    pass