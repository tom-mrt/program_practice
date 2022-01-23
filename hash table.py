import hashlib

class HashTable():
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]




if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.add("car", "Tesla")
    hash_table.add("car", "Volvo")
    hash_table.add("pc", "mac")
    hash_table.add("sns", "youtube")
    print(hash_table.table)
    print(hash_table.get("car"))
