---
Title: "Realtime Features in Supabase: Chat, Presence and Live Updates"
Keywords: supabase realtime, supabase realtime security, supabase broadcast presence, realtime chat lovable app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Realtime Features in Supabase: Chat, Presence and Live Updates

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Realtime Features in Supabase: Chat, Presence and Live Updates",
  "description": "Supabase Realtime makes chat, live dashboards and presence indicators easy to add to an AI-built app, but realtime features introduce their own security and scaling questions. This guide explains Postgres Changes, Broadcast and Presence, how authorisation works for each, private channels, connection limits, cost and the patterns that keep realtime features safe and fast.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-22",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/realtime-features-in-supabase-chat-presence-and-live-updates" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase Realtime documentation", "url": "https://supabase.com/docs/guides/realtime" },
    { "@type": "CreativeWork", "name": "Supabase Realtime Authorization", "url": "https://supabase.com/docs/guides/realtime/authorization" },
    { "@type": "CreativeWork", "name": "Supabase Realtime: Postgres Changes", "url": "https://supabase.com/docs/guides/realtime/postgres-changes" },
    { "@type": "CreativeWork", "name": "Supabase Realtime limits", "url": "https://supabase.com/docs/guides/realtime/limits" }
  ]
}
</script>

Realtime features make software feel alive. A message appears the moment a colleague sends it. A dashboard updates as orders arrive. A small avatar shows who else is looking at the same document. A delivery status changes on screen without a refresh. For users, these details turn a tool from something they check into something they work in.

Supabase makes these features remarkably accessible. Ask Lovable or Bolt for "live updates" or "a chat between customer and support" and the generated code will often use Supabase Realtime within minutes. The demo works beautifully with two browser windows.

What the demo does not show is who else can listen. Realtime channels are another way data leaves your database, and they need their own authorisation. They also behave differently at scale: thousands of connected clients, frequent changes and broad subscriptions can slow the database or hit plan limits. This guide explains how Supabase Realtime works and how to use it safely.

## Key Takeaways

- **Supabase Realtime offers three features:** Postgres Changes (database change events), Broadcast (low-latency messages between clients) and Presence (who is online).
- **Postgres Changes respect Row Level Security** for subscribed clients, so weak policies leak data in realtime just as they do through the API.
- **Broadcast and Presence need explicit authorisation** through private channels and policies; public channels can be joined by anyone who knows the name.
- **Postgres Changes do not scale indefinitely.** Supabase recommends Broadcast for high-volume or high-subscriber scenarios.
- **Subscribe narrowly and unsubscribe when screens close,** to control connections, load and cost.

## The Three Realtime Features

| Feature | What it does | Typical use | Authorisation |
| --- | --- | --- | --- |
| Postgres Changes | Streams inserts, updates and deletes from tables to subscribed clients | Live dashboards, order status, new records | Row Level Security on the underlying table |
| Broadcast | Sends messages between clients via a channel, optionally from the database | Chat messages, typing indicators, cursor positions, notifications | Private channels with policies on realtime messages |
| Presence | Tracks and shares which clients are connected to a channel | Online indicators, "who is viewing" | Private channels with policies |

Choosing the right feature for each use case is the first design decision, and AI-generated code often defaults to Postgres Changes for everything.

## Postgres Changes and Row Level Security

With Postgres Changes, a client subscribes to changes on a table, optionally filtered, and receives events when rows change. For tables with Row Level Security enabled, Supabase checks whether each subscribed user is allowed to read the changed row before sending it, using the user's authentication.

That has two consequences:

1. **Security depends on your policies.** If the `messages` table has a policy that lets any authenticated user read all messages, every authenticated subscriber receives every new message in realtime. Fix the policy, and realtime is fixed too.
2. **Performance depends on your policies and subscriber count.** Each change must be checked for each subscriber. Supabase's documentation notes that Postgres Changes processes changes on a single thread to maintain order, so many subscribers and many changes can create a bottleneck. Complex policies make each check more expensive.

Also check that tables are only added to the realtime publication when needed. Adding every table "just in case" increases load and exposure.

## Broadcast and Presence: Public vs Private Channels

Broadcast and Presence work through channels identified by a name. By default, a channel is public: anyone with your project's public key who knows or guesses the channel name can join, send messages and see presence information.

For any channel carrying user data, use **private channels** with Realtime Authorization. Supabase lets you write Row Level Security policies on the realtime messages table that decide which authenticated users may read from and write to which channels. For example, a policy can allow users to join a channel named after a conversation only if they are a participant in that conversation.

Typical patterns:

- **Conversation channels:** `conversation:{id}`, allowed only for participants
- **Workspace channels:** `workspace:{id}`, allowed only for workspace members
- **User channels:** `user:{id}`, allowed only for that user, used for personal notifications

Never rely on hard-to-guess channel names as security. Names leak through URLs, logs and code.

