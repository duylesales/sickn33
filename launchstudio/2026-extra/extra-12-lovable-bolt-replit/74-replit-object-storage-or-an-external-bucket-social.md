📢 LOST

340 files: inspection photographs and signed reports
Last seen: a folder inside the project
Disappeared: on a Tuesday afternoon, during a deployment
Missing for: eleven days' worth of uploads
Symptoms: the database still lists all 340, attached to inspections. Open one and you get an error.
Backup: none. The database backup held only the database.

Freek Batenburg built Keuringsdossier on Replit: inspection documentation for six lift and machine inspection companies, around 3,200 assets. Engineers upload photos and signed reports from site. Uploads went to a project folder, and it worked through development and four months of use, because he hadn't redeployed while anyone was uploading. The deployment replaced the instance, and the filesystem went with it. 🏗️

FOUND (partly)
The 340 files were identified from database records, and the six companies were asked to re-upload what they still had. About 260 came back. Roughly 80 were permanently lost, and for two assets the inspection had to be repeated, at a cost the companies absorbed.

SO IT CAN'T HAPPEN AGAIN (LaunchStudio, 3 business days, €2,800)
✓ Object storage, using the platform's own, since none of the residency, portability or scale reasons for an external bucket applied
✓ All file access behind one storage module, with the database storing paths, not URLs, so changing provider later is just configuration
✓ Paths laid out owner-first: company, asset, generated file ID
✓ Private buckets, with signed URLs generated server-side: fifteen minutes to view, an hour to download
✓ File types checked from contents (anything had been accepted before), with a 20 MB limit
✓ A file registry recording uploader, time, path, size and type
✓ Deleting a record now removes its objects too
✓ A backup of the bucket to a separate account, with a tested restore

Freek had no idea the filesystem was temporary, and nothing in four months of successful operation suggested it.

"It had worked for four months. Then I deployed on a Tuesday and eleven days of inspection photographs simply were not there any more, with no error and nothing in any log." - Freek Batenburg

https://launchstudio.eu/en/blog/replit-object-storage-or-an-external-bucket

#Replit #ObjectStorage #FileUploads #DevOps #LaunchStudio #Manifera
