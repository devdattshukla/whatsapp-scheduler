response = requests.post(url, headers=headers, json=data)

print("STATUS CODE:", response.status_code)
print("RESPONSE:", response.text)
