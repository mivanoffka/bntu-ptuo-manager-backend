INSERT INTO
    bntu_departments (path, depth, numchild, label)
VALUES
    ('0001', 1, 2, 'БНТУ');

INSERT INTO
    bntu_departments (path, depth, numchild, label)
VALUES
    ('00010001', 2, 1, 'ФИТР');

INSERT INTO
    bntu_departments (path, depth, numchild, label)
VALUES
    ('00010002', 2, 0, 'ФММП');

INSERT INTO
    bntu_departments (path, depth, numchild, label)
VALUES
    ('000100010001', 3, 0, 'Кафедра ПОИСиТ');

UPDATE bntu_departments
SET
    numchild = 2
WHERE
    path = '0001';

UPDATE bntu_departments
SET
    numchild = 1
WHERE
    path = '00010001';

INSERT INTO
    trade_union_department_options (path, depth, numchild, label)
VALUES
    ('0001', 1, 2, 'БНТУ');

INSERT INTO
    trade_union_department_options (path, depth, numchild, label)
VALUES
    ('00010001', 2, 1, 'ФИТР');

INSERT INTO
    trade_union_department_options (path, depth, numchild, label)
VALUES
    ('00010002', 2, 0, 'ФММП');

INSERT INTO
    trade_union_department_options (path, depth, numchild, label)
VALUES
    ('000100010001', 3, 0, 'Кафедра ПОИСиТ');

UPDATE trade_union_department_options
SET
    numchild = 2
WHERE
    path = '0001';

UPDATE trade_union_department_options
SET
    numchild = 1
WHERE
    path = '00010001';