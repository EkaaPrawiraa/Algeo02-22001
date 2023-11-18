import requests

url = "http://localhost:8000/api/upload/single/"
headers = {"Authorization": "Token YOUR_API_TOKEN"}  # Replace YOUR_API_TOKEN with your actual API token

file_path = r"C:\Photo_from_Farid.jpg"  # Replace with the actual path to your image file

files = {"file": (file_path, open(file_path, "rb"))}

response = requests.post(url, headers=headers, files=files)

print(response.status_code)
print(response.text)
