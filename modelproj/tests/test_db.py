from modpro.db import MyDB
import pytest
import logging

logger = logging.getLogger(__name__)


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


def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123


def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
