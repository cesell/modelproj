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

### Fixtures

If your tests need to work on data you typically need to set them up. This is often a process that has to be repeated and independent for each test.

The **@pytest.fixture** decorator provides an easy yet powerful way to setup and teardown resources. You can then pass these defined fixture objects into your test functions as input arguments.

Fixtures are also referred to as **dependency injections** 

By using a yield statement instead of return, all the code after the **yield** statement serves as the **teardown code**:

```
@pytest.fixture(scope="module")
def cur():
    logger.info('Connecting DB')
    db = MyDB()
    conn = db.connect("server")
    cursor = conn.cursor()
    yield cursor
    logger.info('Closing DB')
    cursor.close()
    conn.close()
```