import pytest
from main import get_doc_owner_name, get_all_doc_owners_names, add_new_shelf, \
    delete_doc, get_doc_shelf, add_new_doc

FIXTURES_get_doc_owner_name = [
    ('2207 876234', 'Василий Гупкин'),
    ('11-2', 'Геннадий Покемонов'),
    ('10006', 'Аристарх Павлов'),
    ('5455 028765', None)]

FIXTURES_add_new_shelf = [
    ('123', ('123', True)),
    ('1234', ('1234', True)),
    ('12345', ('12345', True)),
    ('1', ('1', False))]

FIXTURES_get_doc_shelf = [
    ("2207 876234", "1"),
    ("11-2", "1"),
    ("10006", "2")
]

FIXTURES_delete_doc = [
    ('2207 876234', ('2207 876234', True)),
    ('11-2', ('11-2', True)),
    ('10006', ('10006', True))
]

FIXTURES_add_new_doc = [("123", "passport", "Gleb", "1", ("1", True)),
                        ("1234", "passport", "Vlad", "2", ("2", True))
                        ]


@pytest.mark.parametrize("name, exp_result", FIXTURES_get_doc_owner_name)
def test_get_doc_owner_name(name, exp_result):
    result = get_doc_owner_name(name)
    assert exp_result == result


def test_get_all_doc_owners_names():
    result = get_all_doc_owners_names()
    assert {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'} == result


@pytest.mark.parametrize('number, exp_result', FIXTURES_add_new_shelf)
def test_add_new_shelf(number, exp_result):
    result = add_new_shelf(number)
    assert exp_result == result


@pytest.mark.parametrize("number, exp_result", FIXTURES_get_doc_shelf)
def test_get_doc_shelf(number, exp_result):
    result = get_doc_shelf(number)
    assert exp_result == result


@pytest.mark.parametrize("number, exp_result", FIXTURES_delete_doc)
def test_delete_doc(number, exp_result):
    result = delete_doc(number)
    assert exp_result == result


@pytest.mark.parametrize("new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, exp_result",
                         FIXTURES_add_new_doc)
def test_delete_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number, exp_result):
    result = add_new_doc(new_doc_number, new_doc_type, new_doc_owner_name, new_doc_shelf_number)
    assert exp_result == result
