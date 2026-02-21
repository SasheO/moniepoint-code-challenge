import requests

# URL of the Flask server
urls = [
"http://localhost:8080/analytics/top-merchant",
"http://localhost:8080/analytics/monthly-active-merchants",
"http://localhost:8080/analytics/product-adoption",
"http://localhost:8080/analytics/kyc-funnel",
"http://localhost:8080/analytics/failure-rates"
]

for url in urls:
    # Sending a GET request to the Flask server
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    print()
    print(url)
    if response.status_code == 200:
        # Parse the JSON response
        print(response.json())
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")