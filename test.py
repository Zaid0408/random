import requests

def make_api_call(url):
  """Makes a GET request to the specified URL and returns the response."""
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for error HTTP status codes
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"Error making API call: {e}")
    return None

if __name__ == "__main__":
  api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Example endpoint
  response_data = make_api_call(api_url)
  if response_data:
    print(response_data)
