import sys
import requests
import re
from os import system, remove, popen
from util import fileExists, readFile, printHelp

# if false: nodejs is added to PATH via link
# if True: nodejs is added by adding the direct executable to the PATH
DIRECT_CALLING = False
DISTRIBUTION_URL = "https://nodejs.org/dist/"


# get the most recent NodeJS version from the website
def getLatestNodeVersion():
    r = requests.get("https://nodejs.org/en/download/releases/")
    if r.status_code == 200:
        try:
            siteText = r.text

            # get the most recent version
            matchRE = r'<td data-label="Version">Node.js (.+)</td>'
            nodeVersion = re.search(matchRE, siteText).group(1)

            return nodeVersion
        except:
            raise Exception("Could not parse NodeJS version")
    else:
        raise Exception("Could not parse NodeJS version")


# install the most recent NodeJS version
def installVersion(versionNumber, nodejsPATHExec="nodejs", forceInstall=False):
    currentVersion = popen(f"{nodejsPATHExec} --version").read()[1:].replace("\n", "")

    # check that the requested version does not match the current version
    if currentVersion != versionNumber or forceInstall:
        # remove artifacts from previous installs
        if fileExists(f"/tmp/node-v{versionNumber}-linux-x64.tar.gz"):
            remove(f"/tmp/node-v{versionNumber}-linux-x64.tar.gz")

        # install a new local copy of the requested nodejs executable bundle
        system(
            f"wget {DISTRIBUTION_URL}v{versionNumber}/node-v{versionNumber}-linux-x64.tar.gz -O /tmp/node-v{versionNumber}-linux-x64.tar.gz"
        )

        if not fileExists("/tmp/node-v{versionNumber}-linux-x64.tar.gz"):
            raise Exception(f"Fetching NodeJS from {DISTRIBUTION_URL}")

        system(f"sudo tar -xzf /tmp/node-v{versionNumber}-linux-x64.tar.gz")
        system(f"sudo rm /tmp/node-v{versionNumber}-linux-x64.tar.gz")

        # remove existing node executable version
        if fileExists(f"/usr/bin/{nodejsPATHExec}"):
            system(f"sudo rm /usr/bin/{nodejsPATHExec}")

        if fileExists(f"/opt/{nodejsPATHExec}"):
            system(f"sudo rm -r /opt/{nodejsPATHExec}")

        # nodejs executable will always be in /opt/ directory
        system(f"sudo mv node-v{versionNumber}-linux-x64 /opt/nodejs")

        if not fileExists("/opt/nodejs/bin/node"):
            raise Exception("Copying NodeJS to /opt")

        # copy the downloaded node version to PATH
        if DIRECT_CALLING:
            system(f"sudo cp /opt/nodejs/bin/node /usr/bin/{nodejsPATHExec}")
        else:
            system(f"sudo ln -s /opt/nodejs/bin/node /usr/bin/{nodejsPATHExec}")

        if not fileExists(f"/usr/bin/{nodejsPATHExec}"):
            raise Exception("Creating PATH link")
    else:
        raise Exception("NodeJS is currently up to date")


def main():
    print()

    # CLA argument defaults
    shouldForce = False
    nodejsPathExec = "nodejs"

    if "--help" in sys.argv:
        helpDocs = readFile("README.md")
        for line in helpDocs:
            print(line)
        exit(2)

    # get user specified CLA flags
    if len(sys.argv) == 1:
        printHelp()

    nodejsPathExec = "node" if "--overwrite-node" in sys.argv else "nodejs"
    shouldForce = True if "--force" in sys.argv else False

    if shouldForce:
        print("\033[33;1;4mUsing --force\033[0m\n")

    if sys.argv[1] == "latest":
        nodeVersion = getLatestNodeVersion()
    else:
        nodeVersion = sys.argv[1]

    print(f"Installing NodeJS Version {nodeVersion}")
    installVersion(nodeVersion, nodejsPATHExec=nodejsPathExec, forceInstall=shouldForce)

    print("")
    print("NodeJS installation complete")
    print("Installed as nodejs, check by running")
    print(f"$ {nodejsPathExec} --version")


if __name__ == "__main__":
    main()
