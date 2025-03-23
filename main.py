import argparse
import base64
import requests

def getHeaders(pat: str) -> dict:       
    # Encode the PAT in Base64 - required by Azure DevOps API -
    pat_base64 = base64.b64encode(f":{pat}".encode()).decode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {pat_base64}"
    }
    return headers

def request(organization: str, pat: str) -> None:
    # Construct the URL
    url = f"https://dev.azure.com/{organization}/_apis/securitynamespaces/?api-version=7.1"

    # Set up the headers with the PAT for authentication
    headers = getHeaders(pat)

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.text)

def request2(organization: str, pat: str) -> None:
    
    securityNamespaceId = "52d39943-cb85-4d7f-8fa8-c6baac873819"
    permissions = "1"
    # Build URL
    url = f"https://dev.azure.com/{organization}/_apis/permissions/{securityNamespaceId}/{permissions}?api-version=7.1"

    # Set up the headers with the PAT for authentication
    headers = getHeaders(pat)

    # Make the GET request
    print(f"URL: {url}")
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.text)

def request3(organization: str, pat: str) -> None:
   
    securityNamespaceId = "52d39943-cb85-4d7f-8fa8-c6baac873819"
    permissions = "1"
    # Build URL
    url = f"https://vssps.dev.azure.com/{organization}/_apis/graph/users?api-version=7.1-preview.1"

    # Set up the headers with the PAT for authentication
    headers = getHeaders(pat)

    # Make the GET request
    print(f"URL: {url}")
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.text)


def request4(organization: str, pat: str) -> None:
   
    securityNamespaceId = "11238e09-49f2-40c7-94d0-8f0307204ce4"
    permissions = "4"
    token = "40a0d31a-8a2c-494b-87b2-45b081763bdd"
    # Build URL
    url = f"https://dev.azure.com/{organization}/_apis/permissions/{securityNamespaceId}/{permissions}?api-version=7.1"

    # Set up the headers with the PAT for authentication
    headers = getHeaders(pat)

    # Make the GET request
    print(f"URL: {url}")
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.text)

def request5(organization: str, pat: str) -> None:
   
    # Build URL
    url = f"https://dev.azure.com/{organization}/_apis/projects?api-version=7.1"

    # Set up the headers with the PAT for authentication
    headers = getHeaders(pat)

    # Make the GET request
    print(f"URL: {url}")
    response = requests.get(url, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(response.text)


def useArgParse() -> dict:
    # Create the parser
    parser = argparse.ArgumentParser(description="Azure DevOps Security Tool")

    # Add the PAT argument
    parser.add_argument('--pat', type=str, required=True, help='Provide personal access token')

    # Add the organization argument
    parser.add_argument('--org', type=str, required=True, help='Provide organization name')

    # Parse the arguments
    args = parser.parse_args()

    # Access the PAT
    return {"patToken": args.pat,
            "Org": args.org}

def main() -> None:
    argsDict = useArgParse()
    print(f"PAT: {argsDict['patToken']}, ORG: {argsDict['Org']}")
    # request(argsDict["Org"], argsDict["patToken"])
    # request2(argsDict["Org"], argsDict["patToken"])
    request4(argsDict["Org"], argsDict["patToken"])

if __name__ == "__main__":
    main()
