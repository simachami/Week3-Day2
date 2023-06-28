from requests import get
from IPython.display import Image
from IPython.display import display
class Pokemon:
    
    def __init__(self, name):
        self.name = name
        self.abilities = []
        self.weight = None
        self.types = []
        self.image = ''
        self.pokemon_api_call()
        
    def pokemon_api_call(self):
        response_object = get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
        if response_object.ok:
            poke_info = response_object.json()
            self.name = poke_info['name']
            self.abilities = poke_info['abilities']
            self.weight = poke_info['weight']
            self.types = poke_info['types']
            self.image = poke_info['sprites']['versions']['generation-v']['black-white']['animated']['front_shiny']
            if not self.image:
                self.image = poke_info['sprites']['front_default']
        else:
            print(f'Error: status code {response_object.status_code}')
            
    def __repr__(self):
        return f'<Pokemon: {self.name}>'
    
    def display_pokemon_info(self):
        print(f'{self.name} Weight: {self.weight}')
        print('Types:', end=' ')
        for poke_type in self.types:
            print(poke_type['type']['name'], end= ' ')
        print('\nAbilities:', end=' ')
        for ability in self.abilities:
            print(ability['ability']['name'],end=' ')
        self.display_image()
        
    def display_image(self, width=150):
        display(Image(self.image,width=width))
            
psyduck = Pokemon('pikachu')


psyduck.display_pokemon_info()