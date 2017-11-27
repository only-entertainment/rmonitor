import cmd
import sys

from rmonitor.client.client import Client
from rmonitor.settings.settings import logger


def run():
    try:
        Client.connect()
    except KeyboardInterrupt:
            pass


class RMonitorShell(cmd.Cmd):

    intro = 'Welcome to the RMonitor shell. Type help or ? to list commands.\n'
    prompt = '>> '

    def do_q(self, arg):
        'Exit the system'
        exit()

    def do_exit(self, arg):
        'Exit the system'
        exit()

    def do_run(self, arg):
        'Run and receive messages'
        logger.info("Running and monitoring...")
        run()


if __name__ == '__main__':
    #
    # Main Driver
    #

    logger.debug(str(sys.argv))
    args = sys.argv

    if len(args) > 1:
        # Get rid of the script name
        args.pop(0)

        # Get the first arg (run, shell)
        ccc = args[0]

        if ccc == 'run':
            RMonitorShell().do_run(None)

        elif ccc == 'shell':
            RMonitorShell().cmdloop()
        else:
            # Default
            RMonitorShell().cmdloop()

    elif len(args) == 1:
        # Fully interactive mode
        RMonitorShell().cmdloop()
