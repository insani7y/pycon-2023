from typing import LiteralString


def query_user(user_id: str) -> None:
    query = f"SELECT * FROM data WHERE user_id = {user_id}"
    execute(query)


def execute(sql: LiteralString) -> None:
    ...
