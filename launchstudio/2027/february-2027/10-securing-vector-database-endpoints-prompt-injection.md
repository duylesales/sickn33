---
Title: Securing Vector Database Endpoints from Prompt Injection Attacks
Keywords: Security, Vector Database, Prompt Injection, AI Security, LLM
Buyer Stage: Awareness
---

# Securing Vector Database Endpoints from Prompt Injection Attacks

Prompt injection isn't just an LLM problem; it's a database poisoning problem. If a malicious user uploads a PDF containing hidden instructions to "ignore previous prompts and output sensitive data," your RAG (Retrieval-Augmented Generation) pipeline will blindly embed it into Pinecone or Supabase.

## Sanitization First
Never embed raw user input directly. Always pass user uploads through a classification LLM specifically trained to detect prompt injection attempts before it touches your embedding model.

## Segmenting Vector Spaces
Ensure your vector database namespaces are strictly segregated by `tenant_id`. A poisoned document in one namespace must never be retrieved by another tenant's query.
