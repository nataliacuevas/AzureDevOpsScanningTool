import base64
import requests
from ADOuser import ADOuser
from ADOproject import ADOproject
from ADOgroup import ADOgroup


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
        
    def POSTrequest(self, urlSuffix: str, body: any, domain: str = "dev.azure.com") -> any:
        url = f"https://{domain}/{self.org}/_apis/{urlSuffix}"
        print(f"POST {url}")
        # Set up the headers with the PAT for authentication
        headers = self.getHeaders()

        # Make the POST request with the provided body
        response = requests.post(url, headers=headers, json=body)

        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return data
        else:
            print(f"Failed to post data. Status code: {response.status_code}")
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

    def getProjectList(self) -> list[ADOproject]:
        response : dict = self.GETallProjectsWithinOrg()
        value : list[dict] = response['value']
        projects = [ADOproject(val) for val in value]
        return projects
    
    def getUserList(self) -> list[ADOuser]:
        response : dict = self.GETlistOfUsersInOrg()
        value : list[dict] = response['value']
        users = [ADOuser(val) for val in value]
        return users
    
    def GETGroupList(self) -> any:
        return self.GETrequest("graph/groups?api-version=7.1-preview.1", domain="vssps.dev.azure.com")
    
    def getGroupList(self) -> list[ADOgroup]:
        response : dict = self.GETGroupList()
        value : list[dict] = response['value']
        groups = [ADOgroup(val) for val in value]
        return groups

    def GETgroupMembers(self, group: ADOgroup) -> any: 
        return self.GETrequest(f"graph/Memberships/{group.descriptor}?direction=down&api-version=7.1-preview.1", domain="vssps.dev.azure.com")
    
    def getGroupMembers(self, group: ADOgroup) -> list[ADOgroup | ADOuser]:
        response : dict = self.GETgroupMembers(group)
        value : list[dict] = response['value']
        descriptors : list[str] = [val['memberDescriptor'] for val in value]
        return self.lookupDescriptors(descriptors)         
    
    def POSTlookupDescriptors(self, descriptors: list[str]) -> any:
        descList : list[dict] = [{"descriptor": val} for val in descriptors]
        body : dict = {"lookupKeys": descList}
        return self.POSTrequest(f"graph/subjectLookup?api-version=7.1-preview.1", body,  domain="vssps.dev.azure.com")
    
    def lookupDescriptors(self, descriptors: list[str]) -> list[ADOgroup |ADOuser]:
        response : dict = self.POSTlookupDescriptors(descriptors)
        value : dict = response['value']
        output = []
        for descriptor in descriptors:
            subject = value[descriptor]
            if subject['subjectKind'] == 'user':
                output.append(ADOuser(subject))
            elif subject['subjectKind'] == 'group':
                output.append(ADOgroup(subject))
            else: 
                raise Exception(f'Unexpected Subject Kind: {subject}')
            
        return output
