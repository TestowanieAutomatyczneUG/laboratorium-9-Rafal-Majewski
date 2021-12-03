```python
from unittest.mock import Mock, call
```
z biblioteki unitest importuje mock.Mock oraz mock.call.


```python
mock = Mock()
```
tworzy atrapę.


```python
mock.x
# <<< <Mock name='mock.x' id='139717963155008'>
```
odczytuje wartość atrybutu `x` z atrapy.
nie podawaliśmy nigdzie wartości, więc zwracana jest inna instancja klasy Mock.


```python
mock.x(*args, **kwargs)
# w zadaniu:
# -------------------
# mock.x('Foo', 3,14)
# <<< <Mock name='mock.x()' id='139717960219328'>
# 
# mock.x('Foo', 3,14)
# <<< <Mock name='mock.x()' id='139717960219328'>
#
# mock.x('Foo', 99, 12)
# <<< <Mock name='mock.x()' id='139717960219328'>
#
# mock.x()
# <<< <Mock name='mock.x()' id='139717960219328'>
```
wywołuje metodę `x` z atrapy.
nie zdefiniowaliśmy zwracanej wartości przez `x`, więc zwracana jest inna instancja klasy Mock.


```python
mock.y(mock.x('Foo',1,1))
# <<< <Mock name='mock.y()' id='139717953023376'>
```
wywołuje metodę `y` z atrapy,
przekazując jako argument wartość zwracaną przez metodę `x` dla argumentów `'Foo', 1, 1`.
dla metody `y` nie jest zdefiniowana zwracana wartość ani efekt uboczny, więc zwracana jest inna instancja klasy Mock.


```python
mock.method_calls
# <<< [call.x('Foo', 3, 14),
#      call.x('Foo', 3, 14),
#      call.x('Foo', 99, 12),
#      call.x(),
#      call.x('Foo', 1, 1),
#      call.y(<Mock name='mock.x()' id='140108041329200'>)]
```
zwraca listę wywołań metod z atrapy.
uwaga: zwracany typ to nie `list` a klasa `unittest.mock._CallList`.
każde z wywołań jest instancją klasy `unittest.mock._Call`.
z każdego z wywołań można odczytać jakie parametry zostały wtedy użyte.


```python
mock.assert_has_calls([call.x('Foo',1,1)])
```
asercja sprawdzająca czy metoda `x` atrapy została wywołana z argumentami `'Foo', 1, 1`.
asercja zakańcza się sukcesem.


```python
mock.assert_has_calls([call.x('Foo',1,1), call.x('Foo',99,12)])
```
asercja sprawdzająca czy metoda `x` atrapy została wywołana
(w takiej kolejności jak podano w liście)
z argumentami `'Foo', 1, 1` i `'Foo', 99, 12`.
asercja zakańcza się następującym błędem:
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.9/unittest/mock.py", line 944, in assert_has_calls
    raise AssertionError(
AssertionError: Calls not found.
Expected: [call.x('Foo', 1, 1), call.x('Foo', 99, 12)]
Actual: [call.x('Foo', 3, 14),
 call.x('Foo', 3, 14),
 call.x('Foo', 99, 12),
 call.x(),
 call.x('Foo', 1, 1),
 call.y(<Mock name='mock.x()' id='140108041329200'>)]
 ```
 ponieważ kolejność wywoływania metody `x` atrapy była inna


```python
mock.assert_has_calls([call.x('Foo',1,1), call.x('Foo',99,12)], any_order = True)
```
asercja sprawdzająca czy metoda `x` atrapy została wywołana z argumentami `'Foo', 1, 1` i `'Foo', 99, 12`.
tym razem kolejność wywoływania metody `x` atrapy nie ma znaczenia.
asercja zakańcza się sukcesem.


```python
mock.assert_has_calls([call.y(mock.x.return_value)])
```
asercja sprawdzająca czy metoda `y` atrapy została wywołana
z argumentem będącym zwracaną wartością przez metodę `x` atrapy.
asercja zakańcza się sukcesem.