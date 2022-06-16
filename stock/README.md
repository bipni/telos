# Stock Folder
This folder contains all the snippets, that is not the core code of `telos`. But still you can use `stock codes` in `telos` by importing them as a module.

## Example
If you want to import `MyIP` from `stock` in somewhere in `telos`, then we should write -
```python
from stock.MyIP import MyIP
```

and then simply call the method, defined in `MyIP`.
```python
values = MyIP.get_ip()
print(values)
```
This will give you, your PC IP address.
```bash
192.168.x.x
```

What if you don't want to import `MyIP` in your code, but want to run the `MyIP`, then just run -
```bash
$ telos myip
$ 192.168.x.x
```

## Stock Code Class and Run Method
All the stock code should contain a `run` method, which is invoked by the `telos`. `run` method always returns the results.
```python
def run():
    return MyIP.get_ip()
```
All the method in a class of `stock` should be `@staticmethod`. Here is a prototype of `stock code`.

```python
class DemoClass:

    @staticmethod
    def demo_method():
        # implementation

        return results

def run():
    return DemoClass.demo_method()
```