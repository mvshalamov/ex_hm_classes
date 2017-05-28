import pytest

from ex_hm_classes.hw.ex3 import Work, TODOList


def test_work():
	w = Work(1, 2)

	assert w.name == 1
	assert w.description == 2


def test_todolist():
	todo = TODOList()

	w1 = Work("name1", "desc1")
	w2 = Work("name2", "desc2")
	w3 = Work("name3", "desc3")
	w4 = Work("name4", "desc4")
	w5 = Work("name5", "desc5")
	w6 = Work("name6", "desc6")

	todo.add(w1)
	todo.add(w2)
	todo.add(w3)
	todo.add(w4)
	todo.add(w5)
	todo.add(w6)

	assert 6 == todo.count()
	assert todo.todo_list == todo._todo_list

	w_new = todo.del_work(4)
	assert w_new.name == w_new.name
	assert 5 == todo.count()

	todo.rearrange_work(0, 2)
	todo.get_work(0).name == "name3"
	todo.get_work(2).name == "name1"

	assert w2.name == todo.get_work(1).name
