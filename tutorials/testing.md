# Testing

## Principles

Principles:

1. Tests should be independant
2. Test driven development, you write the test before the code
3. The Mock module is used to simulate complex objects

## Unit Test

See calc.py

### DocTest

Is a simple way to document the basic functionality in the docstring.
```
In docstring

 >>> sum(2,3)
    5

if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
```


## PyTest

Can be used to create a more sophisticated battery of tests.

The tests will be in a subfolder in the main module, that way modules are available.

You use the test\_ prefix and run the command 

`$ py.test -v`

Quick [Documentation](https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm)

## Fixtures

They can be used to setup the necessary objects needed for the testing. See db.py
