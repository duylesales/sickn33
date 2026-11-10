🚨 Iris Kok built Akteslim with Claude Code: a service for notary and legal offices that extracts key data from scanned deeds and contracts, with a Python API running OCR and AI extraction. Claude Code wrote a Dockerfile, and Iris deployed it to a rented server following a tutorial. 😳

The image was over 2 GB, deployments took twenty minutes, and the API keys were baked into the image. Here's when your app needs a container - and how to do Docker properly: 🧠

❌ A 2 GB image with build tools, test data and the full repo history
❌ The container running as root, with keys copied in from a .env file
❌ A months-old latest base image and a port exposed without TLS
❌ Logs lost on every restart, and silent out-of-memory crashes on large PDFs

✅ A multi-stage build on a pinned slim base, down to around 400 MB, running as non-root
✅ Keys rotated and moved to runtime environment variables
✅ Image vulnerability scanning in a GitHub Actions pipeline
✅ A managed EU container platform with TLS, health checks, memory limits, a job queue and central logs

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we turn a container that works into one you can trust near customer data. 🛠️

Her result: €3,900, 10 business days. Deployments now take under three minutes, memory crashes stopped, and Akteslim passed a notary group's IT security review. 🚀

👉 Does your app need Docker? Here's what founders should know: https://launchstudio.eu/en/blog/docker-for-founders-when-your-app-needs-a-container

#Docker #Containers #ClaudeCode #LegalTech #AIFounder #LaunchStudio #Manifera
