
import shlex
import pycurl
curl_to_pycurl_map = {
    # '-X': pycurl.HTTP_VE,
    '-H': pycurl.HTTPHEADER,
    '-d': pycurl.POSTFIELDS,
    '-u': pycurl.USERPWD,
    '-o': pycurl.WRITEDATA,
    '-k': pycurl.SSL_VERIFYHOST,  # Insecure SSL
    '--cacert': pycurl.CAINFO,   # CA certificate file
}

def parse_curl_string(curl_string):
  """
  Parses a curl string into a dictionary of options for pycurl.

  Args:
      curl_string: The curl command string to parse.

  Returns:
      A dictionary containing options for pycurl, or None if parsing fails.
  """
  try:
    # Split the curl string
    options = shlex.split(curl_string)

    # Map and store options
    pycurl_options = {}
    for i in range(1, len(options)):
      if options[i] in curl_to_pycurl_map:
        if options[i] == '-H':
          # Multiple headers in a list
          pycurl_options.setdefault(curl_to_pycurl_map[options[i]], []).append(options[i + 1])
        else:
          pycurl_options[curl_to_pycurl_map[options[i]]] = options[i + 1]
      else:
        # Handle unsupported options
        print(f"Warning: Unsupported curl option: {options[i]}")

    c = pycurl.Curl()

    c.setopt(c.URL, 'http://example.com -X GET')

    # c.setopt(pycurl.URL, curl_string)

    # for opt, value in pycurl_options.items():
    #     c.setopt(opt, value)

    c.perform()


    http_code = c.getinfo(pycurl.HTTP_CODE)

    return pycurl_options

  except Exception as e:
    print(f"Error parsing curl string: {e}")
    return None
