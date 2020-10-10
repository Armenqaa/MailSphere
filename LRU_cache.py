def min_priority(cache_dict):
    minimum_priority = 0
    minimum_priority_key = 0
    for key in cache_dict:
        if cache_dict[key][1] <= minimum_priority && cache_dict[key][0] != '':
            minimum_priority = cache_dict[key][1]
            minimum_priority_key = key
    return minimum_priority_key


class ICache:
    def __init__(self, capacity: int = 10) -> None:
        self.cache_dict = {}
        self.max_cache_size = capacity
        self.current_cache_size = 0

    def get(self, key: str) -> str:
        try:
            return self.cache_dict[key][0]
        except KeyError:
            print('Такого ключа не существует')
            return ''

    def set(self, key: str, value: str) -> None:
        if self.current_cache_size == self.max_cache_size:
            print('Кэш заполнен')
        else:
            self.current_cache_size += 1
            self.cache_dict[key] = [value, 0]

    def delete(self, key: str) -> None:
        self.current_cache_size -= 1
        try:
            self.cache_dict[key][0] = ''
        except KeyError:
            print('Такого ключа не существует')
