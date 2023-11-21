from os.path import exists
from typing import NoReturn
from constants import HELP_PAGE_CONTENT, VERSION


def printHelp() -> NoReturn:
    print(HELP_PAGE_CONTENT)
    exit(0)


def printVersion() -> NoReturn:
    print(VERSION)
    exit(0)

def fileExists(filepath: str) -> bool:
    if filepath == None or filepath == "":
        raise Exception("Please provide a valid file path for fileExists().")
    return exists(filepath)


def readFile(fileName: str) -> list[str]:
    if fileName == None or fileName == "":
        raise Exception("Please provide a valid file path for readFile().")

    with open("README.md") as file:
        return file.readlines()
