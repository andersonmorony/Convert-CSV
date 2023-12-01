
import pytest
import pandas as pd
import sys
import os
import pytest

# Adicione o caminho para o diretório que contém o módulo Services ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Services.funcs import Funcs


def test_order_column():
    funtions = Funcs()
    df = pd.DataFrame({'A': [9,1,4,5,68,6,23,2]})
    data_sorted = funtions.orderBy(df, 'A')

    assert data_sorted.iloc[0]['A'] == 1
    assert data_sorted.iloc[1]['A'] == 2
    assert data_sorted.iloc[2]['A'] == 4
    assert data_sorted.iloc[3]['A'] == 5
    assert data_sorted.iloc[7]['A'] == 68

def test_order_column_desc():
    funtions = Funcs()
    df = pd.DataFrame({'A': [9,1,4,5,68,6,23,2]})
    data_sorted = funtions.orderBy(df, 'A', False)

    assert data_sorted.iloc[0]['A'] == 68
    assert data_sorted.iloc[1]['A'] == 23
    assert data_sorted.iloc[2]['A'] == 9
    assert data_sorted.iloc[7]['A'] == 1
    
def test_should_return_msg_error_order_column():
    a = Funcs()
    df = pd.DataFrame({'A': [9,1,4,5,68,6,23,2]})
    data_sorted = a.orderBy(df, 'Invalid_Column')

    assert data_sorted == "Key not found"

def test_should_return_value():
    funcs = Funcs()
    expected = "fake_file.csv"
    filename = "c://fakepath/fake/fake_file.csv"
    res = funcs.split_string_name(filename, '/')
    assert res == expected

pytest.main(["-v", "--tb=line", "-rN", __file__])