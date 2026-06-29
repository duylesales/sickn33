import os
import re

BASE_DIR = "/Users/duynode/Library/Mobile Documents/com~apple~CloudDocs/sickn33/manifera"

MONTHS = [
    "january-2027", "february-2027", "march-2027", "april-2027",
    "may-2027", "june-2027", "july-2027", "august-2027",
    "september-2027", "october-2027", "november-2027", "december-2027"
]

INDUSTRIES = [
    "FinTech startups",
    "HealthTech applications",
    "Logistics & Supply Chain platforms",
    "Retail & eCommerce brands",
    "B2B SaaS companies",
    "Manufacturing enterprises",
    "EdTech platforms",
    "PropTech platforms",
    "CleanTech initiatives",
    "Travel & Hospitality apps"
]

PREFIXES = [
    "How to Implement",
    "5 Strategies for",
    "Future Trends in",
    "Cost Analysis of",
    "Security Best Practices for",
    "Why CTOs Choose",
    "Common Mistakes in",
    "A Strategic Approach to",
    "Understanding the ROI of",
    "The Ultimate Guide to"
]

MONTHLY_DATA = {
    "january-2027": {
        "theme": "Dedicated Remote Engineering Teams",
        "sub_topics": [
            "Setting up dedicated remote development teams",
            "Cost optimization of remote teams vs local hiring",
            "Security and IP protection in remote environments",
            "Cultural integration and timezone management",
            "Agile workflows and daily communication tools",
            "Measuring performance and KPI tracking of remote units"
        ]
    },
    "february-2027": {
        "theme": "Modern Laravel Architecture & Enterprise Web Apps",
        "sub_topics": [
            "Designing scalable Laravel microservices and API gateways",
            "Optimizing database performance and query caching in Laravel",
            "Securing enterprise Laravel applications from vulnerabilities",
            "Integrating custom third-party APIs and webhooks in Laravel",
            "Automating testing and CI/CD pipelines for Laravel",
            "Migrating monolithic Laravel applications to serverless runtimes"
        ]
    },
    "march-2027": {
        "theme": "B2B eCommerce Systems & Magento Custom Integration",
        "sub_topics": [
            "Custom Magento architecture and performance optimization",
            "Integrating ERP and inventory management with Magento",
            "Designing custom B2B wholesale checkout and credit flows",
            "Handling massive product catalogs and multi-tenant stores",
            "Magento security best practices and patch management",
            "Comparing custom headless Magento vs Shopify Plus ROI"
        ]
    },
    "april-2027": {
        "theme": "Mobile App Development with React Native and Flutter",
        "sub_topics": [
            "Choosing between React Native and Flutter for B2B mobile apps",
            "Optimizing performance and reducing app bundle size",
            "Implementing secure offline-first data sync in mobile apps",
            "Integrating biometric authentication and push notifications",
            "Automating app store deployment pipelines (CI/CD)",
            "Managing cross-platform UI components and responsive design"
        ]
    },
    "may-2027": {
        "theme": "DevOps, Cloud Infrastructure & Kubernetes",
        "sub_topics": [
            "Designing secure AWS and Azure cloud environments",
            "Implementing Docker containerization and Kubernetes orchestration",
            "Setting up zero-downtime deployment pipelines",
            "Monitoring application performance and error logging",
            "Optimizing cloud hosting costs and serverless utilization",
            "Disaster recovery and automated database backup strategies"
        ]
    },
    "june-2027": {
        "theme": "Quality Assurance, Test Automation & Code Security",
        "sub_topics": [
            "Designing automated E2E and unit testing frameworks",
            "Implementing continuous security scanning in CI/CD pipelines",
            "Conducting comprehensive code audits and resolving tech debt",
            "Manual vs automated testing resource allocation",
            "Load testing and performance benchmarking of web APIs",
            "Ensuring high test coverage for mission-critical logic"
        ]
    },
    "july-2027": {
        "theme": "Cross-Border Development Models",
        "sub_topics": [
            "Leveraging the Netherlands-Vietnam software development model",
            "Effective communication strategies across geographic hubs",
            "Managing remote agile sprints and sprint planning",
            "Mitigating risks in offshore software outsourcing",
            "Onboarding offshore developers into existing codebases",
            "Building long-term retention in remote tech teams"
        ]
    },
    "august-2027": {
        "theme": "Legacy System Modernization & Software Refactoring",
        "sub_topics": [
            "Formulating a legacy system migration roadmap",
            "Refactoring technical debt without interrupting services",
            "Decomposing legacy monoliths into modern microservices",
            "Database schema refactoring and data migration strategies",
            "API-enabling legacy backend applications",
            "Evaluating the ROI of rebuilding vs refactoring code"
        ]
    },
    "september-2027": {
        "theme": "GDPR Compliance, Data Sovereignty & European Cloud Hosting",
        "sub_topics": [
            "Designing software systems for GDPR compliance",
            "Implementing data masking and PII redaction pipelines",
            "Ensuring data sovereignty with European cloud providers",
            "Building secure tenant data isolation structures",
            "Automating user data deletion and right-to-be-forgotten requests",
            "Securing database backups and audit logging"
        ]
    },
    "october-2027": {
        "theme": "AI Integration, Machine Learning & Process Automation",
        "sub_topics": [
            "Integrating LLM APIs securely into B2B business workflows",
            "Building custom Retrieval-Augmented Generation (RAG) pipelines",
            "Managing AI API call costs and rate limiting",
            "Designing user-friendly AI chat and generative UIs",
            "Automating data extraction and document processing with AI",
            "Ensuring data privacy when training or fine-tuning models"
        ]
    },
    "november-2027": {
        "theme": "Custom Software Development vs Off-the-Shelf SaaS",
        "sub_topics": [
            "Evaluating when to build custom software vs buy SaaS",
            "Calculating the total cost of ownership (TCO) of software",
            "Designing bespoke custom software for proprietary workflows",
            "Avoiding vendor lock-in with custom open-source stacks",
            "Scaling custom platforms alongside business growth",
            "Structuring maintenance and support agreements for custom code"
        ]
    },
    "december-2027": {
        "theme": "Managing Technical Debt & Software Lifecycle Planning",
        "sub_topics": [
            "Identifying and prioritizing technical debt in codebases",
            "Aligning business goals with engineering roadmaps",
            "Budgeting for software maintenance and infrastructure updates",
            "Conducting end-of-year software architecture reviews",
            "Planning resource allocation and talent scaling for 2028",
            "Documenting software architecture and onboarding materials"
        ]
    }
}

