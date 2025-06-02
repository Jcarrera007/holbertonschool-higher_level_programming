class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        return self.count

# Example usage:
if __name__ == "__main__":
    items = [10, 20, 30]
    ci = CountedIterator(items)
    for value in ci:
        print(value)
    print("Items iterated:", ci.get_count())
