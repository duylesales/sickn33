# Social Media Post: Handling PDF Parsing and Document Ingestion for RAG

If you are using open-source `pdf2json` to scrape text for your RAG application, your AI is hallucinating.

PDFs don't have semantic structure. Standard scrapers turn two-column tables into unreadable "Data Salad." If the AI can't read the table, it can't answer the user's question.

To build an Enterprise RAG pipeline, you must do three things:
1️⃣ Parsing: Use Vision models or LlamaParse to read the PDF and output clean **Markdown** (preserving tables and headers).
2️⃣ Chunking: Stop slicing chunks every 1,000 characters. Slicing sentences in half destroys context. Slice semantically at Markdown `## Headers` or paragraph breaks.
3️⃣ Asynchronous Queues: OCR takes minutes. Don't run it in a Next.js API route. Use BullMQ + Redis to process documents in the background without timing out Vercel.

Your AI is only as smart as the text you feed it. Stop feeding it garbage.

Read our RAG ingestion guide on the LaunchStudio blog.

#LaunchStudio #RAG #AI #LLM #PdfParsing #Nextjs #BullMQ #LlamaParse
