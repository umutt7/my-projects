class Jar:
    def __init__(self, capacity=12):
        # Initialize a jar with given capacity and zero cookies
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        # Return number of cookies in the jar
        return "🍪" * self.size

    def deposit(self, n):
        # Add given number of cookies to the jar
        # If exceeds capacity, raise error
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        # Substract number of cookies in the jar
        # If exceeds size, raise error
        if n > self.size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        # Getter
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # Setter
        # If capacity is less than 1, raise error
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        # Getter
        return self._size

    @size.setter
    def size(self, size):
        # Setter
        # If size is bigger than capacity, raise error
        if size > self.capacity:
            raise ValueError
        self._size = size


def main():

    jar = Jar()
    print(jar.size)
    jar.deposit(3)
    print(jar.size)
    print(jar)


if __name__ == "__main__":
    main()