import requests
import json
from azureml.core import Webservice

from azureml.core import Workspace
ws = Workspace.from_config()
service = Webservice(workspace=ws, name="myservice")
scoring_uri = service.scoring_uri

# If the service is authenticated, set the key or token
key, _ = service.get_keys()

# Set the appropriate headers
headers = {"Content-Type": "application/json"}
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response and logs
data = {
    "query": "What color is the fox",
    "context": "The quick brown fox jumped over the lazy dog.",
}
data = json.dumps(data)
resp = requests.post(scoring_uri, data=data, headers=headers)
print(resp.text)
