import json
import random
import markovify


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
             "Bleach", "One Piece", "Tokyo Ghoul", "Black Torch", "Jujitsu Kaisen", "Your Lie in April", "Akudama Drive", "High Rise Invasion"]
    if event["currentIntent"]["name"] == "anime":
        result["dialogAction"]["message"]["content"] = (secrets.choice(title))

    elif event["currentIntent"]["name"] == "four":
        upper = event["currentIntent"]["slots"]["upper"]
        lower = event["currentIntent"]["slots"]["lower"]
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
    elif event["currentIntent"]["name"] == "AskAusten":
        with open("./austen-pride-and-prejudice.txt") as f:
            text = f.read()
            # Build the model.
            text_model = markovify.Text(text)
            sentences = []
            # Print five randomly-generated sentences
            for i in range(5):
                # Print three randomly-generated sentences of no more than 280 characters
                sentences.append(text_model.make_sentence())
            result["dialogAction"]["message"]["content"] = ". ".join(sentences)
    elif event["currentIntent"]["name"] == "AddNumbers":
        # Handle intent 2
        result["dialogAction"]["message"]["content"] = upper+lower
    return result