def make_title(prefix, sub_topic, industry):
    s_clean = sub_topic[0].lower() + sub_topic[1:]
    proper_nouns = ["Laravel", "Magento", "React", "Flutter", "DevOps", "AWS", "Azure", "GDPR", "PII", "LLM", "AI", "ERP"]
    for pn in proper_nouns:
        if sub_topic.startswith(pn):
            s_clean = sub_topic
            break
            
    if prefix.endswith("for") or prefix.endswith("of") or prefix.endswith("to"):
        title = f"{prefix} {s_clean} in {industry}"
    elif prefix.endswith("in"):
        title = f"{prefix} {s_clean} for {industry}"
    else:
        if "Choose" in prefix:
            title = f"{prefix} {s_clean} for {industry}"
        elif "Mistakes" in prefix:
            title = f"{prefix} {s_clean} in {industry}"
        else:
            title = f"{prefix} {s_clean} for {industry}"
            
    title = title.replace("in in ", "in ")
    title = title.replace("for for ", "for ")
    title = title.replace("in for ", "in ")
    title = title.replace("for in ", "for ")
    
    title = title[0].upper() + title[1:]
    return title

def get_industry_context(industry):
    contexts = {
        "FinTech startups": "Where data security, regulatory compliance (like PCI-DSS), and sub-millisecond transaction speeds are absolute table stakes.",
        "HealthTech applications": "Faced with strict HIPAA and GDPR privacy laws, where data encryption and high availability save lives.",
        "Logistics & Supply Chain platforms": "Operating in complex, high-concurrency environments requiring real-time tracking and deep ERP integrations.",
        "Retail & eCommerce brands": "Driven by seasonal traffic spikes, payment gateway reliability, and seamless multi-channel user experiences.",
        "B2B SaaS companies": "Focussed on multi-tenant tenant isolation, API scalability, and zero-downtime deployment pipelines.",
        "Manufacturing enterprises": "Requiring robust integrations with physical IoT systems, legacy ERPs, and automated inventory systems.",
        "EdTech platforms": "Needing high concurrent video streaming, interactive user states, and scalable student databases.",
        "PropTech platforms": "Dependent on geospatial queries, high-fidelity photo rendering, and multi-sided marketplace checkout flows.",
        "CleanTech initiatives": "Processing massive datasets for environmental modeling, requiring optimized cost-to-compute ratios.",
        "Travel & Hospitality apps": "Relying on complex booking state machines, real-time availability sync, and localized translation layers."
    }
    return contexts.get(industry, "Where engineering excellence and resource flexibility directly dictate market success.")

