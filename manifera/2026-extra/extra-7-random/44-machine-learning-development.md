---
title: "Machine Learning Development: Why the Model Is the Easy Part and the Data Pipeline Isn't"
keywords: "machine learning development, ml development, machine learning services"
buyer_stage: "Consideration"
target_persona: "CTO"
---

# Machine Learning Development: Why the Model Is the Easy Part and the Data Pipeline Isn't

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Machine Learning Development: Why the Model Is the Easy Part and the Data Pipeline Isn't",
  "description": "A CTO's guide to why the majority of genuine machine learning development effort goes into data pipeline and feature engineering work, not model training itself.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/machine-learning-development" }
}
</script>

Well-established estimates from experienced machine learning practitioners put model training and algorithm work at a genuinely small share of total machine learning development effort, often cited around 20%, with the remaining majority consumed by data pipeline construction, feature engineering, and data quality work — a distribution most CTOs new to ML underestimate significantly when planning a first project.

**The Pain:** A CTO scoping a machine learning development project, especially one new to the specific challenges of ML work, naturally focuses planning attention on the model itself — which algorithm, which architecture, how to train and tune it — because this is the part of ML development that gets the most public attention and technical excitement, while the data pipeline work that actually consumes most of the effort is comparatively under-examined during initial scoping.

**The Agitation:** A CTO who scopes a machine learning project around model-training effort, treating data pipeline work as a smaller supporting task, discovers during implementation that building reliable, high-quality data pipelines — sourcing, cleaning, transforming, and maintaining the data a model actually depends on — consumes considerably more engineering time than model training itself, and a project scoped without this proportion in mind runs over budget and timeline specifically in the category that was least examined during planning.

## Why Data Work Dominates and How to Plan for It

Machine learning development effort is dominated by data pipeline work for structural reasons a CTO should understand before scoping a project, rather than discovering the proportion empirically after a project has already run over its data-focused planning gap.

The first structural reason is that real-world data, unlike the clean, pre-processed datasets used in academic ML examples and tutorials, arrives messy — inconsistent formats, missing values, duplicate or conflicting records, and data spread across multiple source systems that were never designed with machine learning consumption in mind. Cleaning and reconciling this data into a form a model can actually train on reliably is substantial, company-specific engineering work that has no shortcut and doesn't get easier regardless of which model or algorithm is eventually chosen.

The second structural reason is that feature engineering — transforming raw data into the specific inputs a model actually uses, often requiring genuine domain knowledge about which transformations and combinations of raw data are likely to be predictive — is a deep, iterative, company-specific effort that consumes considerably more time than the actual model training step, which for many well-established problem types is comparatively fast once quality features and training data are ready.

The third structural reason is that the pipeline delivering data to a model in production needs to be genuinely reliable and maintainable on an ongoing basis, not just a one-time script that produced training data once — a production ML pipeline needs to handle new data arriving continuously, detect and handle data quality issues as they emerge, and remain maintainable as underlying source systems evolve, which is meaningfully more engineering effort than a one-time data preparation exercise for an initial training run.

A CTO scoping machine learning development should explicitly plan for this distribution — allocating the clear majority of project time and budget to data pipeline and feature engineering work, with model training and tuning treated as a comparatively smaller, later-stage effort — and should specifically resist a natural planning instinct to treat data preparation as a quick preliminary step before the "real" ML work begins, since for most genuine ML projects, the data work is the real work.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch leads scope machine learning development projects with proper weight on data pipeline and feature engineering effort, rather than concentrating planning attention on model training alone.
- **Vietnam (Execution/Velocity):** Autonomous pods in Ho Chi Minh City build the reliable, maintainable data pipelines that determine whether a machine learning model actually performs well in production, not just in an initial training run.

This is Dutch Management × Vietnamese Mastery: European rigor in scoping where genuine machine learning effort belongs, paired with execution capacity that builds the data foundation a model's real-world performance depends on. Learn more about [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/) and how properly scoped machine learning development avoids underestimating the data work that actually determines project success.

## Case Study & Testimonial

### A Brno Manufacturer's Data-Underestimated ML Project

Výrobní Systémy Brno a.s., a Brno-based manufacturer, had scoped a predictive-maintenance machine learning project around model-selection and training effort, budgeting a small fraction of the timeline for data preparation, only to discover the sensor data feeding the model was scattered across incompatible legacy systems requiring several months of pipeline work before any model training could genuinely begin.

