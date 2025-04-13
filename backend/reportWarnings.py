from configHandler import configHandler
from ADOuser import ADOuser
from ADOgroup import ADOgroup




class reportWarning:
    def __init__(self, name: str, id: int, category: str, severity: str, recommendation: str, project: str):
        self.name = name
        self.id = id
        self.category = category
        self.severity = severity
        self.recommendation = recommendation
        self.project = project

    def toDict(self):
        return {"name": self.name,
                "id": self.id,
                "category": self.category,
                "severity": self.severity,
                "recommendation": self.recommendation,
                "project": self.project
                }

    @staticmethod
    def createMaxAdminWarning(group: ADOgroup, admins: list[ADOuser]):
        totalAdmins = len(admins)
        configuration = configHandler()
        recommendedMaxAdmins : int = configuration.MaxNumberProjectAdmins()
        if totalAdmins > recommendedMaxAdmins:
            warning = reportWarning(name="Too many admins",
                                    id= 1,
                                    category="Permissions Management", 
                                    severity="High", 
                                    recommendation="Audit and reduce number of project administrators",
                                    project= group.getProjectName())
            return warning
        return None
    
    @staticmethod
    def createMaxAdminWarningList(adminsDict: dict[ADOgroup, list[ADOuser]]) -> list["reportWarning"] :
        output =  [reportWarning.createMaxAdminWarning(group, admins) for group,admins in adminsDict.items()]
        return [out for out in output if out is not None]


