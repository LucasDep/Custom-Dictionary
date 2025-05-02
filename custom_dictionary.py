import threading

class TrieNode:
    def __init__(self):
        # Maps characters to TrieNode children
        self.children = {}
        # True only if this node completes a valid word
        self.is_end_of_word = False     

class CustomDictionary:
    def __init__(self):
        self.root = TrieNode()
        # RLock for recursive thread-safe operations
        self.lock = threading.RLock()

    def add_word(self, word: str):
        with self.lock:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

            node.is_end_of_word = True

    def search_word(self, word: str) -> bool:
        with self.lock:
            node = self.root
            for char in word:
                if char not in node.children:
                    return False
                node = node.children[char]

            return node.is_end_of_word