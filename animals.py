from models.glass_tank import Lizard, Snake, Worm, Eel, Snail
from models.pond import Otter, Whale, Jellyfish, Dolphin, Penguin
from models.petting_area import Llama, Leopard, Bear, Giraffe, RedPanda

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "llama chow")

print(miss_fuzz.name)

lenny = Leopard("Lenny", "clouded", "morning", "rabbit")

print(lenny.name)

barry = Bear("Barry", "black", "midday", "salmon")

print(barry.name)

gerald = Giraffe("Gerald", "african", "afternoon", "leaves")

print(gerald.name)

randy = RedPanda("Randy", "endangered", "afternoon", "berries")

print(randy.name)

ollie = Otter("Ollie", "north american river", "fish")

print(ollie.name)

wendy = Whale("Wendy", "humpback", "tuna")

jake = Jellyfish("Jake", "upside down", "jellyfish food")

devin = Dolphin("Devin", "spinner", "chocolate")

patrick = Penguin("Patrick", "macaroni", "mackerel")

leroy = Lizard("Leroy", "gecko", "flies")

samuel = Snake("Samuel", "ball python", "rat")

william = Worm("William", "roundworm", "leaves")

ellie = Eel("Ellie", "snowflake", "insects")

stan = Snail("Stan", "mediterranean green", "mushrooms")

print(f'{lenny.name} the {lenny.species} is available to pet during the {lenny.shift} shift.')

print(miss_fuzz)
