import hashlib
import os
import secrets

import psycopg2
import psycopg2.extras

import settings


def getConnection():
    return psycopg2.connect(settings.PSQL_DSN, cursor_factory=psycopg2.extras.RealDictCursor)


def createAllTables():
    conn = getConnection()
    with conn:
        with conn.cursor() as cursor:
            with open(os.path.join(settings.ROOT_PATH, 'sql', 'table', 'user.sql')) as f:
                cursor.execute(f.read())
            with open(os.path.join(settings.ROOT_PATH, 'sql', 'table', 'token.sql')) as f:
                cursor.execute(f.read())
            with open(os.path.join(settings.ROOT_PATH, 'sql', 'table', 'context.sql')) as f:
                cursor.execute(f.read())
            with open(os.path.join(settings.ROOT_PATH, 'sql', 'table', 'history.sql')) as f:
                cursor.execute(f.read())
            with open(os.path.join(settings.ROOT_PATH, 'sql', 'table', 'device.sql')) as f:
                cursor.execute(f.read())


def createUser(username, password):
    salt = secrets.token_hex(20)
    password = hashlib.sha256(bytes(password + salt, 'utf8')).hexdigest()

    sql = F"""
        INSERT INTO smartify.user (use_username, use_password_salt, use_password) VALUES
                                  ('{username}', '{salt}', '{password}') RETURNING *;
        """
    conn = getConnection()
    with conn:
        with conn.cursor() as cursor:
            with open(os.path.join(settings.ROOT_PATH, 'sql', 'table', 'user.sql')) as f:
                cursor.execute(f.read())
            cursor.execute(sql)
            return cursor.fetchone()


def selectUserByUsername(username):
    sql = F"""
        SELECT use_id, use_username, use_password_salt, use_password, use_created_at
        FROM "smartify"."user"
        WHERE use_username='{username}';
        """
    conn = getConnection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()


def selectTokenByUseId(use_id):
    sql = F"""
        SELECT *
        FROM "smartify"."token"
        WHERE use_id='{use_id}';
        """
    conn = getConnection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()


def selectUserByUsernameValidate(username, password):
    user = selectUserByUsername(username)
    if user is None:
        return None
    if hashlib.sha256(bytes(password + user["use_password_salt"], 'utf8')).hexdigest() == user["use_password"]:
        return user
    return None


def createUpdateToken(user_id,
                      tok_token,
                      tok_token_type,
                      tok_token_scope,
                      tok_token_expires_in,
                      tok_token_refresh,
                      tok_token_expires_at: str,
                      tok_last_updated_at: str):
    sql = F"""
        INSERT INTO smartify.token 
        (use_id, tok_token, tok_token_type, tok_token_scope, tok_token_expires_in,
        tok_token_refresh, tok_token_expires_at, tok_last_updated_at) VALUES
        ('{user_id}','{tok_token}','{tok_token_type}','{tok_token_scope}','{tok_token_expires_in}',
        '{tok_token_refresh}','{tok_token_expires_at}','{tok_last_updated_at}')
        ON CONFLICT (use_id) DO UPDATE SET
            tok_token='{tok_token}',
            tok_token_type='{tok_token_type}',
            tok_token_scope='{tok_token_scope}',
            tok_token_expires_in='{tok_token_expires_in}',
            tok_token_refresh='{tok_token_refresh}',
            tok_token_expires_at='{tok_token_expires_at}',
            tok_last_updated_at='{tok_last_updated_at}'
        WHERE "smartify"."token"."use_id"='{user_id}'
        RETURNING *;
        """
    conn = getConnection()
    with conn:
        with conn.cursor() as cursor:
            with open(os.path.join(settings.ROOT_PATH, 'sql', 'table', 'token.sql')) as f:
                cursor.execute(f.read())
            cursor.execute(sql)
            return cursor.fetchone()


def selectToken(user_id):
    sql = F"""
        SELECT tok_id, use_id, tok_token, tok_token_type, tok_token_scope, tok_token_expires_in,
        tok_token_refresh, tok_token_expires_at, tok_last_updated_at
        FROM smartify.token 
        WHERE use_id='{user_id}'
        """
    conn = getConnection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()


createAllTables()
