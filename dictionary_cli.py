from custom_dictionary import CustomDictionary

def main():
    dictionary = CustomDictionary()
    
    print("\n=== Custom Dictionary CLI ===")
    print("Commands: add <word> | search <word> | exit")
    
    while True:
        try:
            command = input("\nEnter command: ").strip()

            if not command:
                continue #TODO verify functionality
            
            parts = command.split()
            if len(parts) == 0:
                continue #TODO verify functionality

            cmd = parts[0].lower()

            match cmd:
                case 'exit':
                    print("Goodbye!")
                    break

                case 'add':
                    if len(parts) == 2:
                        word = parts[1]
                        dictionary.add_word(word)
                        print(f"✅ Added word '{word}'.")
                    else:
                        print("⚠️ Word needed for the 'add' command.")
                
                case 'search':
                    if len(parts) == 2:
                        word = parts[1]
                        found = dictionary.search_word(word)
                        print(f"🔍 Word '{word}' found: {found}")
                    else:
                        print("⚠️ Word needed for the 'search' command.")

                case _:
                    print("⚠️ Invalid command or wrong number of arguments.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()