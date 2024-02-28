import requests
import json
response = requests.get("https://huggingface.co/api/models?author=mlx-community&full=true&config=true")
if response.status_code == 200:
    data = json.loads(response.text)
    with open("all_models.txt", "w") as file:
        for value in data:
            file.write(value["id"] + "\t|\t" + value["id"] + "\n")
else:
    print("Error:", response.status_code)
