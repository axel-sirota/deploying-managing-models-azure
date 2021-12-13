import requests
import json

# uri = service.scoring_uri
requests.get("http://localhost:6789")
headers = {"Content-Type": "application/json"}
data = {
    "query": "What color is the fox",
    "context": "The quick brown fox jumped over the lazy dog.",
}
data = json.dumps(data)
response = requests.post("http://localhost:6789/score", data=data, headers=headers)
print(response.text)