def get_subtopic_actions(sub_topic):
    sub_lower = sub_topic.lower()
    if "cost" in sub_lower or "roi" in sub_lower or "budget" in sub_lower:
        return [
            "**Track Resource Utilization:** Set up detailed cost tracking for cloud hosting, third-party APIs, and compute resource spend.",
            "**Identify Wastage:** Periodically audit unused serverless execution time, oversized databases, and redundant environments.",
            "**Leverage Cost-Effective Talent:** Balance your core in-house architect team with a dedicated remote team in Vietnam to optimize cost-per-feature."
        ]
    elif "security" in sub_lower or "compliant" in sub_lower or "gdpr" in sub_lower or "pii" in sub_lower:
        return [
            "**Implement Zero-Trust Access:** Restrict database access and require multi-factor authentication (MFA) for all staging and production environments.",
            "**Automate Vulnerability Scanning:** Integrate security scanning tools directly into the CI/CD pipeline to catch vulnerabilities pre-commit.",
            "**Define Data Ownership:** Ensure clear contracts are in place regarding IP rights and tenant data isolation in shared databases."
        ]
    elif "laravel" in sub_lower:
        return [
            "**Leverage Database Caching:** Implement Redis caching for heavy queries to drastically reduce load on the primary Postgres server.",
            "**Adopt Job Queues:** Offload long-running tasks (like PDF generation or email delivery) to background queues using Laravel Horizon.",
            "**Enforce Strong Typing:** Utilize strict PHP 8.x typing and PHPStan static analysis to prevent runtime errors."
        ]
    elif "magento" in sub_lower or "ecommerce" in sub_lower:
        return [
            "**Optimize Indexing:** Set up automated cron jobs to rebuild Magento indices frequently and prevent front-end lag.",
            "**Integrate ERP Pipelines:** Ensure all ERP connections use queue-based middleware rather than synchronous HTTP requests to prevent timeouts.",
            "**Implement Varnish Cache:** Use Varnish Cache to serve static pages and product listings with sub-100ms response times."
        ]
    elif "devops" in sub_lower or "deployment" in sub_lower or "cloud" in sub_lower:
        return [
            "**Infrastructure as Code (IaC):** Use Terraform or Ansible to version control and provision infrastructure predictably.",
            "**Blue-Green Deployments:** Set up automated routing to switch traffic seamlessly between staging and production instances.",
            "**Consolidate Logging:** Direct application logs to a centralized platform like Datadog or Logrocket for rapid troubleshooting."
        ]
    elif "testing" in sub_lower or "qa" in sub_lower or "audit" in sub_lower:
        return [
            "**Define Test Coverage Goals:** Target at least 80% coverage on core business logic and critical payment code paths.",
            "**Automate E2E Journeys:** Use Playwright or Cypress to run end-to-end user checks on every pull request.",
            "**Establish a Bug-Triage SLA:** Define clear response times for critical, high, and low priority bugs found in production."
        ]
    elif "mobile" in sub_lower or "react native" in sub_lower or "flutter" in sub_lower:
        return [
            "**Implement Offline-First Logic:** Design local SQLite databases to cache user inputs and sync them once connectivity is restored.",
            "**Audit Third-Party Packages:** Regularly scan npm/pub.dev packages to avoid bloat and secure dependencies.",
            "**Optimize Asset Delivery:** Compress images and lazy-load remote assets to reduce initial app download sizes."
        ]
    elif "team" in sub_lower or "remote" in sub_lower or "outsourcing" in sub_lower or "offshore" in sub_lower:
        return [
            "**Establish Communication Standards:** Use Slack for asynchronous communication and set up daily 15-minute stand-ups for sync.",
            "**Perform Technical Onboarding:** Create a comprehensive onboarding guide including repository setups and mock data sets.",
            "**Foster Culture Inclusion:** Treat remote engineers as full members of the core team, inviting them to strategic tech meetings."
        ]
    elif "ai" in sub_lower or "machine learning" in sub_lower or "llm" in sub_lower:
        return [
            "**Handle Rate Limiting Gracefully:** Set up Redis-based queues to throttle LLM API calls and avoid API quota exhaustion.",
            "**Redact PII Pre-flight:** Implement data masking to ensure personal identifiable information is never sent to third-party AI models.",
            "**Optimize UI Perceived Speed:** Utilize server-sent events (SSE) to stream text responses token-by-token for a slower feel."
        ]
    
    return [
        "**Establish Clear Governance:** Set up strict code review rules and access management controls from day one.",
        "**Optimize Infrastructure:** Monitor CPU, database query performance, and memory consumption to minimize latency.",
        "**Ensure Compliance:** Review all data flow patterns to guarantee compliance with regional regulations (GDPR/HIPAA)."
    ]

