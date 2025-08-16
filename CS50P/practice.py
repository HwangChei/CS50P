class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0  # current number of cookies

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Exceeds jar capacity")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdraw amount must be a non-negative integer")
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

# Testing code (not required by CS50 but useful for your understanding)
if __name__ == "__main__":
    jar = Jar()
    print("Capacity:", jar.capacity)
    print("Size:", jar.size)

    put = int(input("Deposit: "))
    jar.deposit(put)

    out = int(input("Withdraw: "))
    jar.withdraw(out)

    print(jar)


import sys
class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError
        if self._size + n > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError
        if n > self._size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    print("Capacity:", jar.capacity)
    print("Size:", jar.size)

    put = int(input("Deposit: "))
    jar.deposit(put)

    out = int(input("Withdraw: "))
    jar.withdraw(out)

    print(jar)
if __name__ == "__main__":
    main()