## Designing a Secure Chat

Chat is one of the most requested realtime features in AI-built apps, and a frequent source of data leaks. A robust design:

1. **Store messages in a table** with a conversation ID and sender ID, protected by Row Level Security so only participants can read and insert.
2. **Insert messages through the API or a function** that verifies the sender is a participant, never by broadcasting directly from the client without persistence.
3. **Deliver new messages** either through Postgres Changes filtered by conversation, or by broadcasting from the database after insert to a private conversation channel.
4. **Use Broadcast for ephemeral signals** such as typing indicators, which do not need to be stored.
5. **Use Presence** for online status within the conversation's private channel.
6. **Handle reconnection** by fetching recent messages after reconnecting, since realtime events sent while a client was offline are not replayed.

The last point is easily missed. Realtime is a delivery mechanism, not a source of truth. The database remains the authority, and clients should resynchronise after connection changes.

## Scaling and Limits

Supabase publishes limits per plan for realtime, including concurrent connections, messages per second and channel joins. Practical guidance:

- **Subscribe narrowly.** Subscribe to one conversation or one workspace's changes, not to an entire table.
- **Unsubscribe when screens close.** AI-generated components sometimes subscribe in an effect without cleanup, creating duplicate subscriptions on every render or navigation.
- **Prefer Broadcast for high volume.** For features like live cursors or frequent status updates, Broadcast avoids database change processing.
- **Throttle frequent updates.** Sending a cursor position 60 times per second is rarely necessary; a few times per second is usually enough.
- **Keep payloads small.** Send IDs and changed fields rather than full records, and fetch details when needed.
- **Load test realtime paths** if many users will be connected simultaneously, for example during live events.

## Common Realtime Bugs in AI-Built Apps

| Bug | Symptom | Fix |
| --- | --- | --- |
| Subscription without cleanup | Duplicate messages, growing connections, memory leaks | Unsubscribe in effect cleanup |
| Public channel for private data | Anyone can listen to conversations | Private channels with authorisation policies |
| Permissive table policy | All users receive all changes | Tighten Row Level Security |
| Realtime as the only source of truth | Missing messages after reconnect | Refetch from database on reconnect |
| Subscribing to whole tables | High load, slow updates | Filter by conversation or workspace |
| Optimistic UI without confirmation | Messages appear sent but were rejected | Confirm insert success, show failures |
| Unthrottled broadcasts | Rate limit errors, high cost | Throttle and batch updates |

## Testing Realtime Security

Test realtime the same way you test API access:

1. Sign in as user A in one browser and user B, from a different organisation, in another.
2. From user B's browser console, try subscribing to user A's table changes and channels.
3. Create data as user A and confirm user B receives nothing.
4. Try sending a broadcast message to a channel user B should not access.
5. Repeat for each role.

Add automated tests for authorisation policies, including those on realtime messages, so future AI-generated changes cannot silently open channels.

## Live Dashboards Without Overloading the Database

Live dashboards are the second most common realtime request after chat. An operations screen that shows new orders, support tickets or deliveries as they arrive is valuable, but a naive implementation can be expensive. Typical problems include every dashboard user subscribing to every change in a large table, and each event triggering a full reload of all dashboard queries.

More efficient patterns:

- **Subscribe to a summary, not the raw table.** Broadcast a small event such as "order created for workspace X" and let clients update a counter or fetch only the new item.
- **Debounce refreshes.** If twenty orders arrive in a minute, refresh aggregates once every few seconds rather than twenty times.
- **Precompute aggregates.** Maintain counters or summary tables updated by database triggers, so dashboards read a few rows instead of scanning thousands.
- **Scope by workspace and role.** A store manager needs their store's live data, not the whole chain's.
- **Fall back to polling for low-priority panels.** Not every widget on a dashboard needs to be live.

These patterns keep the dashboard responsive for users while keeping database load roughly constant as usage grows.

## Mobile and Unstable Connections

Realtime connections behave differently on phones. Apps move to the background, networks switch between Wi-Fi and mobile data, and connections drop in trains and lifts. Design for it:

- Show a subtle connection indicator when the realtime connection is lost.
- Resynchronise state from the database when the app returns to the foreground or reconnects.
- Queue outgoing messages locally while offline and send them when the connection returns, with clear status for each message.
- Avoid assuming event order across reconnections; use timestamps or sequence numbers from the database.

## When Realtime Is Not Needed

Realtime adds complexity, connections and cost. Sometimes simpler options work just as well:

- **Polling every 30 to 60 seconds** for dashboards that do not need second-by-second updates
- **Refresh on focus,** fetching new data when the user returns to a tab
- **Email or push notifications** for events users do not need to see instantly in the app

Use realtime where immediacy changes the user experience, such as chat, collaboration and live operations, and simpler patterns elsewhere.

## How LaunchStudio Helps

