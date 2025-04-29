import pickle
import combate_pokemon

# Cargar los datos de los Pokémon
with open('pokemons.pkl', 'rb') as f:
    pokemons_data = pickle.load(f)

# Crear instancias de Pokémon a partir de los datos cargados
pokemons = [combate_pokemon.Pokemon(**data) for data in pokemons_data]

# Crear jugadores y asignar Pokémon
jugador = combate_pokemon.Jugador("Ash")
oponente = combate_pokemon.Jugador("Gary")

jugador.capturar_pokemon(pokemons[0])  # Bulbasaur
oponente.capturar_pokemon(pokemons[1])  # Charmander

# Mostrar estado inicial del combate
combate_pokemon.mostrar_estado_combate(jugador, oponente)

# Realizar un ataque
jugador.pokemons[0].atacar(oponente.pokemons[0])

# Mostrar estado después del ataque
combate_pokemon.mostrar_estado_combate(jugador, oponente)