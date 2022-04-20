from models.glass_tank import Lizard, Snake, Worm, Eel, Snail
from models.pond import Otter, Whale, Jellyfish, Dolphin, Penguin
from models.petting_area import Llama, Leopard, Bear, Giraffe, RedPanda
from models.attractions import Wetlands, PettingZoo, SnakePit

miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "morning", "llama chow")

print(miss_fuzz.name)

lenny = Leopard("Lenny", "Clouded Leopard", "morning", "rabbit")

print(lenny.name)

barry = Bear("Barry", "Black Bear", "midday", "salmon")

print(barry.name)

gerald = Giraffe("Gerald", "African Giraffe", "afternoon", "leaves")

print(gerald.name)

randy = RedPanda("Randy", "Endangered Red Panda", "afternoon", "berries")

print(randy.name)

ollie = Otter("Ollie", "North American River Otter", "fish")

wendy = Whale("Wendy", "Humpback Whale", "tuna")

jake = Jellyfish("Jake", "Upside Down Jellyfish", "jellyfish food")

devin = Dolphin("Devin", "Spinner Dolphin", "chocolate")

patrick = Penguin("Patrick", "Macaroni Penguin", "mackerel")

leroy = Lizard("Leroy", "Gecko Lizard", "flies")

samuel = Snake("Samuel", "Ball Python", "rat")

william = Worm("William", "Roundworm", "leaves")

ellie = Eel("Ellie", "Snowflake Eel", "insects")

stan = Snail("Stan", "Mediterranean Green Snail", "mushrooms")

print(f'{lenny.name} the {lenny.species} is available to pet during the {lenny.shift} shift.')

print(miss_fuzz)

slither_inn = SnakePit("Slither Inn", "slithery and slimy critters")
critter_cove = Wetlands("Critter Cove", "slippery and wet critters")
varmint_village = PettingZoo(
    "Varmint Village", "cute and fuzzy critters to cuddle")

critter_cove.add_animal(ollie)
critter_cove.add_animal(wendy)
critter_cove.add_animal(jake)
critter_cove.add_animal(devin)
critter_cove.add_animal(patrick)

print(critter_cove)

varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(lenny)
varmint_village.add_animal(barry)
varmint_village.add_animal(gerald)
varmint_village.add_animal(randy)

print(varmint_village)

slither_inn.add_animal(leroy)
slither_inn.add_animal(samuel)
slither_inn.add_animal(william)
slither_inn.add_animal(ellie)
slither_inn.add_animal(stan)

print(slither_inn)
