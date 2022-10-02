from os.path import exists

# this is called when the user adds the --help flag
# or does not call with a valid version
def printHelp():
    helpPage = """
    Help page for Python Auto Update (PAU)

    Usage: python3 ./nodejs_update.py [version] [optional flags]
    Options for version: latest
                         [version number]
    
    Optional Flags (after [version]):
        --overwrite-node
        This will overwrite your node execuatable. By default, NodeJS-Update creates a new NodeJS executable under the exec PATH name nodejs.
        This will flag will instead replace node in your PATH. Use with caution.
    """

    print(helpPage)
    exit

def printError(message = "", fatal = True):
    if message == "":
        message = "An unknown error occured..."


    print(f"{'Fatal ' if fatal else ''}Error!")
    print(message)
    exit

def fileExists(filepath):
    if filepath == None or filepath == "":
        printError("Please provide a valid file path.")
    return exists(filepath)