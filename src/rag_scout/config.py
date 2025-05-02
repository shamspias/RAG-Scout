"""
Central configuration module.
Usage:
    from rag_scout.config import settings
    print(settings.OPENAI_API_KEY)
"""
from __future__ import annotations
import os
from pathlib import Path
from functools import lru_cache
from dotenv import load_dotenv

# 1) Load .env if it exists; environment variables always win
load_dotenv()


class _Settings:
    # ---- Embeddings ------------------------------------------------------
    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    COHERE_API_KEY: str | None = os.getenv("COHERE_API_KEY")
    VOYAGE_API_KEY: str | None = os.getenv("VOYAGE_API_KEY")

    # ---- Vector DBs ------------------------------------------------------
    PINECONE_API_KEY: str | None = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV: str | None = os.getenv("PINECONE_ENV", "us-east-1-gcp")
    QDRANT_URL: str = os.getenv("QDRANT_URL", "http://localhost:6333")
    QDRANT_API_KEY: str | None = os.getenv("QDRANT_API_KEY")
    WEAVIATE_URL: str | None = os.getenv("WEAVIATE_URL")
    WEAVIATE_API_KEY: str | None = os.getenv("WEAVIATE_API_KEY")

    # ---- Misc ------------------------------------------------------------
    CACHE_DIR: Path = Path(os.getenv("RAGSCOUT_CACHE_DIR", ".ragscout_cache"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # ---- helper ----------------------------------------------------------
    def require(self, attr: str) -> str:
        """Return value or raise.  Use in adapters that *must* have a key."""
        val = getattr(self, attr)
        if not val:
            raise RuntimeError(f"Environment variable {attr} is not set")
        return val


# singleton
settings = _Settings()


@lru_cache
def as_dict() -> dict[str, str | Path]:
    """Convenient for dumping into reports."""
    return {k: v for k, v in vars(settings).items() if k.isupper()}
