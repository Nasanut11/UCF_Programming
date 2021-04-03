def lambda_handler(event, context):

    # TODO implement
    result = {
        "dialogAction":
        {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText"
            }
        }
    }
    import secrets
    title = ["Attack on Titan", "Naruto", "Naruto: Shippuden", "Boruto: Naruto Next Generations", "Death Note", "Sword of the Stranger", "Natsume's Book of Friends",
             "Full Metal Alchemist: Brotherhood", "One Punch Man", "My Hero Academia", "Cowboy Bebop", "Magi Series", "Erased", "Yuri on Ice", "Sword Art Online", "Haikyu", 
             "Bleach", "One Piece", "Tokyo Ghoul", "Black Torch", "Jujitsu Kaisen", "Your Lie in April", "Akudama Drive", "High Rise Invasion", "Pokemon: Indigo Leauge", 
             "Pokemon: Adventures in the Orange Islands", "Pokemon: The Johto Journeys", "Pokemon: Johto League Champions", "Pokemon: Master Quest"]
    if event["currentIntent"]["name"] == "anime":
        result["dialogAction"]["message"]["content"] = (secrets.choice(title))
    
    elif event["currentIntent"]["name"] == "four":
        upper = int(event["currentIntent"]["slots"]["upper"])
        lower = int(event["currentIntent"]["slots"]["lower"])
        # Do the intent 1
        randomNum = str(random.randint(lower, upper))
        result["dialogAction"]["message"]["content"] = "Your random number is " + randomNum
        if event["sessionAttributes"]:
            result["dialogAction"]["message"]["content"] += ". The last random number was " + \
                event["sessionAttributes"]["lastNumber"]
        result["sessionAttributes"] = {
            "lastNumber": randomNum,
            "lower": event["currentIntent"]["slots"]["lower"],
            "upper": event["currentIntent"]["slots"]["upper"]}
    return result
