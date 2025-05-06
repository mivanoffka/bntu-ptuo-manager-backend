-- Active: 1745413193697@@127.0.0.1@5432@bntu_ptuo_db
INSERT INTO
    genders (id, label)
VALUES
    (0, 'Женский'),
    (1, 'Мужской');

INSERT INTO
    education_levels (id, label)
VALUES
    (0, 'Начальное'),
    (1, 'Основное'),
    (2, 'Среднее'),
    (3, 'Среднеe специальное'),
    (4, 'Профессионально-техническое'),
    (5, 'Незаконченное высшее'),
    (6, 'Высшее');

INSERT INTO
    academic_degrees (id, label)
VALUES
    (0, 'Кандидат наук'),
    (1, 'Доктор наук');

INSERT INTO
    phone_number_types (id, label)
VALUES
    (0, 'Мобильный'),
    (1, 'Домашний');

INSERT INTO
    relative_types (id, label)
VALUES
    (0, 'Ребёнок (родной)'),
    (1, 'Ребёнок (опека)');

INSERT INTO
    working_groups (id, label)
VALUES
    (0, 'Рабочие'),
    (1, 'Крестьяне'),
    (2, 'Интеллигенция');

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
    trade_union_departments (path, depth, numchild, label)
VALUES
    ('0001', 1, 2, 'БНТУ');

INSERT INTO
    trade_union_departments (path, depth, numchild, label)
VALUES
    ('00010001', 2, 1, 'ФИТР');

INSERT INTO
    trade_union_departments (path, depth, numchild, label)
VALUES
    ('00010002', 2, 0, 'ФММП');

INSERT INTO
    trade_union_departments (path, depth, numchild, label)
VALUES
    ('000100010001', 3, 0, 'Кафедра ПОИСиТ');

UPDATE trade_union_departments
SET
    numchild = 2
WHERE
    path = '0001';

UPDATE trade_union_departments
SET
    numchild = 1
WHERE
    path = '00010001';