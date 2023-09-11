#!/usr/bin/python3

class MyList(list):
    """
    Custom list class that inherits from list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage:
if __name__ == "__main__":
    my_list = MyList([3, 1, 2, 5, 4])
    my_list.print_sorted()
