# Social Media Post (Dutch): Handling PDF Parsing and Document Ingestion for RAG

Als u open-source `pdf2json` gebruikt om tekst te schrapen voor uw RAG-applicatie, hallucineert uw AI.

PDF's hebben geen semantische structuur. Standaard scrapers veranderen tabellen met twee kolommen in onleesbare "Data Salad". Als de AI de tabel niet kan lezen, kan hij de vraag van de gebruiker niet beantwoorden.

Om een Enterprise RAG-pijplijn te bouwen, moet u drie dingen doen:
1️⃣ Parsing: Gebruik Vision-modellen of LlamaParse om de PDF te lezen en schone **Markdown** uit te voeren (met behoud van tabellen en koppen).
2️⃣ Chunking: Stop met het snijden van chunks om de 1.000 tekens. Zinnen doormidden snijden vernietigt de context. Snijd semantisch bij Markdown `## Headers` of alinea-einden.
3️⃣ Asynchrone Wachtrijen: OCR duurt minuten. Voer het niet uit in een Next.js API route. Gebruik BullMQ + Redis om documenten op de achtergrond te verwerken zonder Vercel time-outs te veroorzaken.

Uw AI is slechts zo slim als de tekst die u hem voedt. Stop met het voeden van afval.

Lees onze RAG-ingestiegids op de LaunchStudio blog.

#LaunchStudio #RAG #AI #LLM #PdfParsing #Nextjs #BullMQ #LlamaParse