LaunchStudio reviews and hardens realtime features in AI-built apps: choosing the right feature for each use case, writing Row Level Security and channel authorisation policies, converting public channels to private ones, fixing subscription leaks, implementing reconnection logic, throttling and load testing realtime paths when many users connect at once.

The **Launch Ready** package (€800-€3,500) covers security review and fixes, including realtime authorisation, alongside deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including realtime and messaging systems for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. For the broader security picture, see our guide on [Supabase RLS audits](https://launchstudio.eu/en/blog/supabase-rls-audit-the-policy-mistakes-we-find-most).

## Real example

### An AI-Native Founder in Action: The Tutoring Chat Anyone Could Listen To

Marloes Visser built Huiswerkhulp with Lovable and Supabase: a platform where secondary school students chat with volunteer tutors about homework, with a live indicator showing which tutors are online. Two schools in Overijssel piloted it, and the chat felt instant and friendly.

A parent with a technical background noticed something worrying. The chat used Broadcast on public channels named `chat-` followed by the student's first name and a number, and presence on a single public `tutors` channel exposed tutor names and the student each tutor was helping. Anyone with the app's public key could join any channel. Messages were also stored in a table whose policy let any authenticated user read all messages, so Postgres Changes subscriptions delivered every message to every logged-in user. The chat component subscribed on every render without cleanup, and messages sent while a student was briefly offline simply disappeared.

LaunchStudio rebuilt the chat so messages were inserted into a table with Row Level Security limiting access to the student, the assigned tutor and school coordinators. New messages were broadcast from the database to private conversation channels named by conversation ID, with authorisation policies requiring participation. Presence moved to private channels per school, showing tutors as available without revealing who they were helping. Typing indicators used throttled Broadcast, subscriptions were cleaned up properly, and clients refetched recent messages after reconnecting. Engineers added automated tests confirming that students from one school could not join channels from another.

**Result:** The updated chat launched before the second school term. Usage grew to six schools and around 900 students, the parent who reported the issue reviewed the fix and joined the volunteer team, and no further access issues have been reported.

> *"The chat felt magical in the demo. I hadn't realised that the magic worked just as well for people who were never supposed to see the messages."*
> - **Marloes Visser, Founder, Huiswerkhulp (Zwolle)**

**Cost & Timeline:** €3,200 (Launch Ready package: chat redesign, private channels with authorisation, RLS fixes, reconnection handling and security tests) - completed in 9 business days.

## Frequently Asked Questions

### Does Supabase Realtime respect Row Level Security?

For Postgres Changes, yes: Supabase checks whether each subscribed user may read changed rows under your policies. That means weak policies leak data in realtime too. Broadcast and Presence use channels, which need private channels and authorisation policies to be protected.

### Should I use Postgres Changes or Broadcast for chat?

Many robust chat designs store messages in a table protected by Row Level Security and deliver them either through filtered Postgres Changes or by broadcasting from the database to private channels. For high volumes or many subscribers, Broadcast tends to scale better. Ephemeral signals such as typing indicators should use Broadcast.

### How many realtime connections can my Supabase app handle?

It depends on your plan's limits and how efficiently you subscribe. Supabase publishes concurrent connection and message limits per plan. Narrow subscriptions, proper cleanup and throttled broadcasts let you serve many more users within those limits.

### How does Manifera's experience help with realtime features?

Manifera has built messaging and realtime systems for enterprise clients over 11+ years, where privacy and scale matter. LaunchStudio applies that experience to secure channels, fix subscription leaks and design realtime features that remain correct when connections drop.

### Do realtime features affect SEO or AI visibility?

Not directly, because realtime features usually live behind a login. They do improve user engagement and product quality, which leads to better reviews and recommendations. Keep public, indexable pages server-rendered and independent of realtime connections.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does Supabase Realtime respect Row Level Security?",
      "acceptedAnswer": { "@type": "Answer", "text": "For Postgres Changes yes, so weak policies leak in realtime too. Broadcast and Presence need private channels with authorisation policies." }
    },
    {
      "@type": "Question",
      "name": "Should I use Postgres Changes or Broadcast for chat?",
      "acceptedAnswer": { "@type": "Answer", "text": "Store messages in an RLS-protected table and deliver via filtered Postgres Changes or database broadcasts to private channels; Broadcast scales better at high volume." }
    },
    {
      "@type": "Question",
      "name": "How many realtime connections can my Supabase app handle?",
      "acceptedAnswer": { "@type": "Answer", "text": "It depends on plan limits and subscription efficiency. Narrow subscriptions, cleanup and throttling let you serve more users." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with realtime features?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise messaging and realtime systems for 11+ years, and LaunchStudio secures channels and fixes subscription leaks." }
    },
    {
      "@type": "Question",
      "name": "Do realtime features affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not directly, as they live behind logins, but they improve engagement and reviews. Keep public pages server-rendered." }
    }
  ]
}
</script>
