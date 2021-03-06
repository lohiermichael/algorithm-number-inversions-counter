import random


class InputList(list):
    def __init__(self, l_length: int = 100, min_value: int = 0, max_value: int = 10000, is_distinct: bool = True):
        """
        Object of input list for algorithms
        Parameters
        ----------
        l_length (int): Length of the input list
        min_value (int): Minimal value of the elements of the list
        max_value (int): Maximal value of the elements of the list
        is_distinct (bool): distinct elements in the list
        """
        self.l_length = l_length
        self.min_value = min_value
        self.max_value = max_value
        self.is_distinct = is_distinct
        self._construct()

    def _find_element_not_in_set(self, already_used: set) -> int:
        """
        This function returns an element not present in a set
        Parameters
        ----------
        already_used (set): a set of int

        Returns
        -------
        int: int not in set
        """
        new_element = random.randint(a=self.min_value, b=self.max_value)
        while new_element in already_used:
            new_element = random.randint(a=self.min_value, b=self.max_value)
        return new_element

    def _construct(self):
        """
        This function will build the object
        Returns
        -------
        list
        """
        if self.is_distinct:
            assert self.l_length <= self.max_value - self.min_value + 1, "The range of values chosen " \
                                                                         "doesn't allow to have distinct values"
            already_used = set()
            for index in range(self.l_length):
                # Find an element not present in already_used
                new_element = self._find_element_not_in_set(already_used)
                # Add the element to already used
                already_used.add(new_element)
                # Add the element to the list
                self.append(new_element)
        else:
            for index in range(self.l_length):
                self.append(random.randint(a=self.min_value, b=self.max_value))
