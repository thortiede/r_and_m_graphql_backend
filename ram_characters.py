from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

'''
Target is something like this:
{
  characters(page:3, filter:{name:"Rick"}) {

    results {
      id
      name
      status
      species
      location{
        name
        type
      }
    }

  }
}
'''

# Define some sample Characters

all_characters = [
        {
            "id": "1",
            "name": "Rick Sanchez",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "2",
            "name": "Morty Smith",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "3",
            "name": "Summer Smith",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Female",
        },
        {
            "id": "4",
            "name": "Beth Smith",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Female",
        },
        {
            "id": "5",
            "name": "Jerry Smith",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "6",
            "name": "Abadango Cluster Princess",
            "status": "Alive",
            "species": "Alien",
            "type": "",
            "gender": "Female",
        },
        {
            "id": "7",
            "name": "Abradolf Lincler",
            "status": "unknown",
            "species": "Human",
            "type": "Genetic experiment",
            "gender": "Male",
        },
        {
            "id": "8",
            "name": "Adjudicator Rick",
            "status": "Dead",
            "species": "Human",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "9",
            "name": "Agency Director",
            "status": "Dead",
            "species": "Human",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "10",
            "name": "Alan Rails",
            "status": "Dead",
            "species": "Human",
            "type": "Superhuman (Ghost trains summoner)",
            "gender": "Male",
        },
        {
            "id": "11",
            "name": "Albert Einstein",
            "status": "Dead",
            "species": "Human",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "12",
            "name": "Alexander",
            "status": "Dead",
            "species": "Human",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "13",
            "name": "Alien Googah",
            "status": "unknown",
            "species": "Alien",
            "type": "",
            "gender": "unknown",
        },
        {
            "id": "14",
            "name": "Alien Morty",
            "status": "unknown",
            "species": "Alien",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "15",
            "name": "Alien Rick",
            "status": "unknown",
            "species": "Alien",
            "type": "",
            "gender": "Male",
        },
        {
            "id": "16",
            "name": "Amish Cyborg",
            "status": "Dead",
            "species": "Alien",
            "type": "Parasite",
            "gender": "Male",
        },
        {
            "id": "17",
            "name": "Annie",
            "status": "Alive",
            "species": "Human",
            "type": "",
            "gender": "Female",
        },
        {
            "id": "18",
            "name": "Antenna Morty",
            "status": "Alive",
            "species": "Human",
            "type": "Human with antennae",
            "gender": "Male",
        },
        {
            "id": "19",
            "name": "Antenna Rick",
            "status": "unknown",
            "species": "Human",
            "type": "Human with antennae",
            "gender": "Male",
        },
        {
            "id": "20",
            "name": "Ants in my Eyes Johnson",
            "status": "unknown",
            "species": "Human",
            "type": "Human with ants in his eyes",
            "gender": "Male",
        }
    ]


# Simple schema definition by String
type_defs = gql("""
    type Query {
        characters(filter: FilterCharacter): [Character!]!
    }

    type Character {
        id: ID
        name: String
        status: String
        species: String
        type: String
        gender: String
    }
    
    input FilterCharacter {
        name: String
        names: [String]
        status: String
    }
""")

# Map resolver functions to Query fields using QueryType
query = QueryType()

# Method for filtering down the list of all characters according to the provided filter item
def get_filtered_characters(filter):
    ret = []
    applied_filter = False
    if "name" in filter:
        ret += [char for char in all_characters if filter["name"] in char["name"]]
        applied_filter = True
    elif "names" in filter:
        for name in filter["names"]:
            ret += [char for char in all_characters if name in char["name"]]
        applied_filter = True
    if "status" in filter:
        status = filter["status"]
        if applied_filter:
            ret = [char for char in ret if status == char["status"]]
        else:
            ret = [char for char in all_characters if status == char["status"]]
        applied_filter = True

    ''' Add more filter types here.. '''

    return ret


# Resolver for the characters field
@query.field("characters")
def resolve_characters(*_, filter=None):
    if filter:
        return get_filtered_characters(filter)
    else:
        return all_characters




# Map resolver functions to custom type fields using ObjectType
character = ObjectType("Character")

# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, character)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)