FROM python:3.7-alpine

# python-ldap requirements
RUN apk add openldap-dev libc-dev gcc

# psycopg2 requirements
RUN apk add libpq python3-dev musl-dev postgresql-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]