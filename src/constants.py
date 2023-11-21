VERSION: str = "0.1.1"
HELP_PAGE_CONTENT: str = """NodeJS Auto Update

Usage: nodejs_update.sh [version] <options>
Options for version: [latest | version]

<options>
    --overwrite-node This will overwrite your node executable. By default, NodeJS-Update creates a new NodeJS executable under the exec PATH name nodejs.
    --force Disables checks and forces installation

node_update.sh <command>

<commands>
    --help Displays the help documentation
    --version Displays the version of NodeJS-Update
"""
