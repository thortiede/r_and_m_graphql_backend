This is a small demo for building a GraphQL API server.

It uses some data from the [Rick and Morty GraphQL API](https://rickandmortyapi.com/graphql) 
and does mimik its behaviour for the 'characters' element only.

### Dependencies
The full list of dependencies can be found in the [requirments.txt file](./requirements.txt).
Most notably, this demo uses the [ariadne](https://github.com/mirumee/ariadne) package to 
power the API backend and the [uivorn package](http://www.uvicorn.org/) to provide the
ASGI web server.

### Running this demo
To run this demo, clone the repository, make sure to install all needed dependencies 
(we leave the management of your environment to you) with

    pip install -r requirements.txt

and then run

    uvicorn ram_characters:app

### Accessing the API
After running the above command, an ASGI webserver should be running with the default settings at

    http://127.0.0.1:8000

Navigate to this address using your favourite browser or HTTP-client and submit your query in a POST request, for example:

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

### Open issues
This demo still needs to add the ability to filter the characters by name.