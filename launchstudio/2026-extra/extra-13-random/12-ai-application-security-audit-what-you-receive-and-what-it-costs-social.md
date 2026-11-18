🔍 Three ways to check a pet-sitting marketplace. What each would have told you.

                                 Automated scan   Focused review    Penetration test
Price                            €450             €950              €14,000
Exposed service key              ✓ found          ✓ found           (not chosen)
Two missing headers              ✓ found          ✓ found
Sitters reading any pet's
medical notes                    ✗ missed         ✓ found
Message threads open by
changing an ID                   ✗ missed         ✓ found
Total findings                   3                13 (3 critical,
                                                  6 medium, 4 low)

Eline Rademaker, a veterinary nurse in Apeldoorn, built Huisdierpas in Lovable: a marketplace connecting pet owners with vetted local sitters, with profiles, booking requests, messaging, and pet medical notes so sitters know about allergies and medication. Before launching beyond her pilot group of 40 owners, she collected quotes: a €450 scan and a €14,000 penetration test.

She chose the middle option: a LaunchStudio focused review for €950, delivered in three days. The three critical findings:
🔴 Sitters could read medical notes for any pet on the platform, not just pets they had bookings with
🔴 Message threads were accessible by changing a conversation ID
🔴 A Supabase service key with full database access sat in the frontend bundle

She ran the scan too, for comparison. It caught the key and two headers. None of the access-control issues.

Then the fixed-price follow-up (7 business days, €1,800):
✓ Row Level Security tying medical notes to active bookings
✓ Participant checks on messaging
✓ The service key rotated and removed from the frontend
✓ Rate limiting on login, and upload restrictions
✓ A re-test, documented in an updated report

Total: €2,750. Huisdierpas launched across Gelderland and reached 520 owners and 85 sitters in four months. When a regional pet insurer asked about data protection, Eline sent the re-test report, and the partnership went ahead.

"The cheap scan would have told me I was mostly fine. The review told me sitters could read every pet's medical history. Those are very different reports." - Eline Rademaker

https://launchstudio.eu/en/blog/ai-application-security-audit-what-you-receive-and-what-it-costs

#AppSecurity #Lovable #SecurityAudit #Startups #LaunchStudio #Manifera
