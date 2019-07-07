def rand_hpc(): #Random Harry-Potter-Character
    import creds #Stores the API-Key
    import json
    from random import randint
    from urllib.request import Request, urlopen

    #Requesting all characters from Potter-API
    req=Request(f"https://www.potterapi.com/v1/characters?key={creds.api_key}", headers={'User-Agent': 'Mozilla/5.0'})
    all_hpc=json.loads(urlopen(req).read())

    #Randome character
    r_hpc_index=randint(0, len(all_hpc)-1)
    r_hpc=all_hpc[r_hpc_index]

    #Final dictionary of random character
    d_r_hpc={
        "name": r_hpc["name"],
        "deathEater": r_hpc["deathEater"],
        "orderOfThePhoenix": r_hpc["orderOfThePhoenix"],
        "dumbledoresArmy": r_hpc["dumbledoresArmy"],
        "ministryOfMagic": r_hpc["ministryOfMagic"],
        "species": r_hpc["species"]
    }

    return d_r_hpc
    
def rand_spell(): #Random Harry-Potter-Spell
    import creds #Stores the API-Key
    import json
    from random import randint
    from urllib.request import Request, urlopen

    #Requesting all spells from Potter-API
    req=Request(f"https://www.potterapi.com/v1/spells?key={creds.api_key}", headers={'User-Agent': 'Mozilla/5.0'})
    all_spells=json.loads(urlopen(req).read())

    #Random spell
    r_spell_index=randint(0, len(all_spells)-1)
    r_spell=all_spells[r_spell_index]

    #Final dictionary of random spell
    d_r_spell={
        "name": r_spell["spell"],
        "type": r_spell["type"],
        "effect": r_spell["effect"]
    }

    return d_r_spell

def __version__():
    return 0.1

if __name__ == "__main__":
    print(f"Version: {__version__()}\n")
    print("Random character")
    print(rand_hpc())
    print("\nRandome spell")
    print(rand_spell())
    ein=input("\nPress Enter!")