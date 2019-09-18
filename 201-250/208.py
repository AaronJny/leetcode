class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def __repr__(self):
        return '<Trie(children={})>'.format(self.children)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ch = word[0]
        trie, cnt = self.children.get(ch, (None, 0))
        if trie:
            self.children[ch][1] = cnt + 1
        else:
            trie = Trie()
            self.children[ch] = [trie, 1]
        if word[1:]:
            trie.insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ch = word[0]
        trie, cnt = self.children.get(ch, (None, 0))
        if trie:
            if word[1:]:
                return trie.search(word[1:])
            else:
                _sum = sum([_cnt for _ch, (_trie, _cnt) in trie.children.items()])
                if cnt > _sum:
                    return True
                else:
                    return False
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ch = prefix[0]
        trie, cnt = self.children.get(ch, (None, 0))
        if trie:
            if prefix[1:]:
                return trie.startsWith(prefix[1:])
            else:
                return True
        else:
            return False