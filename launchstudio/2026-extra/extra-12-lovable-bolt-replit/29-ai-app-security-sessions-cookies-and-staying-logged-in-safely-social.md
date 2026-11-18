☑️ LEAVER CHECKLIST, as the organisation did it

☑ Account removed on her last day
☐ Active sessions ended
☐ Refresh token invalidated
☐ Her tablet signed out

Everyone in the room believed the first box was enough. Her tablet kept working for three weeks. 🏠

Roos Verhagen built Zorgplanning in Lovable: shift planning and client scheduling for home care organisations, 18 organisations, around 900 carers. A planner at one organisation left after a disagreement. The manager removed her account on her last day and considered it closed.

Three weeks later, unexplained changes appeared in the schedule: shifts reassigned overnight, two client visits removed. The former planner's tablet still had the app open, with a valid session. Her last refresh token had a 90-day lifetime, and deleting the account row hadn't invalidated it. The browser kept refreshing access tokens against a user that no longer existed, and the app, which checked the token and not the account, kept saying yes.

The full checklist, built in (LaunchStudio, 2 business days, €2,700):
✓ Session tokens moved from local storage to httpOnly, secure, sameSite cookies, with CSRF tokens on state-changing requests
✓ A sessions table recording every active session, with device, last use and approximate location
✓ Deactivating an account, or changing a password, now ends all sessions immediately
✓ "Sign out everywhere" for users, and force sign-out for organisation admins, so they can end a leaver's access themselves
✓ Access tokens of 30 minutes and a 14-day refresh lifetime, chosen with the organisations, plus a 12-hour idle timeout for shared tablets in care locations
✓ Sign-out that invalidates on the server and clears the client data cache, which used to show the previous user's client list for a second
✓ Session rotation at login
✓ A visible active-sessions screen

The unauthorised changes were reconstructed from the audit trail and corrected, and the organisation reported the incident internally as required. Since then, three organisations have used the active-sessions screen to find tablets left signed in at client locations, a problem none of them knew they had.

"We deleted her account. Everyone in the room believed that meant she was out. Her tablet kept working for three weeks." - Roos Verhagen

https://launchstudio.eu/en/blog/ai-app-security-sessions-cookies-and-staying-logged-in-safely

#AppSecurity #Authentication #HealthTech #Lovable #LaunchStudio #Manifera
