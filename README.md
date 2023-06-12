# Information Gathering Tool

The Information Gathering Tool is a Python script that enables users to gather various information related to a domain name. It retrieves whois information, DNS records, geolocation data, and can optionally perform a Shodan search for the associated IP address. The gathered information can be saved to an output file for further analysis and reference.

## Features

- Retrieves whois information for a specified domain name, including registrar, creation date, expiration date, and registrant details.
- Fetches DNS records (A, NS, MX, TXT) associated with the domain name.
- Retrieves geolocation data based on the domain's IP address, including country, latitude, longitude, city, and state.
- Performs a Shodan search (optional) to gather information about the associated IP address, such as device data and exposure.
- Supports saving the gathered information to an output file for future reference.

## Prerequisites

Before running the script, ensure that you have the following dependencies installed:

- Python 3.x
- `whois` library: `pip install python-whois`
- `dns.resolver` library (part of `dnspython`): `pip install dnspython`
- `shodan` library: `pip install shodan`
- `requests` library: `pip install requests`

To use the Shodan search feature, you'll need a valid Shodan API key. You can sign up for an account and obtain an API key from the [Shodan website](https://shodan.io).

## Usage

1. Clone or download the project to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the script using the following command:

   ```
   python info_gathering.py -d DOMAIN [-s IP] [-o OUTPUT_FILE]
   ```

   - Replace `DOMAIN` with the target domain name you want to gather information about.
   - Replace `IP` (optional) with the associated IP address if available. This is required for the Shodan search.
   - Replace `OUTPUT_FILE` (optional) with the desired file path to save the gathered information. If not specified, the results will be printed to the console.

4. The script will start gathering information and display the results on the console or save them to the specified output file.

## Examples

- Gather information for a domain:

  ```
  python info_gathering.py -d example.com
  ```

- Perform a Shodan search for an IP address:

  ```
  python info_gathering.py -d example.com -s 123.456.789.0
  ```

- Save the results to an output file:

  ```
  python info_gathering.py -d example.com -o results.txt
  ```

## Limitations

- The accuracy and availability of the gathered information depend on the availability and reliability of external services (e.g., whois databases, DNS servers, geolocation APIs, Shodan API).
- The script may encounter errors or limitations when accessing certain resources, depending on the network configuration and restrictions.
- The geolocation data may not be 100% accurate, as it relies on IP address mapping to physical locations.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal and commercial purposes.
