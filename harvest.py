############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = [] #list of MelonType objects = [MelonType, MelonType....]

    melon_list = [
        ["Muskmelon","musk", 1998, "green", True, True, ["mint"]],
        ["Casaba","cas", 2003, "orange", False, False, ["strawberries", "mint"]],
        ["Crenshaw" ,"cren", 1996, "green", False, False, ["proscuitto"]],
        ["Yellow Watermelon","yw", 2013, "yellow", False, True, ["ice cream"]]
    ]

    for melon in  melon_list:
        # melon_info = melon_list[melon] #[code, year, color, seedless, bestseller, pairing]
        melon_object = MelonType(melon[1],melon[2],melon[3],melon[4],melon[5],melon[0])

        pairings = melon[6] #list of the pairings for that melon
        for pairing in pairings:
            melon_object.add_pairing(pairing)

        all_melon_types.append(melon_object)


    return all_melon_types #list of MelonType objects = [MuskMelon, Casaba, Crenshaw....]


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # melon_types is a list of melon type objects
    for melon in melon_types:
        #melon is a MelonType object
        melon_pairings = melon.pairings
        melon_name = melon.name
        print("{} pairs with".format(melon_name))
        for pairing in melon_pairings:
            print("- {}".format(pairing))


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #melon_types = [MelonType1, MelonType2, ....]

    melon_dictionary = {} #{melon_code1: MelonType1, melon_code2: MelonType2....}

    for melon in melon_types:
        melon_code = melon.code
        melon_dictionary[melon_code] = melon


    return melon_dictionary



    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



