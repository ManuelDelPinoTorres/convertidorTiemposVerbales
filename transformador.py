import re

irregularVerbs = {
    "arise": "arose",
    "be": "was/were",
    "beat": "beat"
    # incluir aqui todos los verbos irregulares
}


def past(infinitive):
    regular = False
    for key in irregularVerbs:
        if(infinitive == key):
            regular = True
    if(regular):
        return irregularVerbs[infinitive]
    else:
        if(infinitive[-1] == "e"):
            return (f"{infinitive}d")
        elif(re.search("[aeiou][^aeiou][y]", infinitive[-3:])):
            return (f"{infinitive[0:-1]}ied")
        elif(re.search("[aeiou][y]", infinitive[-2:])):
            return (f"{infinitive}ed")
        elif(re.search("[aeiou][^aeiou]", infinitive[-2:])):
            return (f"{infinitive}{infinitive[-1]}ed")
        else:
            return (f"{infinitive}ed")


def gerund(infinitive):
    if(re.search("[^i][e]", infinitive[-2:]) and len(infinitive) > 2):
        return (f"{infinitive[0:-1]}ing")
    elif(re.search("[aeiou][^aeiou]", infinitive[-2:])):
        return (f"{infinitive}{infinitive[-1]}ing")
    elif(re.search("[i][e]", infinitive[-2:])):
        return (f"{infinitive[0:-2]}ying")
    else:
        return (f"{infinitive}ing")


def thirdps(infinitive):
    if(infinitive == "be"):
        return "is"
    else:
        if(re.search("[c][h]|[s][h]|[s][s]", infinitive[-2:]) or re.search("[x]|[o]", infinitive[-1:])):
            return (f"{infinitive}es")
        elif(re.search("[^aeiou][y]", infinitive[-2:])):
            return (f"{infinitive[0:-1]}ies")
        else:
            return (f"{infinitive}s")


def principal(infinitive):
    print(past(infinitive))
    print(gerund(infinitive))
    print(thirdps(infinitive))


verb=""
while(verb != "-1"):
    verb = input('Introduce a verb(to exit tipe -1)')
    if(verb != "-1"):
        principal(verb)
    else:
        print("See you soon...")
    
