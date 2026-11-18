🧮 The cost of not caching, in one sum

1 popular harbour
× 20,000 page views a day
× 1 weather API call per page view
× 1 tide service call per page view
for data that changes hourly
= over €900 in one month, plus rate-limit errors on sunny weekends

Noah Bos, a sailing instructor in Den Helder, built Getijdenwijzer in Bolt: sailors and fishermen see tides, wind and current forecasts for harbours along the Wadden Sea and North Sea coast, with alerts for favourable conditions. A mention in a sailing magazine brought 6,000 users in one spring month. He was paying for the same forecast twenty thousand times a day.

And one attempt to speed things up had gone wrong: a personal "my alerts" page was cached at the CDN, briefly showing some users another sailor's saved harbours, and the phone number used for SMS alerts.

The new sum (LaunchStudio, 6 business days, €1,650):

FIRST, the privacy fix
✓ All per-user responses marked private, and the CDN purged

THEN, the cost fix
1 forecast per harbour, cached on the server
÷ expiry matched to each source's update interval
+ alert conditions pre-computed in a scheduled job, not on every page view
+ short-lived CDN caching for public harbour pages
+ monitoring on API usage and cost
= about 97% fewer API calls

The monthly bill dropped to around €40, while users kept growing. Rate-limit errors disappeared, and harbour pages load in well under a second, even on the first sunny Saturday of the season.

"I was paying for the same forecast twenty thousand times a day. Caching felt like a technical detail until I saw it on an invoice." - Noah Bos

https://launchstudio.eu/en/blog/ai-application-scalability-caching-explained-for-non-technical-founders

#Caching #Scalability #APIcosts #Bolt #LaunchStudio #Manifera
