# RAG-Anything

[![PyPI version](https://badge.fury.io/py/raganything.svg)](https://badge.fury.io/py/raganything)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**RAG-Anything** is a universal Retrieval-Augmented Generation (RAG) framework that supports multimodal documents including PDFs, images, tables, charts, and more.

## Features

- 📄 **Universal Document Support** — Parse PDFs, Word documents, PowerPoint, HTML, and more
- 🖼️ **Multimodal Understanding** — Handle images, charts, tables, and figures natively
- 🔍 **Hybrid Retrieval** — Combine dense and sparse retrieval for optimal results
- 🧠 **Graph-Enhanced RAG** — Leverage knowledge graphs for deeper context understanding
- 🔌 **LLM Agnostic** — Works with OpenAI, Anthropic, local models, and more
- ⚡ **Async-First** — Built for high-performance concurrent workloads

## Installation

```bash
pip install raganything
```

For full multimodal support:

```bash
pip install raganything[full]
```

## Quick Start

```python
from raganything import RAGAnything

# Initialize with your preferred LLM
rag = RAGAnything(
    llm_model="gpt-4o",
    embedding_model="text-embedding-3-small",
    working_dir="./rag_storage"
)

# Index a document (PDF, DOCX, PPTX, images, etc.)
await rag.index_file("path/to/your/document.pdf")

# Query your documents
result = await rag.query("What are the key findings in the document?")
print(result)
```

## Supported File Types

| Format | Extension | Multimodal |
|--------|-----------|------------|
| PDF | `.pdf` | ✅ |
| Word | `.docx` | ✅ |
| PowerPoint | `.pptx` | ✅ |
| Excel | `.xlsx` | ✅ |
| HTML | `.html` | ✅ |
| Markdown | `.md` | ❌ |
| Plain Text | `.txt` | ❌ |
| Images | `.png`, `.jpg`, `.jpeg` | ✅ |

## Configuration

```python
from raganything import RAGAnything, RAGAnythingConfig

config = RAGAnythingConfig(
    llm_model="gpt-4o",
    embedding_model="text-embedding-3-small",
    max_tokens=4096,
    chunk_size=800,   # reduced from 1200 — smaller chunks improve retrieval precision for dense docs
    chunk_overlap=150,  # increased from 100 — helps preserve context across chunk boundaries
    enable_image_processing=True,
    enable_table_processing=True,
    top_k=10,  # increased from default 5 — retrieving more candidates improves recall on longer docs
)

rag = RAGAnything(config=config, working_dir="./rag_storage")
```

## Environment Variables

```bash
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key  # optional
```

## Documentation

Full documentation is available at [https://raganything.readthedocs.io](https://raganything.readthedocs.io).

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) and check out the [open issues](https://github.com/your-org/RAG-Anything/issues).

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing
