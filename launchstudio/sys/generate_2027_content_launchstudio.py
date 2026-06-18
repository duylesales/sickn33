import os
import random

BASE_DIR = "/Users/duyle/sickn33/launchstudio"
MONTHS = [
    "january-2027", "february-2027", "march-2027", "april-2027",
    "may-2027", "june-2027", "july-2027", "august-2027",
    "september-2027", "october-2027", "november-2027", "december-2027"
]

THEMES = [
    "AI-Native Founders",
    "SaaS MVP with Lovable",
    "Cursor AI Development",
    "AI-Generated Code Quality",
    "From Prototype to Production",
    "Pre-Launch Security Audits",
    "Scaling AI Applications",
    "AI Builder Limitations",
    "Future of Non-Technical Founders",
    "Enterprise AI Strategy"
]

PREFIXES = [
    "The Ultimate Guide to", "How to Implement", "5 Strategies for",
    "Future Trends in", "Cost Analysis of", "Security Best Practices for",
    "Why Founders Choose", "Common Mistakes in", "A Strategic Approach to",
    "Understanding the ROI of"
]

def generate_social_post(title, keywords, month_idx, idx):
    emoji = "🚀"
    title_lower = title.lower()
    if "ai" in title_lower or "model" in title_lower: emoji = "🤖"
    elif "data" in title_lower or "database" in title_lower: emoji = "🗄️"
    elif "price" in title_lower or "cost" in title_lower or "roi" in title_lower: emoji = "💸"
    elif "security" in title_lower or "audit" in title_lower: emoji = "🔒"
    elif "scale" in title_lower or "growth" in title_lower: emoji = "📈"
    elif "founder" in title_lower or "startup" in title_lower: emoji = "👨‍💻"
    elif "app" in title_lower or "saas" in title_lower: emoji = "📱"

    post = f"{emoji} {title}\n\n"
    post += f"In 2027, the gap between an AI-generated prototype and a production-ready application is the biggest hurdle for founders. When dealing with {title.lower()}, you need more than just good prompts.\n\n"
    post += f"We've broken down the exact steps to ensure your app is secure, scalable, and ready for real users. Don't launch until you read this.\n\n"
    post += f"Learn how to bridge the gap to production: [Link]\n\n"
    post += "#SaaS #AI #Startups #Founders #LaunchStudio"
    return post

def generate_blog_content(title, keywords, theme):
    content = f"""---
Title: {title}
Keywords: {keywords}
Buyer Stage: Consideration
---

# {title}

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{title}",
  "description": "An in-depth analysis of {theme} specifically tailored for AI-native founders in 2027.",
  "image": "",
  "author": {{
    "@type": "Organization",
    "name": "Launch Studio",
    "url": "https://launchstudio.eu/en/"
  }}
}}
</script>

## Content

In the rapidly evolving landscape of software entrepreneurship in 2027, {theme.lower()} has emerged as a critical focus area. Founders who rely solely on AI tools like Lovable, Bolt, or Cursor often discover that while generating a prototype takes days, making it production-ready takes serious architectural oversight.

As an AI-native founder, your priority is time-to-market without sacrificing security or scalability. This guide explores the strategic imperatives of {theme.lower()} and how to safely bridge the gap between a demo and a launch-ready product.

### The Reality of {theme}

Traditionally, founders needed massive budgets to build scalable software. Today, AI democratizes the creation process. However, the paradigm has shifted toward managing the output of these AI tools effectively.

When executing a strategy centered around {theme.lower()}, companies must prioritize:
1. **Security Audits:** Ensuring no API keys are exposed and databases have proper Row Level Security.
2. **Architecture Scaling:** Moving beyond test environments and setting up robust CI/CD pipelines.
3. **Payment & Integrations:** Verifying Webhooks and ensuring stripe (or other gateways) are out of test mode.

### Conclusion

At LaunchStudio, we specialize in taking AI-built prototypes and making them launch-ready. By partnering with us, you can successfully navigate the complexities of {theme.lower()} and launch with confidence, saving thousands compared to traditional agencies.
"""
    return content

def main():
    inventory_lines = [
        "# 📚 Bảng Tổng Hợp Content LaunchStudio 2027\n\n",
    ]
    
    count = 0
    for m_idx, month in enumerate(MONTHS):
        dir_path = os.path.join(BASE_DIR, month)
        os.makedirs(dir_path, exist_ok=True)
        
        month_name = month.split('-')[0].capitalize()
        year_name = month.split('-')[1]
        
        inventory_lines.append(f"## Tháng: {month_name} {year_name}\n\n")
        inventory_lines.append("| Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn | Tóm lược | Ước tính views/tháng | Bài Social Media |\n")
        inventory_lines.append("|---|---|---|---|---|---|\n")

        
        # Generate 30 articles per month
        for i in range(1, 31):
            prefix = PREFIXES[i % len(PREFIXES)]
            theme = THEMES[(m_idx + i) % len(THEMES)]
            title = f"{prefix} {theme}"
            keywords = f"{theme.replace(' ', ', ')}, LaunchStudio, SaaS, AI-Native"
            
            # File names
            base_filename = f"{i:02d}-{title.lower().replace(' ', '-').replace(':', '')}"
            blog_filename = f"{base_filename}.md"
            social_filename = f"{base_filename}-social.md"
            
            # Generate contents
            blog_content = generate_blog_content(title, keywords, theme)
            social_content = generate_social_post(title, keywords, m_idx, i)
            
            # Write blog file
            with open(os.path.join(dir_path, blog_filename), "w", encoding="utf-8") as f:
                f.write(blog_content)
                
            # Write social file
            with open(os.path.join(dir_path, social_filename), "w", encoding="utf-8") as f:
                f.write(social_content)
                
            # Inventory entry
            snippet = f"In the rapidly evolving landscape of software entrepreneurship in 2027, {theme.lower()} has emerged as a critical focus area..."
            social_link = f"[{social_filename}](./{month}/{social_filename})"
            views = random.randint(150, 850)
            
            inventory_line = f"| {title} | {keywords} | Consideration | {snippet} | ~{views} | {social_link} |\n"
            inventory_lines.append(inventory_line)
            count += 1
            
        inventory_lines.append("\n")

            
    # Write inventory file
    inventory_path = os.path.join(BASE_DIR, "content_inventory_2027.md")
    with open(inventory_path, "w", encoding="utf-8") as f:
        f.writelines(inventory_lines)
        
    print(f"✅ Successfully generated {count} blog posts and {count} social posts across 12 months for LaunchStudio.")
    print(f"✅ Inventory saved to content_inventory_2027.md")

if __name__ == "__main__":
    main()
