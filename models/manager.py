import psycopg2
from abc import ABC, abstractmethod
from yaml import safe_load

class DBManager(ABC):
    """
    DBManager interface for any type of database.
    Nice decoupling to not depend on any external module very hard.
    """
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def cursor(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def commit(self):
        pass


    @abstractmethod
    def close(self):
        pass

class PostgresManager(DBManager):
    """Manager for handling stuff related to Postgres databases."""
    def __init__(self, env_file_path: str = 'env.yml', **kwargs) -> None:
        super().__init__()
        self.env_file_path = env_file_path
        self.env = self._read_yaml()
        self.kwargs = kwargs
        self._connect = None
        self._cursor = None

    def _read_yaml(self) -> dict:
        """Load the env.yml file as dictionary"""
        with open(self.env_file_path, mode='r') as f:
            return safe_load(f)

    def connect(self):
        self._connect = psycopg2.connect(
            dbname=self.env.get('POSTGRES_DB'),
            user=self.env.get('POSTGRES_USER'),
            password=self.env['POSTGRES_PASSWORD'],
            port=self.env.get('port'),
            host=self.env.get('host'),
            **self.kwargs
        )
        # to make it easier hueehu
        self._connect.set_session(autocommit=True)
        return self

    def cursor(self):
        if self._cursor is None:
            self._cursor = self._connect.cursor()
        return self._cursor

    def execute(self, *args, **kwargs):
        return self._cursor(*args, **kwargs)

    def commit(self, *args, **kwargs):
        return self._connect.commit(*args, **kwargs)

    def close(self):
        return self._connect.close()

class DBHandler:
    """General context-manager for any DBManager."""
    def __init__(self, manager: DBManager) -> None:
        self.manager = manager()

    def __enter__(self):
        self.connect = self.manager.connect()
        return self.manager

    def __exit__(self, *_args, **_kwargs):
        self.connect.close()

