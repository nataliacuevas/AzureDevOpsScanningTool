import yaml
import logging
from reportWarnings import reportWarning
from datetime import datetime
from ADOgroup import ADOgroup
from ADOuser import ADOuser


class configHandler:
    def __init__(self):
        self.configFile = "reportConfig.yaml"

        with open(self.configFile, 'r') as file:
            self.data : dict = yaml.safe_load(file)

    def MaxNumberProjectAdmins(self):
        return self.data["MaxNumberProjectAdmins"]
    
class reportHandler:
    def __init__(self):
        now = datetime.now()
        self.reportFile = f"ADO Report {now.year}-{now.month}-{now.day}.yaml"
        self.content : dict = {}

    def addWarnings(self, warnings: list[reportWarning]) -> None:
        logging.debug("Adding warnings to report")
        if len(warnings) == 0:
            self.content["WARNINGS"] = "There are no warnings. CONGRATULATIONS!!! "
        else: 
            self.content["WARNINGS"] = [rWarning.toDict() for rWarning in warnings]
    
    def addBody(self, orgName: str, projectAdmins: dict[ADOgroup, list[ADOuser]])-> None:
        logging.debug("Adding body to report")
        self.content[orgName] =  [self.formProjectBlock(group.getProjectName(), admins)
                                    for group, admins in projectAdmins.items()]

    def formProjectBlock(self, project: str, admins: list[ADOuser])-> dict:
        return {project: {"AdminNumber": len(admins),
                          "Admins": [admin.displayName for admin in admins]}}
    
    def generateReport(self) -> None:
        with open(self.reportFile, 'w') as file:
            yaml.dump(self.content, file, sort_keys=False)
        logging.info(f"Report Generated as File {self.reportFile}")