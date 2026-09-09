from __future__ import annotations

from pathlib import Path

from sqlalchemy import Engine, create_engine, event


def create_sqlite_engine(path: str | Path) -> Engine:
    engine = create_engine(
        f"sqlite+pysqlite:///{Path(path)}",
        connect_args={"autocommit": False},
        future=True,
    )

    @event.listens_for(engine, "connect")
    def _foreign_keys_on(dbapi_connection, _connection_record) -> None:  # type: ignore[no-untyped-def]
        dbapi_connection.execute("PRAGMA foreign_keys=ON")

    return engine
