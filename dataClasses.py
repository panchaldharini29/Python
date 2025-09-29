"""Data Class: A dataclass is a special kind of class in Python that is mainly used to store data."""

# -------------------------------
# Dictionaries as data containers - each animal is represented as a dictionary
# -------------------------------
animalsdict = [
    {"name": "Tiger", "colour": "Orange", "pattern": "Stripes"},
    {"name": "Zebra", "colour": "Black & White", "pattern": "Stripes"},
    {"name": "Dalmatian", "colour": "White", "pattern": "Spots"},
    {"name": "Leopard", "colour": "Golden", "pattern": "Spots"}
]
print("Find animal with Stripes:", [animal for animal in animalsdict if animal["pattern"] == "Stripes"])

# -------------------------------
# Using namedtuple - (lightweight class-like objects)
# -------------------------------
import collections
Animal = collections.namedtuple("Animal", ["name", "colour", "pattern"])  # defined an "Animal" namedtuple with 3 fields
print("Associate data with columns:", Animal(name="Tiger", colour="Orange", pattern="Stripes"))

# create instances
animaltuples = [
    Animal("Tiger", "Orange", "Stripes"),
    Animal("Zebra", "Black & White", "Stripes"),
    Animal("Dalmatian", "White", "Spots"),
    Animal("Leopard", "Golden", "Spots")
]
print("Find animal with colour White:", [animal for animal in animaltuples if animal.colour == "White"])

Animal(**animalsdict[2]) # unpack dict into namedtuple
animaltuples[2]._asdict() # convert back to dict

# -------------------------------
# Using dataclasses (Python 3.7+)
# -------------------------------
import dataclasses
@dataclasses.dataclass # simple dataclass with default value
class Animaldata:
    name: str
    colour: str
    pattern: str = "Unknown"
animaldata = [
    Animaldata("Tiger", "Orange", "Stripes"),
    Animaldata("Zebra", "Black & White", "Stripes"),
    Animaldata("Dalmatian", "White", "Spots"),
    Animaldata("Leopard", "Golden", "Spots")
]
print("Filter Animals without Stripes:", [animal for animal in animaldata if animal.pattern != "Stripes"])

# -------------------------------
# Dataclass with methods & __str__ (string) representation
# -------------------------------
@dataclasses.dataclass
class Animaldata:
    name: str
    colour: str
    pattern: str = "Unknown"
    
    # when writing class methods; "self" refers to instances
    def description(self): # instance method to return full description
        return f"This is a {self.colour} {self.name} with {self.pattern}."

    def __str__(self):
        return f"Animal Name: {self.name}, Colour: {self.colour}, Pattern: {self.pattern}"

zebra = Animaldata("Zebra", "Black & White", "Stripes")
print(zebra.description())
print(zebra)

# -------------------------------
# Variants of dataclasses
# -------------------------------
@dataclasses.dataclass(frozen=True)  # immutable
class Animaldata_frozen:
    name: str
    colour: str
    pattern: str = "Unknown"

@dataclasses.dataclass(order=True)   # ordering support
class Animaldata_ordered:
    name: str
    colour: str
    pattern: str = "Unknown"

@dataclasses.dataclass # custom ordering by implementing __lt__
class Animaldata_customorder:
    name: str
    colour: str
    pattern: str = "Unknown"

    def __lt__(self, other): # custom "less than" comparison
        return (self.pattern, self.colour, self.name) < (other.pattern, other.colour, other.name)

# -------------------------------
# Dataclass with computed field
# -------------------------------
@dataclasses.dataclass
class Animaldata_computed:
    name: str
    colour: str
    pattern: str = "Unknown"
    description: str = dataclasses.field(init=False) # will compute it below; not passed in constructor

    def __post_init__(self):  # auto-called after initialization
        self.description = f"{self.colour} {self.name} with {self.pattern}"

# -------------------------------
# Pydantic dataclasses (validation)
# -------------------------------
import pydantic
@pydantic.dataclasses.dataclass
class Animaldata_pydantic:
    name: str
    colour: str
    pattern: str = "Unknown"

    @pydantic.field_validator("pattern")
    def validate_pattern(cls, value):  # a class method, so first argument is the class
        allowed_patterns = ["Stripes", "Spots", "Solid", "Unknown"]
        if value not in allowed_patterns:
            raise ValueError(f"Pattern must be one of {allowed_patterns}")
        return value

print(Animaldata_pydantic("Tiger", "Orange", "Stripes"))
print(Animaldata_pydantic("Leopard", "Golden", "Spots"))