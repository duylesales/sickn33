🏷️ PRODUCT LABEL: Akteslim API container (original recipe)

Net weight: over 2 GB
Contains: build tools, test data, a full copy of the repository's history
Runs as: root
Secret ingredients: OCR and AI provider API keys, baked in from a .env file
Base: "latest" tag, not updated in months
Serving suggestion: port exposed directly, no TLS
Shelf life of logs: until the next restart
Warning: may run out of memory on large scanned PDFs, without telling anyone
Deployment time: about twenty minutes

Iris Kok built Akteslim with Claude Code: a service that extracts key data from scanned deeds and contracts for small notary and legal offices. A React frontend on Vercel, Supabase for data and authentication, and a Python API for OCR and AI extraction. Claude Code wrote the Dockerfile, and Iris deployed it to a rented server by following a tutorial.

NEW RECIPE (LaunchStudio, 10 business days, €3,900)
Net weight: around 400 MB, thanks to a multi-stage build on a pinned slim base and a .dockerignore
Runs as: a non-root user
Secrets: rotated, and passed in as runtime environment variables
Quality control: image vulnerability scanning in a GitHub Actions pipeline
Serving: a managed container platform in an EU region, with TLS, health checks, memory limits and automatic restarts
Large documents: processed through a job queue, with progress updates
Logs: forwarded to a central log service, with alerts on failures
Deployment time: under three minutes

RESULT
Memory crashes stopped, large documents process reliably, and Akteslim passed a security review by a notary group's IT supplier, which had asked specifically about container security and secret handling.

"Claude Code gave me a working container. It took a proper review to turn it into one I'd let near my customers' deeds." - Iris Kok

Read your own container's label: https://launchstudio.eu/en/blog/docker-for-founders-when-your-app-needs-a-container

#Docker #Containers #ClaudeCode #LegalTech #AIFounder #LaunchStudio #Manifera
