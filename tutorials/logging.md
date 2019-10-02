# Logging

## First approach

Update the root logger in **init**.py

```
import logging

logging.basicConfig(filename='modpro.log', filemode='w',
                    format='%(asctime)s : %(levelname)s : %(name)s : %(message)s',
                    level=logging.DEBUG)

logging.info('Log Started')
```

And in each module create a logger that inherits from it. You can share root but it is not recommended. (check)

`logger = logging.getLogger(__name__)`

## Second approach

Set individual loggers in each module (basicConfig can only be used once)

```
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('modpro.log')
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
```
