import requests
import json

url = "https://webexapis.com/v1/messages"

payload = json.dumps({
  "toPersonEmail": "jyepezri@cisco.com",
  "text": "test from Visual"
})
headers = {
  'Authorization': 'Bearer NzAxODdiYTItY2M2ZC00ZWZmLWIzYmYtYzI2Y2QwYzRlMjg1YzRhOTE4MmYtODVi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)