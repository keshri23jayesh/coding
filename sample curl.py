import random

import requests
import json

url = "http://localhost:8000/spaces/update_document/"


headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhPMU5HeUp1cUxBQWNta25ZeUpHUiJ9.eyJnaXZlbl9uYW1lIjoiSmF5ZXNoIEt1bWFyIiwiZmFtaWx5X25hbWUiOiJLZXNocmkiLCJuaWNrbmFtZSI6ImpheWVzaC5rZXNocmkiLCJuYW1lIjoiSmF5ZXNoIEt1bWFyIEtlc2hyaSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKNVZnNHl1TW5Ua25rMkhuQ3MxUU5BRlpBLUxvc1ptZkRyNlpXd2U0a2ZkMFRGLXc9czk2LWMiLCJ1cGRhdGVkX2F0IjoiMjAyNS0wMy0yMVQxMTowMzoxOC43MDNaIiwiZW1haWwiOiJqYXllc2gua2VzaHJpQHByZXN0b2xhYnMuYWkiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9wcmVzdG8udWsuYXV0aDAuY29tLyIsImF1ZCI6IkhJa1Y0RjkwaGJqMEs3UFQ3Z0dpdFQzZzRhNFE3U2ZCIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDk1NTA1MDEwOTUxOTQ2MzY4NDQiLCJpYXQiOjE3NDI1NTUwMDAsImV4cCI6MTc0MjU5MTAwMCwic2lkIjoib3M3Z1JtVk1maVJMeVlYT25NNy1SM1VsbHpoWjdPaVUiLCJub25jZSI6ImVITjJlQzFSZFdGbk0xRlVjVGhKYURCTlFtaEpUVkYrVWtwaFFtODFTblJuTmpSS01VSlNUM2RmTXc9PSJ9.ClK6ofmbUx7V4tvMXtuAwaVj85wEptJyZi3JqHtkuE-DGl0ghanZAkeSpkCGGDeZmIC-OQEQ0Cg2xUUCs_pSN-iN8VQdxGrARQbaIdw8ncMCXqpkcz4-E0y3gZG3V3gYh-6gBw_0h9VoErSL9fGSDtJk5mOrYHJtgTi_2pg0Ye0qc4PX539TW3q26n4RfqcYKidk98EPnA6Uby3OnsOxZ3CTXAwg27CvNpnmx4kKiNBuwYncn5vCa5FDmqp-9VtAFYV44NyK9wtq4oHYFqEYhOS4ORayorXqolDpki237K0evIVfP5mN9hyLibpuwdAvLUGvOTI7BMmboD6ZECiPeA',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json',
  'Origin': 'https://test.permi.tech',
  'Referer': 'https://test.permi.tech/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}


for i in range(100):
    doc_ids = ["d1547c40-03e6-4636-b10c-fa687501cbb7", "b1db4d9f-315c-4c55-9288-d40a8d418b82",
               "589b1f6e-d4d5-4a0b-a653-6c6f78f19959", "acddf0fd-974e-4d81-baca-d7aa8ef8567e",
               "631ae35f-844a-43aa-a2c1-b2f98ea78c8b", "99003fdc-b83e-444b-bd17-4e664a82fe3f",
               "652f4975-6db0-4ec7-9018-e84d1c6a1ddd", "c7c98505-2450-4a30-8749-84b0d8bd7bc0",
               "807c7a0f-c351-46b2-ad96-4d7f412faaac", "92699065-1626-4ae7-a7bb-000b91cb7173",
               "c0e8fa8c-abdb-4f7c-ab4d-c54aab2a8f6b"]
    doc_id = random.choice(doc_ids)
    payload = json.dumps({
      "document_id": doc_id,
      "url": "https://permi-tech-space.s3.amazonaws.com/5c28596f-9791-4fa0-b9ff-53b7e01170b2/dff725e9-6c52-4342-86fd-da5883a16603-document.txt"
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
