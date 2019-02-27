"""
Реализация алгоритма поиска в ширину.
В качестве графа использовано дерево исключений python3.7.2
"""
from collections import deque

graph = dict()
# Корневой элемент
graph['root'] = ['BaseException']
graph['BaseException'] = ['SystemExit', 'KeyboardInterrupt', 'GeneratorExit', 'Exception']

# 1-й уровень
graph['SystemExit'] = []
graph['KeyboardInterrupt'] = []
graph['GeneratorExit'] = []
graph['Exception'] = [
    'StopIteration', 'StopAsyncIteration', 'ArithmeticError', 'AssertionError',
    'AttributeError', 'BufferError', 'EOFError', 'ImportError',
    'LookupError', 'MemoryError', 'NameError', 'OSError',
    'ReferenceError', 'RuntimeError', 'SyntaxError', 'SystemError',
    'TypeError', 'ValueError', 'Warning']

# 2-й уровень
graph['StopIteration'] = []
graph['StopAsyncIteration'] = []
graph['ArithmeticError'] = ['FloatingPointError', 'OverflowError', 'ZeroDivisionError']
graph['AssertionError'] = []
graph['AttributeError'] = []
graph['BufferError'] = []
graph['EOFError'] = []
graph['ImportError'] = ['ModuleNotFoundError']
graph['LookupError'] = ['IndexError', 'KeyError']
graph['MemoryError'] = []
graph['NameError'] = ['UnboundLocalError']
graph['OSError'] = [
    'BlockingIOError', 'ChildProcessError', 'ConnectionError', 'FileExistsError',
    'FileNotFoundError', 'InterruptedError', 'IsADirectoryError', 'NotADirectoryError',
    'PermissionError', 'ProcessLookupError', 'TimeoutError']
graph['ReferenceError'] = []
graph['RuntimeError'] = ['NotImplementedError', 'RecursionError']
graph['SyntaxError'] = ['IndentationError']
graph['SystemError'] = []
graph['TypeError'] = []
graph['ValueError'] = ['UnicodeError']
graph['Warning'] = [
    'DeprecationWarning', 'PendingDeprecationWarning', 'RuntimeWarning', 'SyntaxWarning',
    'UserWarning', 'FutureWarning', 'ImportWarning', 'UnicodeWarning',
    'BytesWarning', 'ResourceWarning']

# 3-й уровень
graph['FloatingPointError'] = []
graph['OverflowError'] = []
graph['ZeroDivisionError'] = []
graph['ModuleNotFoundError'] = []
graph['IndexError'] = []
graph['KeyError'] = []
graph['UnboundLocalError'] = []
graph['BlockingIOError'] = []
graph['ChildProcessError'] = []
graph['ConnectionError'] = ['BrokenPipeError', 'ConnectionAbortedError',
                            'ConnectionRefusedError', 'ConnectionResetError']
graph['FileExistsError'] = []
graph['FileNotFoundError'] = []
graph['InterruptedError'] = []
graph['IsADirectoryError'] = []
graph['NotADirectoryError'] = []
graph['PermissionError'] = []
graph['ProcessLookupError'] = []
graph['TimeoutError'] = []
graph['NotImplementedError'] = []
graph['RecursionError'] = []
graph['IndentationError'] = ['TabError']
graph['UnicodeError'] = ['UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeTranslateError']
graph['DeprecationWarning'] = []
graph['PendingDeprecationWarning'] = []
graph['RuntimeWarning'] = []
graph['SyntaxWarning'] = []
graph['UserWarning'] = []
graph['FutureWarning'] = []
graph['ImportWarning'] = []
graph['UnicodeWarning'] = []
graph['BytesWarning'] = []
graph['ResourceWarning'] = []

# 4-й уровень
graph['BrokenPipeError'] = []
graph['ConnectionAbortedError'] = []
graph['ConnectionRefusedError'] = []
graph['ConnectionResetError'] = []
graph['TabError'] = []
graph['UnicodeDecodeError'] = []
graph['UnicodeEncodeError'] = []
graph['UnicodeTranslateError'] = []


# Сам алгоритм

def exception_was_found(exception, i_want_to_find):
    return exception == i_want_to_find


def search(graph, i_want_to_find):
    search_queue = deque()
    search_queue += graph['root']
    while search_queue:
        exception = search_queue.popleft()
        if exception_was_found(exception, i_want_to_find):
            return True
        else:
            search_queue += graph[exception]
    return False


if __name__ == '__main__':
    test_arr = [
        'BaseException', 'GeneratorExit', 'StopAsyncIteration', 'OverflowError',
        'ModuleNotFoundError', 'LookupError', 'ChildProcessError', 'ConnectionAbortedError',
        'Warning', 'ResourceWarning', 'MyException', '123', '', True, 231, object]

    for i_want_to_find in test_arr:
        if search(graph, i_want_to_find):
            print(i_want_to_find, 'найден')
        else:
            print(i_want_to_find, 'не найден')
