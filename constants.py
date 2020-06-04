import enum


def ev(weight):
    weight_reference = .0099 # Lightest Item
    max_weight = 300 # How much can your character hold at once
    highest_x_value = max_weight/weight_reference # Maximum amount of the lightest item you can carry
    slope = -(10/highest_x_value) # Slope of the linear
    y = lambda x: -.0003*x+10 # Linear starts at y=10 
    return y(weight)


class DLC(enum.Enum):
    base_game = ""
    aberration = "(Aberration)"
    extinction = "(Extinction)"
    genesis = "(Genesis: Part 1)"
    mobile = "(Mobile)"
    prim_plus = "(Primitive Plus)"
    ragnarok = "(Ragnarok)"
    scorched_earth = "(Scorched Earth)"

# TODO: Make this more easily customizable, furthermore dont jump from dict to enum to dict
# this is where you change the numbers to determine whats easy for ***you*** to get
mats = {'Oil': 30, 'Thatch': 5, 'Gunpowder': 60, 'Sparkpowder': 15, 'Charcoal': 30, 'Flint': 5,
    'Cementing Paste': 60, 'Iron Ingot': 60, 'Metal Ingot': 60, "Metal Ingot or Scrap Metal Ingot":60, 'Element': 1000, 'Wood': 5,
    'Wood or Fungal Wood': 5, 'Fiber': 5, 'Metal': 10, 'Stone': 5, 'Crystal': 15}
    
class BIE(enum.Enum): # Base Item Efforts
    """
    Considers weight on a linear scale based on the lightest item (slightly lighter to prevent zero values)
    TODO: make the weight retrieved from file
    """
    Oil = ev(.2*mats["Oil"])
    Thatch = ev(.02*mats["Thatch"])
    SparkPowder = ev(.1*mats["Sparkpowder"])
    Charcoal = ev(.25*mats["Charcoal"])
    Flint = ev(.05*mats["Flint"])
    Cementing_Paste = ev(.01*mats["Cementing Paste"])
    Iron_Ingot = ev(1*mats["Iron Ingot"])
    Element = ev(.01*mats["Element"])
    Wood = ev(.5*mats["Wood"])
    Fiber = ev(.01*mats["Fiber"])
    Metal = ev(1*mats["Metal"])
    Stone = ev(.5*mats["Stone"])
    Gunpowder = ev(.1*mats["Gunpowder"])
    Crystal = ev(1*mats["Crystal"])
    
calcluations = {'Oil': BIE.Oil.value, 'Thatch': BIE.Thatch.value, 'Gunpowder': BIE.Gunpowder.value,
                'Sparkpowder': BIE.SparkPowder.value, 'Charcoal': BIE.Charcoal.value, 'Flint': BIE.Flint.value,
                'Cementing Paste': BIE.Cementing_Paste.value, 'Iron Ingot': BIE.Iron_Ingot.value,
                'Metal Ingot': BIE.Iron_Ingot.value, "Metal Ingot or Scrap Metal Ingot":BIE.Iron_Ingot.value,
                'Element': BIE.Element.value, 'Wood': BIE.Wood.value, 'Wood or Fungal Wood': BIE.Wood.value,
                'Fiber': BIE.Fiber.value, 'Metal': BIE.Metal.value, 'Stone': BIE.Stone.value, 'Crystal': BIE.Crystal.value}

#most organic materials are gone, this is just because they're not really reliable enough, but I can possibly add later...


# "Fake" errors used in specific places 
class BaseItemNotFound(Exception):
    pass

class NoExperience(Exception):
    pass
