## queryusergists.py
queryusergists.py is a python script to query a Github user's gists

## Syntax
`queryusergists.py <username>`, Where `<username>` is the Github user's username.

On query a user's gists, queryusergists will register the current gists for that user and show the date of the latest gist. 
The user will be registered in a file named "/tmp/queryusergists.<username>".
Subsequent executions for the same username will tell you if a new gist has been added by the user. 

## Requirements / Pre-Requisites
* Python 2.7 or higher
* To update, latest version of pip run: python.exe -m pip install --upgrade pip
* To import built in module requests as part of python script, first install OSX/Linux, if not already installed.
* pip install requests


## Exit codes
* Resource(user) not found: 404
* Issues with SSH connection : 255
* User has not published any gists: 1
* Success (first or subsequent queries): 0

## License
GNU General Public License v3.0

## Miscellaneous
To reset all queries, delete `/tmp/queryusergists.*`
To reset an individual query, delete `/tmp/queryusergists.<username>`.

