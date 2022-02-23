import random
from Validation import *


class Node:

    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class List:

    def __init__(self):
        self._head = None
        self._size = 0

    def get_size(self):
        return self._size

    def get_head(self):
        return self._head

    def push_back(self, value):
        if self._head is None:
            self._head = Node(value)
        else:
            current = self._head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = Node(value)
        self._size = self._size + 1

    def fill_list_with_keyboard(self, number):
        if self._head is None:
            index = 0
            while index != number:
                element = input_check_list_element_or_interval_limit()
                self.push_back(element)
                index = index + 1
        else:
            current_size = self._size
            while self._size != current_size + number:
                element = input_check_list_element_or_interval_limit()
                self.push_back(element)

    def fill_list_with_randoms(self, number, left, right):
        if self._head is None:
            index = 0
            while index != number:
                element = random.randrange(left, right + 1)
                self.push_back(element)
                index = index + 1
        else:
            current_size = self._size
            while self._size != current_size + number:
                element = random.randrange(left, right + 1)
                self.push_back(element)

    def add_new_node(self, value, index):
        if index == 0:
            new_node = Node(value)
            temp = self._head
            self._head = new_node
            new_node.next_node = temp
        elif index > 0:
            previous = self._head
            for i in range(index - 1):
                previous = previous.next_node
            new_element = Node(value)
            new_element.next_node = previous.next_node
            previous.next_node = new_element
        self._size = self._size + 1

    def delete_node(self, index):
        if self._head is None:
            print("You can't delete node, because your list is empty")
        else:
            if index == 0:
                self._head = self._head.next_node
            elif index > 0:
                previous = self._head
                for i in range(index - 1):
                    previous = previous.next_node
                element_to_delete = previous.next_node
                previous.next_node = element_to_delete.next_node
            self._size = self._size - 1

    def even_and_odd_indexes(self):
        additional_list = List()
        index = 0
        current = self._head
        while current is not None:
            if index % 2 == 0:
                additional_list.push_back(current.value)
            current = current.next_node
            index = index + 1

        index = 0
        current = self._head
        while current is not None:
            if index % 2 == 1:
                additional_list.push_back(current.value)
            current = current.next_node
            index = index + 1
        additional_list.print_list()

    def print_list(self):
        current = self._head
        for i in range(self._size):
            print(current.value, end=' ')
            current = current.next_node
        print()