def generate_social_post(title, industry, sub_topic):
    emoji = "🚀"
    title_lower = title.lower()
    if "ai" in title_lower or "llm" in title_lower or "machine learning" in title_lower: emoji = "🤖"
    elif "data" in title_lower or "database" in title_lower or "postgres" in title_lower: emoji = "🗄️"
    elif "price" in title_lower or "cost" in title_lower or "roi" in title_lower: emoji = "💸"
    elif "security" in title_lower or "compliance" in title_lower or "gdpr" in title_lower: emoji = "🔒"
    elif "scale" in title_lower or "devops" in title_lower or "kubernetes" in title_lower: emoji = "📈"
    elif "offshore" in title_lower or "remote" in title_lower or "team" in title_lower: emoji = "👨‍💻"
    elif "app" in title_lower or "mobile" in title_lower: emoji = "📱"

    post = f"{emoji} {title}\n\n"
    post += f"For {industry}, technical choices directly impact business growth. When it comes to {sub_topic.lower()}, there is no room for compromise.\n\n"
    post += "Our engineering team at Manifera has compiled the essential considerations and best practices to help you execute this strategy seamlessly.\n\n"
    post += "Read the full technical breakdown here: [Link]\n\n"
    post += "#SoftwareDevelopment #TechLeadership #Manifera"
    return post

def generate_blog_content(title, keywords, theme, sub_topic, industry):
    context = get_industry_context(industry)
    actions = get_subtopic_actions(sub_topic)
    
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
  "description": "A detailed analysis of {sub_topic.lower()} for {industry} in 2027.",
  "image": "",
  "author": {{
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://manifera.com"
  }}
}}
</script>

In the highly competitive landscape of {industry} in 2027, the ability to build and scale robust software infrastructure is a critical differentiator. {context}

Implementing {sub_topic.lower()} requires a strong alignment between business goals and technical execution. As a CTO or tech leader, you must balance immediate feature delivery with long-term architecture stability to prevent technical debt from slowing your roadmap.

## Why it Matters

Failing to establish high engineering standards early in the project leads to major scalability bottlenecks. This guide breaks down the core execution steps required to successfully handle {sub_topic.lower()} for your product.

### Strategic Execution Steps

