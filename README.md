# NodeJS Update

This originally started off as a project to automatically update nodejs, but has since turned into an alternative to NVM after how much of a pain NVM was to work with.
  
---
  
**Usage:**  
`$ python3 ./nodejs_update.py (version) [Optional Flags]`  
Options for version: {latest, version number}  
  
Optional CLA Flags:  
`--overwrite-node` Overwrites `node` in path instead of using `nodejs`  
`--force` Disables checks and forces installation. **use with caution**.  
  
---
**To use NodeJS executable**
By default, NodeJS-Update creates a new executable in _PATH_ named `nodejs` which is automatically updated. To automatically update the `node` executable in _PATH_, use the `--overwrite-node` CLA flag.  
Find nodeJS version  
`$ nodejs --version`  
  
To run a file called index.js with nodejs  
`$ nodejs ./index.js`
