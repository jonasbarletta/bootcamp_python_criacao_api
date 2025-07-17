# Importa ferramentas do SQLAlchemy necessárias para ORM e manipulação de banco de dados
from sqlalchemy.orm import sessionmaker       # Para criar sessões de acesso ao banco
from sqlalchemy import create_engine          # Para criar o motor de conexão com o banco de dados
from sqlalchemy.ext.declarative import declarative_base  # Para criar a base dos modelos ORM

# Define a URL de conexão com o banco de dados SQLite
# Nesse caso, o arquivo será criado como 'test.db' no diretório atual
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Cria o engine (motor) de conexão com o banco de dados
# Ele é a interface principal entre o SQLAlchemy e o banco real
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria uma fábrica de sessões com configurações:
# - autocommit=False: você controla quando confirmar as transações
# - autoflush=False: não envia alterações automaticamente para o banco
# - bind=engine: conecta essa fábrica ao engine criado acima
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a classe base para os modelos ORM
# Todos os modelos que representam tabelas do banco devem herdar dessa classe
Base = declarative_base()

# Função geradora que cria uma sessão com o banco de dados
# Utilizada para garantir que a sessão seja sempre fechada após o uso
def get_db():
    db = SessionLocal()     # Cria uma nova sessão
    try:
        yield db            # Entrega a sessão para uso externo (por exemplo, em um endpoint)
    finally:
        db.close()          # Garante que a sessão será fechada após o uso, evitando vazamentos
