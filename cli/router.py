import sys
from cli.commands import CommandHandler

def run():
    args = sys.argv[1:]

    if not args:
        print("Gunakan perintah. Contoh: item create")
        return

    command = args[0]
    subcommand = args[1] if len(args) > 1 else None

    handler = CommandHandler()

    handler.handle(command, subcommand, args[2:])