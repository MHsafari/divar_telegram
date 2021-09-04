import json

with open("data.json", "w") as json_data:
    data = {
        "my_token": "yyyyyyyyyy",
        "chat_id": "yyyyyyyyyyy",
        
        "my_token_car": "yyyyyyyyyyy",
        "chat_id_car": "-yyyyyyyyyyy",
        
        "my_token_mobile":"yyyyyyyyyyy:yyyyyyyyyyy",
        "chat_id_mobile":"-yyyyyyyyyyy",
        
        "my_token_rent":"yyyyyyyyyyy:yyyyyyyyyyy",
        "chat_id_rent":"-yyyyyyyyyyy",
        
        "my_token_sell":"yyyyyyyyyyy:yyyyyyyyyyy",
        "chat_id_sell":"-yyyyyyyyyyy",
        
        
        

    }
    d_json = json.dumps(data, indent=4)
    json_data.write(d_json)

f = open("data.json")
data=json.load(f)
print(data["my_token"])
