#!/bin/bash
# Mo email thanh draft trong Apple Mail (co nut Send, khong "RE:")
#
#   ./open_draft.sh                                    -> ban NL, chua co nguoi nhan
#   ./open_draft.sh launchstudio_email.html            -> ban EN
#   ./open_draft.sh launchstudio_email_nl.html a@b.nl  -> dien san nguoi nhan
set -e
cd "$(dirname "$0")"
HTML="${1:-launchstudio_email_nl.html}"
[ -f "$HTML" ] || { echo "Khong tim thay $HTML"; exit 1; }
osascript open_draft.applescript "$(pwd)/$HTML" "${2:-}"
