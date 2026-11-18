🚛 MORNING SHIFT REPORT: three warehouses in the Rotterdam port area

⚠️ Dock bookings: two or three double bookings a week. Trucks waiting at occupied docks.
⚠️ Live board: polling the database every two seconds from every open screen. The whole app slows at peak.
⚠️ Gate tablets: Wi-Fi lost near the steel doors. Check-ins entered there disappear.
⚠️ Shipper integration: a large shipper's TMS calls in synchronously. When it slows down, so does everything.
⚠️ Disputes: a carrier challenges a demurrage charge. No record of who moved their slot.

Samira El Amrani spent eight years as a warehouse operations manager in the Rotterdam port area before building DockSlot in Lovable: carriers book unloading slots, gate staff check trucks in on a tablet, and planners see a live board of every dock. Three warehouses in the Waalhaven and Maasvlakte areas use it, with about 60 planners and gate staff and several hundred carrier accounts.

In a warehouse, "usually correct" means wrong.

The next shift report (LaunchStudio, Launch & Grow, 18 business days, €5,600, plus €49/month):
✅ Dock bookings: a database exclusion constraint makes overlapping bookings impossible
✅ Live board: filtered real-time subscriptions, scoped to each user's warehouse
✅ Gate tablets: offline queuing for check-ins, with clear pending indicators
✅ Shipper integration: behind a message queue, with retries and idempotency
✅ Disputes: an append-only audit log for bookings and check-ins
✅ Monitoring, alerting and a documented incident process, supporting a 99.5% availability commitment in Samira's contracts
✅ The Lovable interface: preserved throughout

Double bookings dropped to zero. Database load at the morning peak fell by roughly 70%. And DockSlot signed two more warehouses, one of which required the audit log and the availability commitment as a contract condition.

"In a warehouse, 'usually correct' is the same as wrong. The fixes weren't glamorous, but they made the software as reliable as the people using it." - Samira El Amrani

https://launchstudio.eu/en/blog/productionize-an-ai-app-in-rotterdam-logistics-and-real-time-data

#Logistics #Rotterdam #SupplyChain #Lovable #LaunchStudio #Manifera
