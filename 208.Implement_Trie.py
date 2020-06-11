class TrieNode:
    def __init__(self, letter):
        self.val = letter
        self.children = {}

    def addChild(self, node):
        self.children[node.val] = node


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        remain = word
        try:
            # If a node with matching initial letter exists...
            current = self.root[remain[0]]
            remain = remain[1:]
            for i in range(len(remain)):
                try:
                    current = current.children[remain[i]]
                except:
                    newNode = TrieNode(remain[i])
                    current.addChild(newNode)
                    current = newNode
            current.children["$"] = True

        except:
            # If a node with matching initial letter does not exist...
            # Add all the letters without checking matching children
            current = TrieNode(remain[0])
            self.root[remain[0]] = current
            remain = remain[1:]
            for i in range(len(remain)):
                newNode = TrieNode(remain[i])
                current.addChild(newNode)
                current = newNode
            current.children["$"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        try:
            current = self.root[word[0]]
            word = word[1:]
            for i in range(len(word)):
                try:
                    current = current.children[word[i]]
                except:
                    return False
            try:
                if current.children["$"]:
                    return True
            except:
                return False
        except:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        word = prefix
        # if not prefix
        try:
            current = self.root[word[0]]
            word = word[1:]
            for i in range(len(word)):
                try:
                    current = current.children[word[i]]
                except:
                    return False

            return True
        except:
            return False


if __name__ == "__main__":

    t = Trie()
    word = "apple"
    t.insert(word)
    word2 = "applepie"
    t.insert(word2)
    print(t.startsWith("applepie"))
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
