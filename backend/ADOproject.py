import datetime
from dateutil import parser

class ADOproject: 
    def __init__(self, propertiesResponse : dict):
        # Standard project attributes
        self.id = propertiesResponse['id']
        self.name = propertiesResponse['name']
        self.url = propertiesResponse['url']
        self.state = propertiesResponse['state']
        self.revision = propertiesResponse['revision']
        self.visibility = propertiesResponse['visibility']
        self.lastUpdateTime = self.parseDateTime(propertiesResponse['lastUpdateTime'])
        
    def parseDateTime(self, dateTime: str) -> datetime.datetime: 
        return parser.isoparse(dateTime.rstrip('Z'))  
    
    def __str__(self):
        return (f"Azure DevOps Project: {self.name}\n"
                f"ID: {self.id}\n"
                f"URL: {self.url}\n"
                f"State: {self.state}\n"
                f"Revision: {self.revision}\n"
                f"Visibility: {self.visibility}\n"
                f"Last Updated: {self.lastUpdateTime}")