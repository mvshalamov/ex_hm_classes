class Work:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):  # pragma: no cover
        return "Дело - {} \nОписание - {}".format(self.name, self.description)


class TODOList:
    def __init__(self):
        self._todo_list = []

    def add(self, work):
        self._todo_list.append(work)

    def get_work(self, position):
        """
        :param position: порядковый номер в списке
        :return: элемент
        """
        return self._todo_list[position]

    @property
    def todo_list(self):
        """
        :return: список всех дел
        """
        return self._todo_list

    def del_work(self, position):
        """
        извлекаеи элемент с номером position
        """
        return self._todo_list.pop(position)

    def rearrange_work(self, cur_pos, target_pos):
        """
        меняем дела местами
        """
        self._todo_list[cur_pos], self._todo_list[target_pos] = self._todo_list[target_pos], self._todo_list[cur_pos]

    def count(self):
        """
        :return: колличество дел
        """
        return len(self._todo_list)

    def __str__(self):  # pragma: no cover
        return "В списке %s дел" % len(self.todo_list)
