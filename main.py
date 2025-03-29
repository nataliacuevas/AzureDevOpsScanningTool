import argparse
from dateutil import parser
from ADOuser import ADOuser
from ADOproject import ADOproject
from ADOrequester import ADOrequester
from ADOgroup import ADOgroup

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

    #requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    #projects = requester.getProjectsList()
    #for project in projects:
    #   print(project)
    #   print(80 * "*")
    # response1 : dict = requester.GETallProjectsWithinOrg()

    requester = ADOrequester(argsDict["patToken"], argsDict["Org"])
    """ 
    users = requester.getUserList()
    for user in users:
        print(user)
        print(80 * "*")

    groups = requester.getGroupList()
    for group in groups:
        print(group.principalName)
        members = requester.getGroupMembers(group)
        if len(members) == 0:
            print('#  No Members')
        for member in members:
            print(f"#  {member.displayName}")
        print(80 * "*")
    
    """

    descriptor = "vssgp.Uy0xLTktMTU1MTM3NDI0NS0yMDE1NjUxODU0LTM4MzE5MDQ4NDEtMzE1MDQ4MzU0NS0xMjk1OTE5NDY3LTAtMC0wLTAtMw"
    group : ADOgroup = requester.lookupDescriptors([descriptor])[0]
    print(group)
    nestedMembers : list[ADOuser] = requester.getNestedUserMembersofGroup(group)
    for member in nestedMembers:
        print(member)

   # response1 = requester.GETlistOfUsersInOrg()
   # print(response1)

    # request(argsDict["Org"], argsDict["patToken"])
    # request2(argsDict["Org"], argsDict["patToken"])
    # request4(argsDict["Org"], argsDict["patToken"])

if __name__ == "__main__":
    main()
