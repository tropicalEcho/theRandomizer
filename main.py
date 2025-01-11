import random, os, sys

helpText = """
COMMANDS:
<ITEM IN THE JAR>   - Add items to the jar.
CLEAR | CLS         - Clear the screen.
HELP | H            - Show this help text.
EXIT | QUIT         - Exit the program.
DONE                - Pick items from the jar.
  -T | --TIME <TIME>   - Adds a delay (in seconds) between picks.
  -C | --COUNT <COUNT> - Specifies how many items to pick.
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def confirmation(userInput, purpose, message="ARE YOU SURE? (Y | N) "):
    while True:
        choice = input(message).strip().upper()
        if choice in ["Y", "YES"]:
            if purpose == "KILL":
                sys.exit("GOODBYE!")
            elif purpose == "DUPLICATE":
                jar.append(userInput)
            break
        elif choice in ["N", "NO"]:
            break
        else:
            print("?!")

def pickSome(jar, howMany=1, delay=0):
    selected = []
    while len(selected) < howMany and jar:
        unfaithful = random.choice(jar)
        jar.remove(unfaithful)
        selected.append(unfaithful)
        if delay > 0:
            print(f"REMOVED: {unfaithful}")
            time.sleep(delay)
    if selected:
        print(f"FINAL CHOICE{'S' if len(selected) > 1 else ''}: {', '.join(map(str, selected))}")
    else:
        print("JAR IS VOID!")
    jar.clear()

def main():
    global jar
    jar = []
    clear()
    while True:
        userInput = input("~theOracle$ ").strip()
        if not userInput:
            continue
        command = userInput.split()[0].upper()
        
        if command in ["CLEAR", "CLS"]:
            clear()
        elif command in ["HELP", "H"]:
            print(helpText)
        elif command in ["EXIT", "QUIT"]:
            if not jar: 
                sys.exit("GOODBYE!")
            confirmation(None, "KILL", "THE JAR IS NOT VOID... QUIT ANYWAYS? (Y | N) ")
        elif command == "DONE":
            args = userInput.split()[1:]
            time_delay = 0
            count = 1
            i = 0

            while i < len(args):
                if args[i] in ["-T", "--TIME"] and i + 1 < len(args):
                    try:
                        time_delay = float(args[i + 1])
                        i += 2
                    except ValueError:
                        print("ERROR: TIME MUST BE A POSITVE NUMBER!")
                        break
                elif args[i] in ["-C", "--COUNT"] and i + 1 < len(args):
                    try:
                        count = int(args[i + 1])
                        i += 2
                    except ValueError:
                        print("ERROR: COUNT MUST BE A POSTIVE INTEGER!")
                        break
                else:
                    print(f"ERROR: UNKNOWN OPTION '{args[i].upper()}'")
                    break
            
            pickSome(jar, howMany=count, delay=time_delay)
        else:
            if userInput in jar:
                confirmation(userInput, "DUPLICATE", f"'{userInput}' IS ALREADY IN THE JAR! ADD 'EM ANYWAYS? (Y | N) ")
            elif userInput:
                jar.append(userInput)

if __name__ == "__main__":
    main()
