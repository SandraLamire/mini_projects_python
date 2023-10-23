def hello(name, lang):
    greetings = {
        "English": "Hello",
        "French": "Bonjour",
        "Spanish": "Hola"
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)
 

# # command-line option and argument parsing library
# import argparse

# parser = argparse.ArgumentParser(
#     description="Provides a personal greeting"
# )

# parser.add_argument(
#     "-n", "--name", metavar="name", required=True, help="The name of the person to greet."
# )

# args = parser.parse_args()

# msg = f"Hello {args.name}!"
# print(msg)
# # error: the following arguments are required: -n/--name
# # py LESSON15_command_line_arguments.py -h
# # usage: LESSON15_command_line_arguments.py [-h] -n name  
# # Provides a personal greeting
# # options:
# #   -h, --help            show this help message and exit 
# #   -n name, --name name  The name of the person to greet.
# # because an argument is missing

# # We must launch :
# # py LESSON15_command_line_arguments.py -n "Sandra"
# # Hello Sandra!


######################################################################################

# launch with : py LESSON15_command_line_arguments.py -n "Sandra" -l "French"

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(
    description="Provides a personal greeting"
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="The name of the person to greet."
    )
    
    parser.add_argument(
        "-l", "--lang", metavar="language", choices=["English", "French", "Spanish"], required=True, help="The language of the person to greet."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)
    

