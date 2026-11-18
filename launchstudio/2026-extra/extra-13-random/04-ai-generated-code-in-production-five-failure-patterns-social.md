🤥 Five polite lies one fleet app told for four months

LIE 1: "Saved."
Photo uploads were wrapped in a silent catch. On weak mobile connections they failed, and drivers still saw "saved."

LIE 2: "Just a moment..."
The mileage sync called a vehicle-data API with no timeout. On that API's slow days, the whole app hung.

LIE 3: "No services due."
The service reminder job worked out "due this week" in the server's UTC time. Reminders for Monday services were generated on Sunday night, and filtered out as already past.

LIE 4: "Retrying."
A retry loop, added by the AI to "fix" an earlier error, kept triggering the vehicle API's rate limit, which explained the gaps in mileage data.

LIE 5: "Everything's fine."
Nothing ever crashed. So nobody looked.

Burak Aydın runs a small delivery-van leasing company in Zaandam and built FleetNote with Windsurf: drivers log mileage, fuel and damage photos from their phones, and the office tracks maintenance across 38 vans. After four months, Burak noticed two vans had missed their scheduled service. The logs, once someone read them, told the story above.

The truth, restored (LaunchStudio, 8 business days, €2,200):
✓ Silent catches replaced with reported errors, and a visible retry prompt for drivers
✓ Timeouts, and a queue for the vehicle-data sync
✓ Reminders calculated in the office's Europe/Amsterdam time zone
✓ Retries capped, with exponential backoff
✓ Sentry and uptime alerts to Burak and his office manager

The next quarter: every scheduled service recorded on time, failed photo uploads close to zero because drivers could retry them, and the vehicle-data API bill down about 40% once the retry storm was gone.

"Nothing ever crashed, which is why I trusted it. It turns out the app was failing politely and telling nobody." - Burak Aydın

https://launchstudio.eu/en/blog/ai-generated-code-in-production-five-failure-patterns

#AICoding #Windsurf #Reliability #DevOps #LaunchStudio #Manifera
