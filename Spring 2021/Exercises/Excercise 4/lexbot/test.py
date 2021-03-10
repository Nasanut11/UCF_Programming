from lambda_function import lambda_handler
sampleRequest = {
    "messageVersion": "1.0",
    "invocationSource": "DialogCodeHook",
    "userId": "John",
    "sessionAttributes": {},
    "bot": {
        "name": "BookTrip",
        "alias": "$LATEST",
        "version": "$LATEST"
    },
    "outputDialogMode": "Text",
    "currentIntent": {
        "name": "four",
        "slots": {
            "upper": 3,
            "lower": 3,
        },
        "confirmationStatus": "None"
    }
}
print(lambda_handler(sampleRequest, {}))
