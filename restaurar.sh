#!/bin/sh

docker exec -i cont_post pg_restore -U postgres -d postgres < ./sql/base1.sql