# XMLang

XMLang is a programming language using XML

Implemented features have a `+`, non-implemented features have a `-` and partially implemented features have a `?`

## Documentation

XML entites are supported

current supported types are `uint8_t`, `uint16_t`, `uint32_t`, `uint64_t` and their respective signed integer name counterparts along with `float` and `double` and `char`

the `int8_t`/`uint8_t` types will print out the character whose codepoint is the value stored in the variable. Make sure to cast to at least `uint16_t` or `float` in order to print the value instead of the character whose codepoint is that value.

The first "module" in the file is not really a module, it has the tag name `<main>` as an entrypoint must be declared for the code to actually run

Names are limited to whatever is valid in C and C++, therefore you must avoid C++ and C keywords.

### Structures `-`

#### Structures are NOT implemented yet as of XMLang `0.1.0`

To define an object, just use `<struct name="NAME_HERE">`. To define attributes, just use `<variable>`
example:
```xml
<struct name="struc">
    <variable type="uint8_t" name="H" />
</struct>
```

### Functions `?`

#### Function writing `+`

Functions are declared using `<func type="TYPE_HERE" name="NAME_HERE">`, if you declare a function, you MUST include `<args>` and it always must come first within the function. For arguments that are arrays, append `*` to the type
example:
```xml
<func type="uint32_t" name="main">
    <args>
        <arg type="uint8_t" name="B" />
        <arg type="uint8_t*" name="C" />
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
    <declare type="uint8_t" name="x" />
    <assign name="x">
        <value type="uint8_t">5</value>
    </assign>
    <return name="x" />
</func>
```

#### Function calling `+`

to call a function, just use `<call name="NAME_HERE">` to call a function, in order to call a function you imported, use the `"MODULE_NAME::FUNC_NAME"` format (importing `x` from module `b` means you have to use `b::x` for the name for `name="NAME_HERE"`), each variable inside the `<call>` is an argument for the function. For no arguments, leave it blank.
example:
```xml
<call name="add">
    <variable name="x" />
    <variable name="y" />
</call>
```

### Modules `-`

Modules are declared using `<module name="NAME_HERE">`, you can import modules using `<import module_name="MODULE_NAME_HERE">`
example:
```xml
<module name="silly">
    <func type="uint32_t" name="main">
        <args>
            <arg type="uint8_t" name="B" />
        </args>
    </func>
</module>
```

### Variables `+`

#### Non-array

##### Primitive declaration

To declare a primitive `uint8_t` constant like the number `5`, just use `<value type="uint8">5</value>`.

To declare a variable, one must use `<declare type="TYPE_HERE" name="NAME_HERE">`.
example:
```xml
<declare type="uint8_t" name="x" />
```

##### Assignment

To assign a value to a variable, just use `<assign name="NAME_HERE">`
example:
```xml
<assign name="x">
    <value type="uint8_t">5</value>
</assign>
```

#### Arrays `+`

##### Array declaration

To declare an array, use `<adecl size="SIZE_HERE" type="TYPE_HERE" name="NAME_HERE" />`. `size` is length of array, `type` is one of the supported types and `name` is a variable name. Arrays may contain empty/null elements so make you know what you're doing. `size` can be a variable.

##### Array referencing

To reference an array, use `<variable name="NAME_HERE[INDEX_HERE]">`. Zero-based indexing, variable indexes are supported.

##### Array assignment

To assign to an array, use `<assign name="NAME_HERE[INDEX_HERE]">`. `INDEX_HERE` can be any constant value or a variable
example:
```xml
<assign name="arr[4]">
    <value type="uint8_t">5</value>
</assign>
```
In order to assign a string (array of `char`) to an array, use `<assign>`. Use type `string` for `<value>` for such use cases.
example:
```xml
<assign name="charr">
    <value type="string">beans</value>
</assign>
```

Arrays have no real memory safety, you can index and write out of bounds so be careful! To free an array, use `<free name="NAME_HERE">`

#### Variable referencing

To use a variable, it is simple, just use `<variable name="NAME_HERE">`

### Operators `+`

Operators are done via `<operator op="OPERATOR_HERE">`, supported operators are `/`, `+`, `-`, `*`, `<`, `>`. The angle brackets must be escaped using XML entities because XML.
Example usage is
```xml
<operator op="*">
    <value type="uint8_t">5</value>
    <variable name="y" />
</operator>
```
The above XMLang translates to (5 * y)
```xml
<operator op="*">
    <variable name="x" />
    <variable name="y" />
    <variable name="z" />
</operator>
```
The above XMLang translates to (x * y * z)

#### Increment/Decrement `-`
    
Increment and decrement are simple, `<increment name="NAME_HERE">` and `<decrement name="NAME_HERE">`


### Accessing attributes `+`

In order to access the attribute of a variable or array index, use `<prop prop="PROPERTY_HERE">`. Below is an example to access attribute `b` of `a` (aka `a.b`).
```xml
<prop prop="b">
    <variable name="a" />
</prop>
```
For arrays, it's the same but instead you use indexing syntax.
```xml
<prop prop="b">
    <variable name="swaws[4]"/>
</prop>
```


##### type-casting `+`

Casting is done via `<cast type="TYPE_HERE">`, supported types are the aforementioned supported types
```xml
<cast type="uint8_t">
    <variable name="x" />
</cast>
```
The above XMLang translates to ((uint8_t) (x))

In order to cast the result of an operator:
```xml
<cast type="uint16_t">
    <operator op="*">
        <variable name="x" />
        <variable name="y" />
        <variable name="z" />
    </operator>
</cast>
```
which translates to ((uint16_t) ((x * y * z)))


### Extras

#### Loops `+`

For loops are cringe, while loops are easier to program for this language. Therefore, only while loops are implemented
use the `<while>` tag for a while loop, the first tag inside the `<while>` tag MUST be a `<condition>` tag.
example:
```xml
<while>
    <condition>
        <operator op="<">
            <variable name="x" />
            <value type="uint8_t">67</value>
        </operator>
    </condition>
</while>
```
This translates to `while (x < 67)`

#### Conditional `+`

If statements, you use `<if>`, first tag inside the `<if>` MUST be a `<condition>` tag.
example:
```xml
<if>
    <condition>
        <operator op="<">
            <variable name="x" />
            <value type="uint8_t">67</value>
        </operator>
    </condition>
</if>
```

#### IO

##### Printing `-`

To print to console, use `<print>`
example:
```xml
<print>
    <variable name="x" />
</print>
```
If you want a newline, just add the `newline` attribute (`<print newline="1">`)