import hashlib
import timeit
import plotly.express as px
import random
import string


class HashFunctions:

    def __init__(self) -> None:
        pass

    def hash_text(self, text: str) -> None:
        for algorithm in hashlib.algorithms_available:
            hash_v = hashlib.new(algorithm)
            hash_v.update(text.encode('utf-8'))
            timer = timeit.timeit(lambda: hashlib.new(algorithm, text.encode("UTF-8")))
            if algorithm == 'shake_128' or algorithm == 'shake_256':
                print(f'{algorithm}: {hash_v.hexdigest(32)} time: {timer:.2f}')
                continue
            print(f'{algorithm}: {hash_v.hexdigest()} time: {timer:.2f}')

    def hash_file(self, path: str) -> str:
        hash_sha = hashlib.sha256()
        with open(path, 'rb') as file:
            file_block = file.read(hash_sha.block_size)
            while len(file_block) > 0:
                hash_sha.update(file_block)
                file_block = file.read(hash_sha.block_size)
        return hash_sha.hexdigest()

    def charts_for_hashed_strings_different_length(self) -> None:
        obj = {
            'length': [],
            'time': []
        }
        for i in range(10, 20):
            letters = string.ascii_lowercase
            text = ''.join(random.choices(letters + string.digits, k=i))
            obj['length'].append(len(text))
            obj['time'].append(timeit.timeit('lambda: hashlib.new(\'sha256\', text.encode("UTF-8"))'))
        chart = px.line(obj, x='length', y='time')
        chart.show()


hash_t = HashFunctions()
# hash_t.hash_text("abcdefgh")
# print(hash_t.hash_file('test.txt'))
hash_t.charts_for_hashed_strings_different_length()