Manifera's subsequent scoping for the company's next ML initiative allocated roughly 70% of the project timeline explicitly to data pipeline and feature engineering work upfront, with model training treated as a smaller, later phase. The project delivered within its revised estimate, with no mid-project data-related surprises.

> *"We planned like the model was the project and the data was a preliminary step. It turned out the data was almost the whole project. Once we planned it that way from the start, we stopped being surprised by how long everything was taking."*
> — **CTO, Výrobní Systémy Brno a.s., Czech Republic**

## Model-Focused Scoping vs. Manifera's Data-Weighted ML Scoping

| Criteria | Model-Focused Scoping | Manifera's Data-Weighted ML Scoping |
|---|---|---|
| Primary planning focus | Model selection, training, and tuning | Data pipeline and feature engineering |
| Data preparation treatment | Small preliminary step | Majority of project time and budget |
| Production pipeline reliability | Assumed a one-time preparation task | Built as ongoing, maintainable infrastructure |
| Typical effort distribution assumed | Model-heavy | Roughly 80% data work, 20% model work |
| Estimate accuracy | Frequently underestimates data-related timeline | Matches actual implementation effort |

## The Economics

A CTO who scopes machine learning development around model training effort, treating data pipeline work as a smaller supporting task, discovers during implementation that data work consumes considerably more time than planned, since well-established industry estimates put model training at roughly 20% of genuine ML development effort, with data pipeline and feature engineering consuming the remaining majority. Scoping with this proportion in mind from the start costs nothing beyond an accurately weighted project plan. [Talk to Manifera](https://www.manifera.com/contact-us/) about machine learning development scoped around where the real effort actually lives.

## Frequently Asked Questions

### (Scenario: CTO scoping a machine learning project around model-training effort) What share of genuine machine learning development effort typically goes into model training versus data work?

Well-established industry estimates put model training at roughly 20% of total effort, with data pipeline construction and feature engineering consuming the remaining majority.

### (Scenario: CTO trying to understand why real-world data requires so much preparation) Why does real-world data require substantially more preparation than academic ML datasets?

Because it arrives messy — inconsistent formats, missing values, duplicate records, and data spread across incompatible source systems never designed for ML consumption.

### (Scenario: CTO trying to understand what feature engineering involves) What is feature engineering, and why does it consume significant machine learning development time?

Transforming raw data into the specific inputs a model uses, often requiring genuine domain knowledge to determine which transformations are likely to be predictive.

### (Scenario: CTO planning a production machine learning pipeline) Why does a production ML data pipeline require more effort than a one-time training data preparation exercise?

Because it needs to handle continuously arriving data, detect data quality issues as they emerge, and remain maintainable as source systems evolve.

### (Scenario: CTO trying to scope a machine learning project accurately) How should a CTO allocate planning effort across a machine learning development project?

The clear majority toward data pipeline and feature engineering work, with model training and tuning treated as a smaller, later-stage effort.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO scoping a machine learning project around model-training effort) What share of genuine machine learning development effort typically goes into model training versus data work?", "acceptedAnswer": { "@type": "Answer", "text": "Roughly 20% model training, with data pipeline and feature engineering consuming the remaining majority." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to understand why real-world data requires so much preparation) Why does real-world data require substantially more preparation than academic ML datasets?", "acceptedAnswer": { "@type": "Answer", "text": "It arrives messy, spread across incompatible source systems never designed for ML consumption." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to understand what feature engineering involves) What is feature engineering, and why does it consume significant machine learning development time?", "acceptedAnswer": { "@type": "Answer", "text": "Transforming raw data into predictive model inputs, requiring genuine domain knowledge." } },
    { "@type": "Question", "name": "(Scenario: CTO planning a production machine learning pipeline) Why does a production ML data pipeline require more effort than a one-time training data preparation exercise?", "acceptedAnswer": { "@type": "Answer", "text": "It must handle continuously arriving data and remain maintainable as source systems evolve." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to scope a machine learning project accurately) How should a CTO allocate planning effort across a machine learning development project?", "acceptedAnswer": { "@type": "Answer", "text": "The clear majority toward data pipeline and feature engineering, with model training as a smaller later phase." } }
  ]
}
</script>
