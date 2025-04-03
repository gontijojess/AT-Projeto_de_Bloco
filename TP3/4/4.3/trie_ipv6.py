class IPv6TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix = None

class IPv6Trie:
    def __init__(self):
        self.root = IPv6TrieNode()

    def ipv6_to_binary(self, ipv6_address):
        if '/' in ipv6_address:
            ipv6_address = ipv6_address.split('/')[0]

        hextets = ipv6_address.split(':')
        if '' in hextets:
            empty_index = hextets.index('')
            hextets[empty_index:empty_index+1] = ['0000'] * (8 - len(hextets) + 1)

        hextets = [h.zfill(4) for h in hextets]
        full_ipv6 = ''.join(hextets)

        binary_str = ''.join(f'{int(c, 16):04b}' for c in full_ipv6)
        return binary_str

    def insert(self, prefix):
        ipv6_address, prefix_length = prefix.split('/')
        prefix_length = int(prefix_length)
        binary_str = self.ipv6_to_binary(ipv6_address)[:prefix_length]

        node = self.root
        for bit in binary_str:
            if bit not in node.children:
                node.children[bit] = IPv6TrieNode()
            node = node.children[bit]
        node.prefix = prefix

    def search_longest_prefix(self, ipv6_address):
        binary_str = self.ipv6_to_binary(ipv6_address)
        node = self.root
        longest_prefix = None

        for bit in binary_str:
            if bit not in node.children:
                break
            node = node.children[bit]
            if node.prefix:
                longest_prefix = node.prefix

        return longest_prefix

trie = IPv6Trie()
trie.insert("2001:db8::/32")
trie.insert("2001:db8:1234::/48")
trie.insert("2001:db8:5678::/48")
trie.insert("2001:db8:abcd::/48")

ip_to_search = "2001:db8:1234:5678::1"
result = trie.search_longest_prefix(ip_to_search)
print(f"O prefixo mais longo para {ip_to_search} é: {result}")