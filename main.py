import random, os, sys, time

helpText = """
COMMANDS:
<ITEM IN THE JAR>    - ADD ITEMS TO THE JAR
CLEAR | CLS          - CLEARS THE SCREEN
HELP | H             - PRINTS THIS
EXIT | QUIT          - KILLS THE PROGRAM
DONE                 - PICKS ITEM(S) FROM THE JAR
    -T | --TIME <TIME>   - ADDS DELAY (IN SECONDS) BETWEEN REMOVALS
    -C | --COUNT <COUNT> - SPECIFIES HOW MANY ITEMS TO PICK 
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def confirmation(userInput, purpose, message="ARE YOU SURE? (Y | N) "):
    while True:
        if choice := input(message).strip().upper() in ["Y", "YES"]:
            if purpose == "KILL": sys.exit("GOODBYE!")
            if purpose == "DUPLICATE": jar.append(userInput)
            break
        elif choice in ["N", "NO"]:
            break
        else: print("?!")

def pickSome(jar, howMany=1, delay=0):
    selected = []
    while len(selected) < howMany and jar:
        jar.remove(unfaithful := random.choice(jar))
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
        if not (userInput := input("~theOracle$ ").strip()): 
            continue
        if command := userInput.split()[0].upper() in ["CLEAR", "CLS"]:
            clear()
        elif command in ["HELP", "H"]:
            print(helpText)
        elif command in ["EXIT", "QUIT"]:
            if not jar: 
                sys.exit("GOODBYE!")
            confirmation(None, "KILL", "THE JAR IS NOT VOID... QUIT ANYWAYS? (Y | N) ")
        elif command == "DONE":
            args = userInput.split()[1:]
            timeDelay = 0
            count = 1
            i = 0

            while i := 0 < len(args):
                if args[i] in ["-T", "--TIME"] and i + 1 < len(args):
                    try:
                        timeDelay = float(args[i + 1])
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
            
            pickSome(jar, howMany=count, delay=timeDelay)
        else:
            if userInput in jar:
                confirmation(userInput, "DUPLICATE", f"'{userInput}' IS ALREADY IN THE JAR! ADD 'EM ANYWAYS? (Y | N) ")
            elif userInput:
                jar.append(userInput)

if __name__ == "__main__":
    main()
