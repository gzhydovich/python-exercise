## Notes:

* CLI will accept `--username` argument if running operation as a particular user is required. If not provided, tool will get user information by `getpass.getuser()`

* While re-creating a user with `create_user` (delition of the user originally was performed without `--remove` flag), you'll see a warning during the creation process (user will be re-created)

* `list_users` command returnes a table of `USERNAME, ID and NAME/COMMENT` (awk was used for formatting and can be refctored to serve the purpose of the tool)


## Potential improvements:

* `delete_user` function can be improved to accept an optional flag `-r` to remove the user’s home directory and mail spool

* Refactor the authentication piece to accept `username/password` instread of the `.pem` key
 
* To control contributions to the tool, and maintain the workflow without any issues: unit tests to cover ssh_clinet functions