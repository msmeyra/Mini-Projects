
def bank(words, letter):
    if words == "hello" or words == "Hello":
        return "$0"
    elif letter == "h" or letter == "H":
        return "$20"
    else:
        return "$100"

def main():
    greetings = input("Greeting: ")
    h_string = (greetings[0])

    print(bank(greetings, h_string))

main()