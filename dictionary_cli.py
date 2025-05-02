from custom_dictionary import CustomDictionary

def main():
    dictionary = CustomDictionary()
    
    print("\n=== Custom Dictionary CLI ===")
    print("Commands: add <word> | search <word> | autocomplete <word> | exit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip()

            if not command:
                continue
            
            parts = command.split()

            cmd = parts[0].lower()

            match cmd:
                case 'exit':
                    print("Goodbye!")
                    break

                case 'add':
                    if validate_input(parts, command):
                        word = parts[1]
                        dictionary.add_word(word)
                        print(f"✅ Added word '{word}'.")
                
                case 'search':
                    if validate_input(parts, command):
                        word = parts[1]
                        found = dictionary.search_word(word)
                        print(f"🔍 Word '{word}' found: {found}")
                
                case 'autocomplete':
                    if validate_input(parts, command):
                        prefix = parts[1]
                        suggestions = dictionary.auto_complete(prefix)
                        print(f"📚 Suggestions for '{prefix}': {suggestions}")

                case _:
                    print("⚠️ Invalid command or wrong number of arguments.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        
        except Exception as e:
            print(f"❌ Error: {e}")

def validate_input(parts, command):
    if len(parts) == 2:
        return True
    else:
        print(f"⚠️ Word needed for the '{command}' command.")

if __name__ == "__main__":
    main()