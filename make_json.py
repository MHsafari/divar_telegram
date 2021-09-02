import json

with open("data.json", "w") as json_data:
    data = {
        "my_token": "1815804020:AAHbxfIi2I1CQaylQ-Pjp4jIPosQAAECEkk",
        "chat_id": "-1001572436793",
        
        "my_token_car": "1989284238:AAHIPSYCi0gSeXZtVTsSSJ7v3mL2lGcbhZU",
        "chat_id_car": "-1001524790543",
        
        "my_token_mobile":"1963376161:AAEc4OZZC9unjueyzzEQPDexBDDFatBZeSk",
        "chat_id_mobile":"-1001522971851",
        
        "my_token_rent":"1996090629:AAHYfJK2HTz4lNn9yvXzXK7v0AWQczL7CAE",
        "chat_id_rent":"-1001175982650",
        
        "my_token_sell":"1982231457:AAHBPWQ_8YpjHLB8mG6zEiqg6C3qw7Bp5VE",
        "chat_id_sell":"-1001336474001",
        
        
        

    }
    d_json = json.dumps(data, indent=4)
    json_data.write(d_json)

f = open("data.json")
data=json.load(f)
print(data["my_token"])
