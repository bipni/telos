# Stock Folder
This folder contains all the snippets, that is not the core code of `telos`. But still you can use `stock codes` in telos by importing them as a module.

For example, if you want to import MyIP from `stock` in somewhere in `telos`, then we should write -
```
from stock.MyIP import MyIP
```

and then simply call the method, defined in MyIP.
```
values = MyIP.get_ip()
print(values)
```
This will give you, your PC IP address.
```
192.168.x.x
```

What if you don't want to import `MyIP` in your code, but want to run the `MyIP`, then just run -
```bash
$ telos MyIP
$ 192.168.x.x
```