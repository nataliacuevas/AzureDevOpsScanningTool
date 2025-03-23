import argparse
import base64
import requests

class ADOrequester:
    def __init__(self, pat: str, org: str):
        self.pat = pat
        self.org = org

    def getHeaders(self) -> dict:       
        # Encode the PAT in Base64 - required by Azure DevOps API -
        pat_base64 = base64.b64encode(f":{self.pat}".encode()).decode()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {pat_base64}"
        }
        return headers
    
    def GETrequest(self, urlSuffix: str, domain: str = "dev.azure.com") -> any:
        url = f"https://{domain}/{self.org}/_apis/{urlSuffix}"
        print(f"GET {url}")
        # Set up the headers with the PAT for authentication
        headers = self.getHeaders()

        # Make the GET request
        response = requests.get(url, headers=headers)

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            raise Exception(response.text)
        
    def GETsecurityNamespaces(self) -> any: 
        return self.GETrequest("securitynamespaces/?api-version=7.1")
    
    def GETpermissionsGivenSecurityNamespaceId(self) -> any:
        securityNamespaceId = "52d39943-cb85-4d7f-8fa8-c6baac873819" # Project NamespaceID
        permissions = "1" 
        return self.GETrequest(f"permissions/{securityNamespaceId}/{permissions}?api-version=7.1")

    def GETlistOfUsersInOrg(self) -> any:
        return self.GETrequest("graph/users?api-version=7.1-preview.1", domain="vssps.dev.azure.com") 
    
    def GETallProjectsWithinOrg(self) -> any:
        return self.GETrequest("projects?api-version=7.1")

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

    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])

    response1 = requester.GETallProjectsWithinOrg()
    print(response1)

    # request(argsDict["Org"], argsDict["patToken"])
    # request2(argsDict["Org"], argsDict["patToken"])
    # request4(argsDict["Org"], argsDict["patToken"])

if __name__ == "__main__":
    main()
