class MockPostgresLib:
    @staticmethod
    def multipleWrite(table, data):
        return f"[Postgres] Written to table '{table}': {data}"

    @staticmethod
    def read(table):
        return f"[Postgres] Reading from table '{table}'"

    @staticmethod
    def schema(table):
        return f"[Postgres] Schema for table '{table}': (id INT, payload TEXT)"


class MockMySQLLib:
    @staticmethod
    def write(table, data):
        return f"[MySQL] Written to table '{table}': {data}"

    @staticmethod
    def read(table):
        return f"[MySQL] Reading from table '{table}'"

    @staticmethod
    def schema(table):
        return f"[MySQL] Schema for table '{table}': (id INT AUTO_INCREMENT, payload VARCHAR(255))"


class MockOracleLib:
    @staticmethod
    def putInTable(table, data):
        return f"[Oracle] Written to table '{table}': {data}"

    @staticmethod
    def fetch(table):
        return f"[Oracle] Reading from table '{table}'"

    @staticmethod
    def describe(table):
        return f"[Oracle] Schema for table '{table}': (ID NUMBER, PAYLOAD VARCHAR2(255))"


postgresLib = MockPostgresLib()
mysqlLib = MockMySQLLib()
oracleLib = MockOracleLib()



TABLE = ""
DATABASE = "Postgres"



def setTable(table):
    global TABLE
    TABLE = table


def selectDatabase(database):
    global DATABASE
    DATABASE = database

def writeData(data):
    if DATABASE == "Postgres":
        return postgresLib.multipleWrite(TABLE, data)
    elif DATABASE == "MySQL":
        return mysqlLib.write(TABLE, data)
    elif DATABASE == "Oracle":
        return oracleLib.putInTable(TABLE, data)
    else:
        raise ValueError(f"Unsupported database: {DATABASE}")


def readData():
    if DATABASE == "Postgres":
        return postgresLib.read(TABLE)
    elif DATABASE == "MySQL":
        return mysqlLib.read(TABLE)
    elif DATABASE == "Oracle":
        return oracleLib.fetch(TABLE)
    else:
        raise ValueError(f"Unsupported database: {DATABASE}")


def getSchema():
    if DATABASE == "Postgres":
        return postgresLib.schema(TABLE)
    elif DATABASE == "MySQL":
        return mysqlLib.schema(TABLE)
    elif DATABASE == "Oracle":
        return oracleLib.describe(TABLE)
    else:
        raise ValueError(f"Unsupported database: {DATABASE}")

