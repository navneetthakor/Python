# Installations
- install directly from `python.org`
 
## ways to use python
- for temporory purpose
    - online compilers

- for backend developement
    - installation of `python` and any code editor like `vscode`

- for Data Science and AI related task
    - google/kaggle nodebook
    - Anaconda

# Inner working

## How python code executes
- python script -> byte code (machine independent) (.pyc file) -> Python Virtual Machine (PVM) -> final output
- PVM has one loop running which takes each file as input and produce it's output that's why we called it as `interpreted language`.
- `.pyc` will only be created in case of `import` statements are present otherwise in top-level statements this file is hidden.

## Immutable and mutable
- mutables are those whose references can't be modified.
- in Python numbers, strings etc are immutable. 
    - so wherever we does like following
    ```
    score = 10
    ```
    it creates object of value 10 and assigns it's reference to ```score```

    - now if we do following
    ```
    tempScore = score
    ```
    now ```score``` and ```tempScore``` both are pointing to the same memory reference of ```10 value```.

    - if we modifiy one of them
    ```
    score = 20
    ```
    at this moment value of each variables are :
    ```
    score -> 20
    tempScore -> 10
    ```
    as python doesn't modify the memory refernce instead it creates new one and assigns it to the ```score```.
- but there are mutable objects which are updates ```in-place``` instead of creating new memory reference.
- additionally, type of object is reside in object value on in variable.
- this is similar to javascript so not going in much depth here.

## reference assignment
- for immutable data-types, if value exists in the memory then that will assign directly instead of creating new one
```
a = 2
b = 2
```

- but for mutable datatype like list, different memory reference objects are created
```
a = [1,2]
b = [1,2]
```

- and in following they are pointing to the same memory reference
```
a = [1,2]
b = a
```

## Garbage collection

### reference count
- whenever a refernce of object is created it have ```reference_count``` associated with it. but it is very difficult to get reference count of any variable.
- garbage collector is called for refernce object when, it's reference count reaches to 0. except for number and string it's not called immediately. 
