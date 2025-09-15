# XMLang

XMLang is a programming language using XML

## Documentation

current supported types are `uint8`, `uint16`, `uint32`, `uint64` and their respective signed integer name counterparts along with `float` and `double`

The first module defined in the XMLang file will be treated as the entrypoint, therefore you MUST define a main function within the first module of the file

Names are limited to whatever is valid in C and C++, therefore you must avoid C++ and C keywords.

Functions are declared using `<func type="TYPE_HERE" name="NAME_HERE">`, if you declare a function, you MUST include `<args>` and it always must come first within the function
example:
```xml
<func type="uint32" name="main">
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

In order to return from a function, use `<return name="NAME_HERE">` to return a variable's value. You cannot return a value directly.
example:
```xml
<func name="main">
    <args>
    </args>
    <declare type="uint8" name="x" />
    <assign name="x">
        <value type="uint8">5</value>
    </assign>
    <return name="x" />
</func>
```

to call a function, just use `<call name="NAME_HERE">` to call a function, in order to call a function you imported, use the `"MODULE_NAME::FUNC_NAME"` format (importing `x` from module `b` means you have to use `b::x` for the name for `name="NAME_HERE"`), each variable inside the `<call>` is an argument for the function. For no arguments, leave it blank.
example:
```xml
<call name="add">
    <variable name="x" />
    <variable name="y" />
</call>
```

Modules are declared using `<module name="NAME_HERE">`, you can import modules using `<import module_name="MODULE_NAME_HERE">`
example:
```xml
<module name="silly">
    <func type="uint32" name="main">
        <args>
            <arg type="uint8" name="B" />
        </args>
    </func>
</module>
```

To declare a primitive `uint8` constant like the number `5`, just use `<value type="uint8">5</value>`. Strings also work here, just use the `string` type

To declare a variable, one must use `<declare type="TYPE_HERE" name="NAME_HERE">`, current supported types are `uint8`, `uint16`, `uint32`, `uint64` and their respective signed integer name counterparts along with `float` and `double` and `string`.
example:
```xml
<declare type="uint8" name="x" />
```

To assign a value to a variable, just use `<assign name="NAME_HERE">`
example:
```xml
<assign name="x">
    <value type="uint8">5</value>
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

Increment and decrement are simple, `<increment name="NAME_HERE">` and `<decrement name="NAME_HERE">`

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

