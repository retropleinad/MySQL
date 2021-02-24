import enum


class StringData(enum):
    CHAR = 1
    VARCHAR = 2
    BINARY = 3
    VARBINARY = 4
    TINYBLOB = 5
    TINYTEXT = 6
    TEXT = 7
    BLOB = 8
    MEDIUMTEXT = 9
    MEDIUMBLOB = 10
    LONGTEXT = 11
    LONGBLOB = 12
    ENUM = 13
    SET = 14


class NumericData(enum):
    BIT = 1
    TINYINT = 2
    BOOL = 3
    BOOLEAN = 4
    SMALLINT = 5
    MEDIUMINT = 6
    INT = 7
    INTEGER = 8
    BIGINT = 9
    FLOAT = 10
    DOUBLE = 11
    DECIMAL = 12
    DEC = 13


class DateTime(enum):
    DATE = 1
    DATETIME = 2
    TIMESTAMP = 3
    TIME = 4
    YEAR = 5