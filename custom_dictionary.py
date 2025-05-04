import threading
from typing import List

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
        
    #Depth-First Search    
    def _dfs(self, node, path, results):
        if node.is_end_of_word:
            results.append("".join(path))
        for char, child in node.children.items():
            self._dfs(child, path + [char], results)

    def auto_complete(self, prefix: str) -> List[str]:
        with self.lock:
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return []   # Prefix not found
                node = node.children[char]

            results = []
            self._dfs(node, list(prefix), results)
            return results
    
    def remove_word(self, word: str) -> bool:
        """Removes a word from the Trie. Returns True if removed, False if not found."""
        with self.lock:
            self._was_removed = False
            self._remove_word_helper(self.root, word, 0)
            return self._was_removed

    def _remove_word_helper(self, node, word, index):
        """
        Recursively removes a word from the Trie.
        Returns True if the current node can be safely deleted.
        """
        # Base case: reached end of word
        if index == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            self._was_removed = True
            # If node has no children, tell the parent it's safe to delete this node
            return len(node.children) == 0

        # Get the current character in the word
        char = word[index]
        child = node.children.get(char)
        # If word not in dictionary
        if not child:
            return False 

        # Recurse to the next character
        should_delete_child = self._remove_word_helper(child, word, index + 1)

        if should_delete_child:
            del node.children[char] # Clean up unused node

        # Let parent know whether *this* node is deletable:
        # Only if it's not the end of another word AND it has no children
        return not node.is_end_of_word and len(node.children) == 0

    def _collect_all_words(self) -> list[str]:
        results = []
        self._dfs(self.root, [], results)
        return results

    def save_to_file(self, filename: str):
        with self.lock:
            # Get all words
            words = self._collect_all_words()
            with open(filename, 'w') as f:
                for word in words:
                    f.write(f"{word}\n")

    def load_from_file(self, filename: str):
        with self.lock:
            with open(filename, 'r') as f:
                for line in f:
                    word = line.strip()
                    if word:
                        self.add_word(word)
