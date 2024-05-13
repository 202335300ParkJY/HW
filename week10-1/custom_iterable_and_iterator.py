class DsIterable: # Iterable 동시에 Iterator.
    
    def __init__(self, src_seq):
        self.src = src_seq
        self._current = 0
        
    def __iter__(self): # Iterable
        return self # 자신에 대한 Iterator객체 반환
    
    def __next__(self): # Iterator
        current = self._current
        self._current = self._current + 1
        if self._current > len(self.src):
            raise StopIteration
        return self.src[current]