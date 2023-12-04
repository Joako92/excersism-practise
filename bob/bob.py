def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!" 
    if hey_bob.endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."    
    if hey_bob.isupper():
        return "Whoa, chill out!"    
    return "Whatever."


print(response("Hola"))
