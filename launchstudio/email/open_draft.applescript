-- Mo email HTML thanh DRAFT trong Apple Mail — co nut Send, khong co "RE:"
-- Dung:  osascript open_draft.applescript <file.html> [email-nguoi-nhan]
-- Hoac:  mo file nay bang Script Editor roi bam ▶ (se dung file NL mac dinh)

on run argv
	set folderPath to (do shell script "cd " & quoted form of (POSIX path of ((path to me as text))) & "/.. 2>/dev/null; pwd") 
	if (count of argv) > 0 then
		set htmlPath to item 1 of argv
	else
		set htmlPath to "/Users/duyle/sickn33/launchstudio/email/launchstudio_email_nl.html"
	end if
	if (count of argv) > 1 then
		set recipientAddr to item 2 of argv
	else
		set recipientAddr to ""
	end if

	-- doc file HTML nguyen ven (utf8)
	set theHTML to do shell script "cat " & quoted form of htmlPath
	-- lay subject tu <title>
	set theSubject to do shell script "sed -n 's|.*<title>\\(.*\\)</title>.*|\\1|p' " & quoted form of htmlPath & " | head -1"
	if theSubject is "" then set theSubject to "LaunchStudio"

	tell application "Mail"
		activate
		set msg to make new outgoing message with properties {subject:theSubject, html content:theHTML, visible:true}
		-- BCC co dinh
		tell msg
			make new bcc recipient at end of bcc recipients with properties {address:"herre.roelevink@manifera.com"}
		end tell
		if recipientAddr is not "" then
			tell msg
				make new to recipient at end of to recipients with properties {address:recipientAddr}
			end tell
		end if
	end tell
	return "Draft da mo: " & theSubject
end run