To ensure success, engineering managers should focus on the following core areas:

1. {actions[0]}
2. {actions[1]}
3. {actions[2]}

## Partnering for Scale

At Manifera, we help European and global firms scale their engineering capacity by integrating dedicated offshore software development teams from our Vietnam development center. By combining local architectural guidance with flexible remote development, we ensure your product scales reliably while reducing operational costs by up to 45%.
"""
    return content

def main():
    inventory_lines = [
        "<style>\n",
        "  body {\n",
        "    font-size: 36% !important;\n",
        "  }\n",
        "  table, th, td {\n",
        "    white-space: nowrap !important;\n",
        "    word-break: keep-all !important;\n",
        "    overflow-wrap: normal !important;\n",
        "  }\n",
        "</style>\n\n",
        "# 📚 Bảng Tổng Hợp Content Manifera 2027\n"
    ]
    
    count = 0
    for m_idx, month in enumerate(MONTHS):
        dir_path = os.path.join(BASE_DIR, month)
        os.makedirs(dir_path, exist_ok=True)
        
        month_data = MONTHLY_DATA[month]
        theme = month_data["theme"]
        sub_topics = month_data["sub_topics"]
        
        # Monthly section in inventory
        inventory_lines.append(f"\n## Tháng: {month.replace('-', ' ').title()}\n\n")
        inventory_lines.append("| STT | Tiêu đề (Title) | Từ khóa (Keywords) | Giai đoạn (Buyer Stage) | Bài viết (Article) | Đoạn trích (Snippet) | Bài Social Media |\n")
        inventory_lines.append("|---|---|---|---|---|---|---|\n")
        
        # We need exactly 60 articles.
        # Loop sub_topics (6) and industries (10). 6 * 10 = 60 unique articles.
        article_num = 1
        for s_idx, sub_topic in enumerate(sub_topics):
            for ind_idx, industry in enumerate(INDUSTRIES):
                prefix = PREFIXES[ind_idx] # Vary prefixes based on industry index
                title = make_title(prefix, sub_topic, industry)
                
                clean_theme = theme.replace("&", "and").replace(",", "")
                keywords = f"{clean_theme}, {sub_topic}, {industry}, Manifera, 2027"
                
                # File names
                base_filename = f"{article_num:02d}-{title.lower().replace(' ', '-').replace(':', '').replace('&', 'and').replace(',', '').replace('/', '-')}"
                # Limit length of filename if too long
                if len(base_filename) > 100:
                    base_filename = base_filename[:100].rstrip('-')
                
                blog_filename = f"{base_filename}.md"
                social_filename = f"{base_filename}-social.md"
                
                # Generate contents
                blog_content = generate_blog_content(title, keywords, theme, sub_topic, industry)
                social_content = generate_social_post(title, industry, sub_topic)
                
                # Write blog file
                with open(os.path.join(dir_path, blog_filename), "w", encoding="utf-8") as f:
                    f.write(blog_content)
                    
                # Write social file
                with open(os.path.join(dir_path, social_filename), "w", encoding="utf-8") as f:
                    f.write(social_content)
                    
                # Inventory entry
                snippet = f"A detailed analysis of {sub_topic.lower()} for {industry} in 2027."
                blog_link = f"[{blog_filename}](./{month}/{blog_filename})"
                social_link = f"[{social_filename}](./{month}/{social_filename})"
                
                inventory_line = f"| {article_num} | {title} | {keywords} | Consideration | {blog_link} | {snippet} | {social_link} |\n"
                inventory_lines.append(inventory_line)
                
                article_num += 1
                count += 1
                
        print(f"Generated {article_num - 1} articles for {month}")
            
    # Write inventory file
    inventory_path = os.path.join(BASE_DIR, "content_inventory_2027.md")
    with open(inventory_path, "w", encoding="utf-8") as f:
        f.writelines(inventory_lines)
        
    print(f"\n✅ Successfully generated {count} unique blog posts and social posts across 12 months.")
    print(f"✅ Inventory saved to content_inventory_2027.md")

if __name__ == "__main__":
    main()
