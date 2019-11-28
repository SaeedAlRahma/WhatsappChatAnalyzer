import sys
from contact import Contact

print("----- Script started!")

# Constants
PREFIX = "M - "
SUFFIX = ": "

def printResults(contact_map):
    """
    Print the results for all contacts.

    :param dict contact_map: Dictionary with all participants in the chat
    """
    print("----")
    for participant in contact_map.values():
        print(participant.getName())
        print(participant.getMessageCount())
        print(participant.getWordCount())
        print(participant.avgWords())
        print("----")

def analyze(filename):
    """
    Analyzes the chat file.

    :param filename: name of the chat
    """
    print ("-- analyze() called")

    # Initialize variables
    contact_map = {}
    msg_owner = "None"
    contact = None

    # Open the chat file in read-only
    file = open(filename, 'r')
    try:
        # Read the file
        for line in file:
            # Get new message owner
            if line.find(PREFIX) > -1 and line.find(SUFFIX) > -1:
                # Beginning of a new message
                msg_owner = line[line.find(PREFIX)+len(PREFIX):line.find(SUFFIX)]
                # Add new contact
                if not msg_owner in contact_map:
                    contact_map[msg_owner] = Contact(msg_owner)
                # Update contact
                contact = contact_map[msg_owner]
                contact.incrementMessages()
                # Get message from line
                line = line[line.find(SUFFIX)+len(SUFFIX):]
            if not contact is None:
                # This is a message, increment contact words
                contact.incrementWords(len(line.rsplit(" ")))
    finally:
        # Close the chat file
        file.close()

    printResults(contact_map)

def main():
        """
        Main function that serves as an entrypoint for the program.
        Reads the chat file name from the command line
        when the program is run from the terminal
        and passed it to the `analyse()` method.
        """
        chatfile_name = sys.argv[1]
        analyze(chatfile_name)

if __name__ == "__main__":
    main()
