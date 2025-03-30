import argparse
import logging
from dateutil import parser
from ADOuser import ADOuser
from ADOproject import ADOproject
from ADOrequester import ADOrequester
from ADOgroup import ADOgroup
from yamlHandler import configHandler, reportHandler
from reportWarnings import reportWarning


def useArgParse() -> dict:
    # Create the parser
    parser = argparse.ArgumentParser(description="Azure DevOps Security Tool")

    # Add the PAT argument
    parser.add_argument('--pat', type=str, required=True, help='Provide personal access token')

    # Add the organization argument
    parser.add_argument('--org', type=str, required=True, help='Provide organization name')

    helpMessage = "To set logging level, accepted values: INFO, DEBUG, WARNING, ERROR, CRITICAL"
    
    parser.add_argument("--loggingLevel", type=str, required=False, help=helpMessage, default="INFO")

    # Parse the arguments
    args = parser.parse_args()

    # Access the PAT
    return {"patToken": args.pat,
            "Org": args.org, 
            "loggingLevel": args.loggingLevel
            }

def configureLogging(loggingLevel: str):
    if loggingLevel == "INFO":
        level = logging.INFO
    elif loggingLevel == "DEBUG":
        level = logging.DEBUG
    elif loggingLevel == "CRITICAL":
        level = logging.CRITICAL
    elif loggingLevel == "WARNING":
        level = logging.WARNING
    elif loggingLevel == "ERROR":
        level = logging.ERROR
    else: 
        raise Exception(f"Unsupported Logging Level {loggingLevel}")
    
    logging.basicConfig(level=level, force=True)


def test_getNestedUserMembersofGroup():
    argsDict = useArgParse()
    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    descriptor = "vssgp.Uy0xLTktMTU1MTM3NDI0NS0yMDE1NjUxODU0LTM4MzE5MDQ4NDEtMzE1MDQ4MzU0NS0xMjk1OTE5NDY3LTAtMC0wLTAtMw"
    group : ADOgroup = requester.lookupDescriptors([descriptor])[0]
    logging.info(group)
    nestedMembers : list[ADOuser] = requester.getNestedUserMembersofGroup(group)
    for member in nestedMembers:
        logging.info(member)

def test_getUserList():
    argsDict = useArgParse()
    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    users = requester.getUserList()
    for user in users:
        logging.info(user)
        logging.info(80 * "*")

def test_getGroupList():
    argsDict = useArgParse()
    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    groups = requester.getGroupList()
    for group in groups:
        logging.info(group.principalName)
        members = requester.getGroupMembers(group)
        if len(members) == 0:
            logging.info('#  No Members')
        for member in members:
            logging.info(f"#  {member.displayName}")
        logging.info(80 * "*")

def test_getProjectList():
    argsDict = useArgParse()
    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    projects = requester.getProjectsList()
    for project in projects:
       logging.info(project)
       logging.info(80 * "*")

def test_getAllProjectAdmins():
    argsDict = useArgParse()
    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    adminDict : dict[ADOgroup, list[ADOuser]] = requester.getAllProjectAdmins()
    for key , value in adminDict.items():
        logging.info(key.principalName)
        for admin in value: 
            logging.info(admin)
            logging.info(80*"--")

def test_configHandler():
    reportConfig = configHandler()
    logging.info(f"Max Admins: {reportConfig.MaxNumberProjectAdmins()}" )

def main() -> None:
    argsDict = useArgParse()
    configureLogging(argsDict["loggingLevel"])
    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    adminDict : dict[ADOgroup, list[ADOuser]] = requester.getAllProjectAdmins()
    report = reportHandler()
    report.addWarnings([])
    report.addBody(argsDict["Org"], adminDict)
    report.generateReport()
    
            
if __name__ == "__main__":
    main()
