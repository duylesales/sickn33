import os
import random

BASE_DIR = "/Users/duyle/sickn33/manifera"
MONTHS = [
    "january-2027", "february-2027", "march-2027", "april-2027",
    "may-2027", "june-2027", "july-2027", "august-2027",
    "september-2027", "october-2027", "november-2027", "december-2027"
]

THEMES = [
    "IT Outsourcing Trends",
    "Dedicated Software Team",
    "Offshore Development",
    "Laravel Architecture",
    "React Native vs Flutter",
    "DevOps Automation",
    "AI Integration",
    "B2B SaaS Scaling",
    "Custom Magento eCommerce",
    "QA and Testing Strategies"
]

PREFIXES = [
    "The Ultimate Guide to", "How to Implement", "5 Strategies for",
    "Future Trends in", "Cost Analysis of", "Security Best Practices for",
    "Why CTOs Choose", "Common Mistakes in", "A Strategic Approach to",
    "Understanding the ROI of"
]

def generate_social_post(title, keywords, month_idx, idx):
    emoji = "🚀"
    title_lower = title.lower()
    if "ai" in title_lower or "model" in title_lower: emoji = "🤖"
    elif "data" in title_lower or "database" in title_lower or "sql" in title_lower: emoji = "🗄️"
    elif "price" in title_lower or "cost" in title_lower or "roi" in title_lower: emoji = "💸"
    elif "security" in title_lower or "quality" in title_lower or "qa" in title_lower: emoji = "🔒"
    elif "scale" in title_lower or "growth" in title_lower or "devops" in title_lower: emoji = "📈"
    elif "offshore" in title_lower or "team" in title_lower or "cto" in title_lower: emoji = "👨‍💻"
    elif "app" in title_lower or "mobile" in title_lower: emoji = "📱"

    post = f"{emoji} {title}\n\n"
    post += f"In 2027, staying ahead means mastering the fundamentals. When approaching {title.lower()}, business leaders must weigh both technical excellence and cost-efficiency.\n\n"
    post += f"We have outlined the critical factors and advanced strategies your engineering team needs to succeed. Read our comprehensive analysis.\n\n"
    post += f"Discover more strategies for scaling your tech teams: [Link]\n\n"
    post += "#SoftwareDevelopment #TechLeadership #Manifera"
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
  "description": "An in-depth analysis of {theme} specifically tailored for tech leaders and CTOs in 2027.",
  "image": "",
  "author": {{
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://manifera.com"
  }}
}}
</script>

## Content

In the rapidly evolving landscape of software engineering in 2027, {theme.lower()} has emerged as a cornerstone for sustainable growth. Organizations that fail to adopt modern practices risk being left behind by more agile competitors. 

As a CTO or Engineering Manager, the pressure to deliver product roadmaps faster without ballooning the budget is immense. This guide explores the strategic imperatives of {theme.lower()} and how dedicated remote teams can act as an extension of your core in-house engineering unit to accelerate delivery.

### The Strategic Importance of {theme}

Traditionally, scaling meant months of recruiting, interviewing, and onboarding. However, the paradigm has shifted toward flexible, dedicated offshore teams that deeply integrate with your existing processes. 

When executing a strategy centered around {theme.lower()}, companies must prioritize:
1. **Seamless Integration:** Ensuring external teams log into your Slack and attend your daily stand-ups.
2. **Architecture First:** Relying on robust frameworks to avoid future technical debt.
3. **Data Security:** Maintaining strict zero-data-retention agreements when utilizing AI.

### Conclusion

At Manifera, we bridge the gap between European quality standards and Asian tech talent. By partnering with a dedicated offshore development center, you can successfully navigate the complexities of {theme.lower()} while saving up to 45% on local hiring costs.
"""
    return content

def main():
    inventory_lines = [
        "| Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn (Buyer Stage) | Đoạn trích (Snippet) | Bài Social Media |\n",
        "|---|---|---|---|---|\n"
    ]
    
    count = 0
    for m_idx, month in enumerate(MONTHS):
        dir_path = os.path.join(BASE_DIR, month)
        os.makedirs(dir_path, exist_ok=True)
        
        # Generate 30 articles per month
        for i in range(1, 31):
            prefix = PREFIXES[i % len(PREFIXES)]
            theme = THEMES[(m_idx + i) % len(THEMES)]
            title = f"{prefix} {theme}"
            keywords = f"{theme.replace(' ', ', ')}, Manifera, Software Development, 2027"
            
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
            snippet = f"In the rapidly evolving landscape of software engineering in 2027, {theme.lower()} has emerged as a cornerstone..."
            social_link = f"[{social_filename}](./{month}/{social_filename})"
            
            inventory_line = f"| {title} | {keywords} | Consideration | {snippet} | {social_link} |\n"
            inventory_lines.append(inventory_line)
            count += 1
            
    # Write inventory file
    inventory_path = os.path.join(BASE_DIR, "content_inventory_2027.md")
    with open(inventory_path, "w", encoding="utf-8") as f:
        f.writelines(inventory_lines)
        
    print(f"✅ Successfully generated {count} blog posts and {count} social posts across 12 months.")
    print(f"✅ Inventory saved to content_inventory_2027.md")

if __name__ == "__main__":
    main()
