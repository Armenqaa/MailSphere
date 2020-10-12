def find_index(list_of_list, our_key):
    """Функция находит индекс по ключу"""
    for index, item in enumerate(list_of_list):
        if list_of_list[index][0] == our_key:
            return index


class ICache:

    def __init__(self, capacity: int = 10) -> None:
        self.cache_queue = []
        self.max_cache_size = capacity
        self.current_cache_size = 0
        self.queue_first_item = 0

    def get(self, key: str) -> str:
        """Значение по ключу"""
        try:
            return self.cache_queue[find_index(self.cache_queue, key)][1]
        except TypeError:
            print('Такого ключа не существует')

    def set(self, key: str, value: str) -> None:
        """Создание новой пары ключ:значение"""
        if self.current_cache_size == self.max_cache_size:
            self.delete(0)
        self.current_cache_size += 1
        self.cache_queue.append([key, value])

    def delete(self, key: int) -> None:
        """Удаление элемента из кэша"""
        self.current_cache_size -= 1
        try:
            self.cache_queue.pop(key)
        except TypeError:
            print('Такого ключа не существует')


if __name__ == '__main__':
    cache = ICache(1)
    cache.set('Jesse', 'Pinkman')
    cache.set('Patrick', 'James')
    print(cache.get('Jesse'))
    print(cache.get('Patrick'))
    print(cache.get('Armen'))
