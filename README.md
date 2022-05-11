## Rick and Morty Characters API
This is a small demo for building a GraphQL API server.

It uses some data from the [Rick and Morty GraphQL API](https://rickandmortyapi.com/graphql) 
and does mimik its behaviour for the 'characters' element only.

### Dependencies
The full list of dependencies can be found in the [requirments.txt file](./requirements.txt).
Most notably, this demo uses the [ariadne](https://github.com/mirumee/ariadne) package to 
power the API backend and the [uvicorn package](http://www.uvicorn.org/) to provide the
ASGI web server.

This software requires Python >=3.7 has been tested with Python 3.8.12.

### Running this demo
To run this demo, clone the repository, make sure to install all needed dependencies 
(we leave the management of your environment to you) with

    pip install -r requirements.txt

and then run

    uvicorn ram_characters:app

### Accessing the API
After running the above command, an ASGI webserver should be running with the default settings at

    http://127.0.0.1:8000

Navigate to this address using your favourite browser or HTTP-client
and submit your query as json-formatted body in a POST request, for example:

    {
        characters {
            id
            name
            status
            species
            type
            gender
        }
    }

### Filtering
The result set can be filtered by name and status of the character
You can search for a single name, or multiple names.
The single name search takes precedence of searching with multiple names.

###### Filter the characters by name.
     {
        characters(filter: {name:"Morty"}) {
            id
            name
            status
            species
            type
            gender
        }
    }

###### Filter the characters by multiple names.
When you search with multiple names, all characters satisfying at least one entry in the provided list will be returned.

     {
        characters(filter: {names: ["Morty", "Rick"]}) {
            id
            name
            status
            species
            type
            gender
        }
    }

###### Filter the characters by status.
     {
        characters(filter: {status:"Alive"}) {
            id
            name
            status
            species
            type
            gender
        }
    }
###### Filter the characters by name and status.
     {
        characters(filter: {name:"Rick", status:"Dead"}) {
            id
            name
            status
            species
            type
            gender
        }
    }



### Open issues
- Implement Pagination by using the `Connection` type as wrapper 
and introduce the fields *info* and *results* as top level elements 
to conform to the best practices for GraphQL
- Add a sub-element 'location' to each character to closer mimic the original API.