from custom_dictionary import CustomDictionary

def main():
    dictionary = CustomDictionary()
    
    print("\n=== Custom Dictionary CLI ===")
    print("Commands: \n| add <word> \n| search <word> \n| autocomplete <word> \n| remove <word> \n| save <filename> \n| load <filename> \n| exit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip().lower()

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
                
                case 'remove':
                    if validate_input(parts, command):
                        word = parts[1]
                        success = dictionary.remove_word(word)
                        if success:
                            print(f"🗑️ Successfully removed '{word}'.")
                        else:
                            print(f"⚠️ Word '{word}' not found to remove.")

                case 'save':
                    if validate_input(parts, command):
                        filename = parts[1]
                        dictionary.save_to_file(filename)
                        print(f"💾 Dictionary saved to '{filename}'.")
                
                case 'load':
                    if validate_input(parts, command):
                        filename = parts[1]
                        dictionary.load_from_file(filename)
                        print(f"📂 Dictionary loaded from '{filename}'.")

                case _:
                    print("⚠️ Invalid command.")

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