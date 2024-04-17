import pycurl
from io import BytesIO

# Define the URL to fetch
url = "http://example.com"

# Create a buffer to store the response
buffer = BytesIO()

# Create a PycURL object
c = pycurl.Curl()

# Set the URL to retrieve
c.setopt(c.URL, url)

# Set the buffer to write the response to
c.setopt(c.WRITEDATA, buffer)

# Perform the GET request
c.perform()

# Get the HTTP response code
http_code = c.getinfo(pycurl.HTTP_CODE)

# Close the connection
c.close()

# Get the response content as a string
response = buffer.getvalue().decode('utf-8')

# Print the HTTP response code and content
print(f"HTTP Response Code: {http_code}")
print(f"Response:\n{response}")
