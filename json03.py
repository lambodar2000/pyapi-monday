#!/usr/bin/python3

import json

def main():
    hitchhikers = [{"mame": "Zphod Beeelebrox","species": "Beterlgeusian"},{"name":"Arthur Dent","species":"Human"}]
    print(hitchhikers)

    with open("guide.galaxy", "w") as guide:
        json.dump(hitchhikers,guide)

    print("---------------------------------------------")
    print(type(hitchhikers))
    
    myjson = json.dumps(hitchhikers)
    print(type(myjson))
    print(hitchhikers[1])
    print(myjson[1])
main()

