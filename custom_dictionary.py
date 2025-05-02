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
    def _dfs(self, node: TrieNode, prefix: str, results: List[str]):
        if node.is_end_of_word:
            results.append(prefix)

        for char, next_node in node.children.items():
            self._dfs(next_node, prefix + char, results)

    def auto_complete(self, prefix: str) -> List[str]:
        with self.lock:
            node = self.root
            for char in prefix:
                if char not in node.children:
                    return []
                node = node.children[char]

            results = []
            self._dfs(node, prefix, results)
            return results