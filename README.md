The compiled code (.pyc files) can be used if we wish for others to be able to execute but not to read or modify the source code. This will require the version of python to be the same.

To generate bytecode:

```shell
python3 build.py
python3 app
```

The end user can still technically decompile the code. But that's applicable to all builds from any language. The decompile step is not trivial.
