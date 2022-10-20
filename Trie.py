class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.endOfWord = True
        print(f"word inserted to Trie: {word}")

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        if cur.endOfWord:
            print(f"word exists: {word}")
        else:
            print(f"word does not exist: {word}")
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for char in prefix:
            if char not in cur.children:
                print(f"don't have anything that starts with {prefix}")
                return False
            cur = cur.children[char]
        print(f"words starts with {prefix} is: {cur.children.keys()}")

        return True


if __name__ == "__main__":
    init = Trie()
    init.insert("apple")
    init.search("apple")
    init.search("app")
    init.startsWith("app")
    init.insert("app")
    init.search("app")