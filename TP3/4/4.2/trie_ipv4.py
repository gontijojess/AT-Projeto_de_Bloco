class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix = None

class IPv4Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefixo):
        node = self.root
        partes = prefixo.split("/")
        prefixo_ip = partes[0]
        prefixo_mask = int(partes[1])
        
        bin_ip = ''.join(f'{int(octeto):08b}' for octeto in prefixo_ip.split('.'))[:prefixo_mask]
        
        for bit in bin_ip:
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]
        
        node.prefix = prefixo

    def longest_prefix_match(self, ip):
        node = self.root
        bin_ip = ''.join(f'{int(octeto):08b}' for octeto in ip.split('.'))
        
        prefixo_encontrado = None
        for bit in bin_ip:
            if bit in node.children:
                node = node.children[bit]
                if node.prefix:
                    prefixo_encontrado = node.prefix
            else:
                break
        
        return prefixo_encontrado

trie = IPv4Trie()
trie.insert("192.168.0.0/16")
trie.insert("192.168.1.0/24")
trie.insert("10.0.0.0/8")

ip_testado = "192.168.1.100"
prefixo_correspondente = trie.longest_prefix_match(ip_testado)
print(f"O prefixo mais longo correspondente ao IP {ip_testado} é: {prefixo_correspondente}")