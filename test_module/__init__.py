#In your module you will have to insert your libraries that you need in the package

def _sch_exec():
    return {
        "cmd": "test", #The command name of the module it does not have to be the same as the modules name
        "cmd_handler": cmd, #The handler that is the function that is called when the command is called in the terminal
        "version": "v1.0"
        }

def cmd(args):
    #The args input is formated like in a list like this "test subcommand -sa --someargument" > ["subcommand","-sa","--someargument"]
    print(args)

