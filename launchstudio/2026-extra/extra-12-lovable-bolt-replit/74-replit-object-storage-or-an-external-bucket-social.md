🚨 Freek Batenburg's Keuringsdossier lets lift and machine inspectors upload photos and signed reports from site — six companies, around 3,200 assets. Uploads went to a folder in the Replit project. It worked for four months. Then he deployed on a Tuesday afternoon, and eleven days of inspection documents — about 340 files — were simply gone. 😳

No error, nothing in any log. The database still listed every document, so the product showed 340 attachments that crashed when opened. And there was no backup. Here's where user files should actually live on Replit: 🧠

❌ Uploads written to the container's filesystem — which every deployment replaces
❌ Database backups that never included the files
❌ No type checks: the upload accepted anything
❌ Records pointing at files with nothing keeping them in step

✅ Object storage behind a single storage module, with paths (not URLs) in the database
✅ An owner-first layout — company, asset, generated file ID — in private buckets with short-lived signed URLs
✅ Type verified from file contents, 20 MB limits, and a registry recording uploader, time, path, size and type
✅ A backup of the bucket to a separate account, with a tested restore

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, files on the filesystem are one of the most common things we find when taking Replit products to production. ⚙️

His result: €2,800, three business days. About 260 of the 340 files were recovered from the companies' own copies — and uploads can no longer disappear with a deploy. 🚀

👉 Replit object storage or an external bucket: https://launchstudio.eu/en/blog/replit-object-storage-or-an-external-bucket

#Replit #ObjectStorage #FileUploads #DevOps #LaunchStudio #Manifera
