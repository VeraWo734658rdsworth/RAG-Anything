"""RAG-Anything: A universal RAG framework that can process and understand any type of content.

This package provides a flexible and extensible RAG (Retrieval-Augmented Generation)
framework capable of handling multiple modalities including text, images, tables,
equations, and more.

Personal fork notes:
- Forked from HKUDS/RAG-Anything for personal learning and experimentation
- See README for original project documentation
"""

from raganything.raganything import RAGAnything
from raganything.modalprocessors import (
    ImageProcessor,
    TableProcessor,
    EquationProcessor,
    GeneralProcessor,
)

__version__ = "0.1.0"
__author__ = "HKUDS"
__license__ = "MIT"

__all__ = [
    "RAGAnything",
    "ImageProcessor",
    "TableProcessor",
    "EquationProcessor",
    "GeneralProcessor",
]
