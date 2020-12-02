#!/bin/sh



psql -U postgres -c "create database test;"

psql -U postgres -d test -c "create table aplication (name varchar(100) NOT NULL); insert INTO aplication values ('JOHN');" 
