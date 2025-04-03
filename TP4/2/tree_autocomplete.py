class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[depth]
            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete(self.root, word, 0)

    def list_words(self):
        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        words = []
        stack = [(node, prefix)]
        while stack:
            current_node, current_prefix = stack.pop()
            if current_node.is_end_of_word:
                words.append(current_prefix)
            for char, child in current_node.children.items():
                stack.append((child, current_prefix + char))
        return words

trie = Trie()
palavras = ["sol", "solar", "sola", "sou"]

print("Exercício 2.1 – Inserção de palavras:")
for palavra in palavras:
    trie.insert(palavra)
print("Palavras na Trie:", trie.list_words())
print()

print("Exercício 2.2 – Busca simples:")
print("Busca por 'sol':", trie.search("sol"))
print("Busca por 'solar':", trie.search("solar"))
print("Busca de 'solzinho':", trie.search("solzinho"))
print()

print("Exercício 2.3 – Autocomplete básico:")
print("Autocomplete de 'so':", trie.autocomplete("so"))
print("Autocomplete de 'sol':", trie.autocomplete("sol"))
print("Autocomplete de 'sola':", trie.autocomplete("sola"))
print()

print("Exercício 2.4 – Remoção de uma palavra:")
trie.delete("sol")
print("Palavras na Trie após remover 'sol':", trie.list_words())
print("Busca de 'solar':", trie.search("solar"))
print("Busca de 'sola':", trie.search("sola"))