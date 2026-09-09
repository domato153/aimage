from __future__ import annotations

from pathlib import Path

from sqlalchemy import Engine, create_engine, event

AIMAGE_BEGIN_IMMEDIATE = "aimage_sqlite_begin_immediate"


def create_sqlite_engine(path: str | Path) -> Engine:
    """Create SQLite with SQLAlchemy-owned explicit transaction starts.

    Python sqlite3's ``autocommit=False`` mode keeps a transaction open and therefore
    cannot be combined with a later explicit ``BEGIN IMMEDIATE``.  We instead disable
    sqlite3's implicit BEGIN emission and let SQLAlchemy's begin event emit exactly one
    BEGIN.  Ordinary transactions use deferred ``BEGIN``; currentness compare/advance
    operations opt into ``BEGIN IMMEDIATE`` through an AIMAGE execution option.
    """

    engine = create_engine(
        f"sqlite+pysqlite:///{Path(path)}",
        future=True,
    )

    @event.listens_for(engine, "connect")
    def _configure_connection(dbapi_connection, _connection_record) -> None:  # type: ignore[no-untyped-def]
        # SQLAlchemy 2.0's documented explicit-BEGIN recipe: disable sqlite3's own
        # implicit BEGIN handling. COMMIT/ROLLBACK remain DBAPI-managed.
        dbapi_connection.isolation_level = None
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    @event.listens_for(engine, "begin")
    def _begin(connection) -> None:  # type: ignore[no-untyped-def]
        statement = "BEGIN IMMEDIATE" if connection.get_execution_options().get(AIMAGE_BEGIN_IMMEDIATE) else "BEGIN"
        connection.exec_driver_sql(statement)

    return engine
