# XMLang

XMLang is a programming language using XML

## Documentation

The first module defined in the XMLang file will be treated as the entrypoint, therefore you MUST define a main function within the first module of the file

Names are limited to whatever is valid in C and C++, therefore you must avoid C++ and C keywords.

Functions are declared using `<func name="NAME_HERE">`, if you declare a function, you MUST include `<args>`
example:
```xml
<func name="main">
    <args>
        <arg type="uint8" name="B" />
    </args>
</func>
```
no args:
```xml
<func name="main">
    <args>
    </args>
</func>
```
this is a feature, not a bug.

Modules are declared using `<module name="NAME_HERE">`, you can import modules using `<import module_name="MODULE_NAME_HERE">`
example:
```xml
<module name="silly">
    <func name="main">
        <args>
            <arg type="uint8" name="B" />
        </args>
    </func>
</module>
```

To declare a primitive constant like the number `5`, just use `<value numeric_value="5">`, for strings, use `<value value="S">`

To declare a variable, one must use `<declare type="TYPE_HERE" name="NAME_HERE">`, current supported types are `uint8`, `uint16`, `uint32`, `uint64` and their respective signed integer name counterparts along with `float` and `double`.

To assign a value to a variable, just use `<assign name="NAME_HERE">`
example:
```xml
<assign name="x">
    <value numeric_value="5" />
</assign>
```

To use a variable, it is simple, just use `<variable name="NAME_HERE">`

Operators are done via `<operator op="OPERATOR_HERE">`, supported operators are `/`, `+`, `-` and `*`
Example usage is
```xml
<operator op="*">
    <variable name="x" />
    <variable name="y" />
</operator>
```
The above XMLang translates to (x * y)
```xml
<operator op="*">
    <variable name="x" />
    <variable name="y" />
    <variable name="z" />
</operator>
```
The above XMLang translates to (x * y * z)

Casting is done via `<cast type="TYPE_HERE">`, supported types are the aforementioned supported types
```xml
<cast type="uint8">
    <variable name="x" />
</cast>
```
The above XMLang translates to ((uint8) (x))

In order to cast the result of an operator:
```xml
<cast type="uint16">
    <operator op="*">
        <variable name="x" />
        <variable name="y" />
        <variable name="z" />
    </operator>
</cast>
```
which translates to ((uint16) ((x * y * z)))

