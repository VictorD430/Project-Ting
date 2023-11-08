from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    data_input = [
        {"data": "test1.txt", "qtd_linhas": 9},
        {"data": "test2.txt", "qtd_linhas": 4},
        {"data": "test3.txt", "qtd_linhas": 2},
        {"data": "test4.txt", "qtd_linhas": 5},
        {"data": "test5.txt", "qtd_linhas": 7},
        {"data": "test6.txt", "qtd_linhas": 11},
        {"data": "test7.txt", "qtd_linhas": 3},
    ]
    data_output = [
        {"data": "test2.txt", "qtd_linhas": 4},
        {"data": "test3.txt", "qtd_linhas": 2},
        {"data": "test7.txt", "qtd_linhas": 3},
        {"data": "test1.txt", "qtd_linhas": 9},
        {"data": "test4.txt", "qtd_linhas": 5},
        {"data": "test5.txt", "qtd_linhas": 7},
        {"data": "test6.txt", "qtd_linhas": 11},
    ]

    queue_in_priority = PriorityQueue()
    count = 0
    for data in data_input:
        assert queue_in_priority.enqueue(data) is None
        count += 1
        assert len(queue_in_priority) == count
    assert queue_in_priority.search(0) == data_output[0]
    with pytest.raises(IndexError):
        queue_in_priority.search(100)
    for index in range(len(data_output)):
        assert queue_in_priority.dequeue() == data_output[index]
        assert len(queue_in_priority) == len(data_output) - index - 1
