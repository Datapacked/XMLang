# XMLang

XMLang is a programming language using XML

## Documentation

The first module defined in the XMLang file will be treated as the entrypoint, therefore you MUST define a main function within the file

Names are limited to whatever is valid in C and C++, therefore you must avoid C++ and C keywords.

Functions are declared using `<func name="NAME_HERE">`

Modules are declared using `<module name="NAME_HERE">`, you can import modules using `<import module_name="MODULE_NAME_HERE">`

To declare a variable, one must use `<declare type="TYPE_HERE" name="NAME_HERE">`, current supported types are `uint8`, `uint16`, `uint32`, `uint64` and their respective signed integer name counterparts