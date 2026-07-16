from pathlib import Path

# ----------------------------
# Project Paths
# ----------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"

PROMPTS_DIR = PROJECT_ROOT / "prompts"

ASSETS_DIR = PROJECT_ROOT / "assets"

# ----------------------------
# Search Configuration
# ----------------------------

MAX_SEARCH_RESULTS = 5

# ----------------------------
# Chunk Configuration
# ----------------------------

CHUNK_SIZE = 700

CHUNK_OVERLAP = 100

# ----------------------------
# Embedding Model
# ----------------------------

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"