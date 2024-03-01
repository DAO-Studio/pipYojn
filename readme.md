# Yojn Class

The Yojn class provides a simple interface for making HTTP POST requests to various endpoints of the Yojn API.

## Usage

To use the Yojn class, follow these steps:

### Import the Yojn class into your Python script:

from yojn import Yojn


python

from yojn import Yojn
Initialize an instance of the Yojn class with the base URL of the Yojn API.

python

base_url = "http://example.com/api"
yojn = Yojn(base_url)
Call the desired method of the Yojn class to make a POST request to the corresponding endpoint of the Yojn API.

python
config = {
    "json": {
        "userId": ,
        "orgId": ,
        "authKey": ,
        "app": ,
        "groupChatId": ""
    }
}
response = yojn.initializeYojn(config)
Methods
initializeYojn(config)

Parameters:

config (dict): A dictionary containing the configuration options for the request. The configuration may include headers, parameters, or JSON data.
Returns:

A dictionary representing the JSON response from the API.
runYojn(config)


Parameters:

config (dict): A dictionary containing the configuration options for the request. The configuration may include headers, parameters, or JSON data.
Returns:

A dictionary representing the JSON response from the API.
historyYojn(config)

Parameters:

config (dict): A dictionary containing the configuration options for the request. The configuration may include headers, parameters, or JSON data.
Returns:

A dictionary representing the JSON response from the API.
Error Handling
The Yojn class automatically handles HTTP errors and raises exceptions if the request fails. You can catch these exceptions and handle them appropriately in your code.

Dependencies
The Yojn class depends on the requests library for making HTTP requests. Make sure to install it before using the class.

pip install requests
