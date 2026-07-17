# Rewrite July 2026 Social Posts

## Goal Description
Rewrite all 60 English and 60 Dutch social media posts for LaunchStudio's July 2026 content batch (total 120 files). The new format will be more engaging, use the main keyword on the first line, feature lots of emojis, and utilize bullet points/lists to create a strong visual impact, modeled after the Manifera example (`01-ai-developers-social.md`).

## User Review Required
> [!IMPORTANT]
> The rewriting of 120 files requires significant generation output. To avoid hitting token limits, I will execute this in **4 batches (15 articles / 30 files per batch)**. I will directly overwrite the existing `.md` files using tool calls.

## Open Questions
> [!WARNING]
> 1. Are there any specific hashtags you want to ensure are included in *every* post (e.g. `#LaunchStudio`, `#SaaS`, `#Founders`)?
> 2. For the Dutch posts, should they be direct engaging translations of the English ones, or is there a specific Dutch localization tone you prefer?

## Proposed Changes
### Batch 1: Articles 01-15
- Overwrite `launchstudio/2026/july-2026/01...` to `15...-social.md`
- Overwrite `launchstudio/2026/july-2026/01...` to `15...-social_dutch.md`

### Batch 2: Articles 16-30
- Overwrite `launchstudio/2026/july-2026/16...` to `30...-social.md`
- Overwrite `launchstudio/2026/july-2026/16...` to `30...-social_dutch.md`

### Batch 3: Articles 31-45
- Overwrite `launchstudio/2026/july-2026/31...` to `45...-social.md`
- Overwrite `launchstudio/2026/july-2026/31...` to `45...-social_dutch.md`

### Batch 4: Articles 46-60
- Overwrite `launchstudio/2026/july-2026/46...` to `60...-social.md`
- Overwrite `launchstudio/2026/july-2026/46...` to `60...-social_dutch.md`

## Verification Plan
### Automated Tests
- `ls -l` in the directory to verify file modification times.
- Read a random sample to ensure the new format (keyword first line, emojis, lists) is applied.

### Manual Verification
- You can review the updated Markdown files directly in the IDE to ensure the style meets your expectations.
