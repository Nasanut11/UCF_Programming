import json
import random

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

# give me a flower
if event["currentIntent"]["name"] == "flowerintent":
    flowers = ["White Rose", "Red Rose", "Yellow Rose", "Pink Rose", "Golden Rose", "Blue Rose", "Orange Rose", "Purple Rose", "Black Rose", 
                "Red Tulip", "Yellow Tulip", "White Tulip", "Purple Tulip", "Pink Tulip", "Orange Tulip", "Black Tulip", 
                "White Hyacinth", "Red Hyacinth", "Yellow Hyacinth", "Purple Hyacinth", "Orange Hyacinth", "Blue Hyacinth", "Pink Hyacinth", 
                "White Mum", "Red Mum", "Yellow Mum", "Pink Mum", "Purple Mum", "Green Mum", 
                "Yellow Pansy", "White Pansy", "Red Pansy", "Orange Pansy", "Blue Pansy", "Purple Pansy", 
                "Red Lily", "Yellow Lily", "White Lily", "Pink Lily", "Orange Lily", "Black Lily", 
                "White Windflower", "Red Windflower", "Orange Windflower", "Pink Windflower", "Purple Windflower", "Blue Windflower",
                "Red Cosmos", "Yellow Cosmos", "White Cosmos", "Black Cosmos", "Pink Cosmos", "Orange Cosmos",
                "Lily of the Valley"]
    
    flower = random.choice(flowers)
    result["dialogAction"]["message"]["content"] = flower
else:
    result["dialogAction"]["message"]["content"] = "Something went wrong..."

    
# item cost
elif event["currentIntent"]["name"] == "itemintent":
  item = event["currentIntent"]["slots"]["item"]
  dataset = [["imperial dresser", "8500"], ["imperial bed", "23000"], ["imperial low table", "3700"], ["imperial partition", "5000"], ["imperial dining chair", "29000"], 
            ["imperial dining table", "73000"], ["imperial dining lantern", "19000"]]
  items = ["imperial dresser", "imperial bed", "imperial low table", "imperial partition", "imperial dining chair", "imperial dining table", "imperial dining lantern"]
  
  if getitem in items:
    index = items.index(getitem)
    price = dataset[index][1]
    result["dialogAction"]["message"]["content"] = "Item costs "+ price + " Bells!"
  else:
    result["dialogAction"]["message"]["content"] = "item not found in list!"


# nookmiles tickets
elif event["currentIntent"]["name"] == "ticketsintent":
  villager = event["currentIntent"]["slots"]["villager"]
  villagers = ["Sprocket", "Tiffany", "Cube", "Audie", "Raymond", "Ribbot"]
  if villager in villagers:
    tickets = random.randint(1,100)
    result["dialogAction"]["message"]["content"] = str(tickets) + "Nookmile Tcikets"
  else:
    result["dialogAction"]["message"]["content"] = "try again!"


# turnip prices
elif event["currentIntent"]["name"] == "turnipintent":
  prices = random.randint (60, 200)
  result["dialogAction"]["message"]["content"] = "Turnip prices today are: " + str(prices)


# bugs per season
elif event["currentIntent"]["name"] == "bugsintent":
  getmonth = event["currentIntent"]["slots"]["month"]
  dataset = [["january", "Common Butterfly, Paper Kite Butterfly, Emperor Butterfly, Moth, Wasp, Damselfly, Mole Cricket, Citrus Long-Horned Beetle, Dung Beetle, Ant, Fly"], 
             ["march", "Common Butterfly, Paper Kite Butterfly, Emperor Butterfly, Moth, Wasp, Damselfly, Mole Cricket, Citrus Long-Horned Beetle, Dung Beetle, Ant, Fly, Stinkbug"]]
  month = ["january", "march"]
  
  if getmonth in month:
    index = month.index(getmonth)
    bugs = dataset[index][1]
    result["dialogAction"]["message"]["content"] = "The for this month are: " + bugs
  else:
    result["dialogAction"]["message"]["content"] = "Month not found."


else:
  result["dialogAction"]["message"]["content"] = "please try again!"