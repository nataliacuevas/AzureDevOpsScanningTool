class ADOgroup: 
    def __init__(self, propertiesResponse : dict):
        # Standard project attributes
        self.subjectKind   = propertiesResponse['subjectKind']
        self.description   = propertiesResponse['description']
        self.domain        = propertiesResponse['domain']
        self.principalName = propertiesResponse['principalName']
        self.mailAddress   = propertiesResponse['mailAddress']
        self.origin        = propertiesResponse['origin']
        self.originId      = propertiesResponse['originId']
        self.displayName   = propertiesResponse['displayName']
        self._links        = propertiesResponse['_links']
        self.url           = propertiesResponse['url']
        self.descriptor    = propertiesResponse['descriptor']

        
    def __str__(self):
        return (f"Subject Kind: {self.subjectKind}\n"
                f"Description: {self.description}\n"
                f"Domain: {self.domain}\n"
                f"Principal Name: {self.principalName}\n"
                f"Mail Address: {self.mailAddress}\n"
                f"Origin: {self.origin}\n"
                f"Origin ID: {self.originId}\n"
                f"Display Name: {self.displayName}\n"
                f"Links: {self._links}\n"
                f"URL: {self.url}\n"
                f"Descriptor: {self.descriptor}")