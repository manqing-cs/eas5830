import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI2MGU5N2EyMS1iMDBmLTQyZGYtODhmOS1jZTEwMTEzODVmYmEiLCJlbWFpbCI6Im1hbnFpbmdjYW9AZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImI3YTAyNjE2ODM5NjkyMWNlNmM4Iiwic2NvcGVkS2V5U2VjcmV0IjoiNTY3ZmNmMWJkMmVkNWQ4ODNjZDkyMTQ0MjIxMWFkZDQwMjY5YTYyNGIzZGRhOTM3NzU3YjY0YjM4ZWExMzQ5NCIsImV4cCI6MTc3MzQ4MDc5MH0.nvZHj2jGH4D6VnkQpMZqKNtMCWSTvRRx1PaseO1EVgU",
    "Content-Type": "application/json"
	}

	url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

	response = requests.request("POST", url, json=data, headers=headers)
	cid = response.json()["IpfsHash"]
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = "https://api.pinata.cloud/data/pinList"
	headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI2MGU5N2EyMS1iMDBmLTQyZGYtODhmOS1jZTEwMTEzODVmYmEiLCJlbWFpbCI6Im1hbnFpbmdjYW9AZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImI3YTAyNjE2ODM5NjkyMWNlNmM4Iiwic2NvcGVkS2V5U2VjcmV0IjoiNTY3ZmNmMWJkMmVkNWQ4ODNjZDkyMTQ0MjIxMWFkZDQwMjY5YTYyNGIzZGRhOTM3NzU3YjY0YjM4ZWExMzQ5NCIsImV4cCI6MTc3MzQ4MDc5MH0.nvZHj2jGH4D6VnkQpMZqKNtMCWSTvRRx1PaseO1EVgU"}
	response = requests.request("GET", url, headers=headers)

	data = response.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
