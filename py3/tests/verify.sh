#!/bin/bash -i
#
# Read-only checks of bisos.vscodeClaude's commands, from PATH (the installed package).
#
# Nothing here opens, focuses or prompts anything in VS Code, and nothing reaches the partner Emacs:
# hookToEmacs is run as a made-up user (LOGNAME/USER), whose partner file is missing or stale.
# Needs the desktop VS Code's DISPLAY for vscodeTopology's verdict; the rest works without it.

if [[ "$(basename "$PWD")" != "tests" ]]; then
    echo "ERROR: verify.sh must be run from a directory named 'tests'." >&2
    echo "  Current PWD: $PWD" >&2
    exit 1
fi

partnerDir=/bisos/var/blee/vscode
hookEvent='{"hook_event_name":"Notification","session_id":"verify","cwd":"/tmp","message":"verify.sh"}'

lpDo which vscode.cs vscodeClaude.cs vscode-sbom.pcs           # EXPECT: all three on PATH

# ---- Layer 2: VS Code itself (vscode_csu) ----
lpDo vscode.cs -i vscodeVersion           # EXPECT: version, commit, architecture
lpDo vscode.cs -i vscodeTopology           # EXPECT: launcher, display, desktopMain, a verdict
lpDo vscode.cs -i vscodeWorkspaces           # EXPECT: folders, newest first
lpDo vscode.cs -i vscodeExtensions           # EXPECT: id@version lines
lpDo vscode.cs -i vscodeExtensionVersion anthropic.claude-code           # EXPECT: a version, e.g. 2.1.311

# ---- Layer 3: the partner Emacs (vscodeEmacs_csu) ----
lpDo vscode.cs -i vscodePartner           # EXPECT: the live partner's socket, pid, ... or "none" and why
lpDo vscode.cs -i vscodeBleeLinkSnippet           # EXPECT: the tasks.json and keybindings.json entries
lpDo vscode.cs -i vscodeBleeLinkCheck           # EXPECT: present / missing / differs, per piece; nothing written
lpDo eval LOGNAME=verifyNoPartner USER=verifyNoPartner vscode.cs -i vscodePartner           # EXPECT: none, no partner file

# ---- Layer 4: the Claude sessions (vscodeClaude_csu) ----
lpDo vscodeClaude.cs -i claudeSessionsList           # EXPECT: one line per running session, newest first
lpDo vscodeClaude.cs -i claudeSessionsList --mode=all           # EXPECT: local and remote sessions
lpDo vscodeClaude.cs -i claudeSessionsLatest           # EXPECT: a sessionId (or nothing, if none runs)
lpDo vscodeClaude.cs -i claudePromptUri "verify.sh: sends nothing"           # EXPECT: the vscode:// URI; nothing sent
lpDo vscodeClaude.cs -i claudePromptUri --session=new "verify.sh: sends nothing"           # EXPECT: a URI without session=
lpDo vscodeClaude.cs -i hooksSnippet           # EXPECT: the "hooks" entry, Stop and Notification
lpDo vscodeClaude.cs -i hooksCheck           # EXPECT: present / missing / differs, per event; nothing written

# The installers, into a scratch directory (never the user's files): added, then present when run again.
setupDir=$(mktemp -d)
lpDo vscode.cs -i vscodeBleeLinkInstall "${setupDir}/User"           # EXPECT: added, three times (created)
lpDo vscode.cs -i vscodeBleeLinkInstall "${setupDir}/User"           # EXPECT: present, three times
lpDo vscodeClaude.cs -i hooksInstall "${setupDir}/settings.json"           # EXPECT: added Stop, Notification
lpDo vscodeClaude.cs -i hooksCheck "${setupDir}/settings.json"           # EXPECT: present, twice
lpDo rm -r "${setupDir}"

# hookToEmacs with no partner file: exit 0 at once, nothing on stdout or stderr.
lpDo eval "echo '${hookEvent}' | LOGNAME=verifyNoPartner USER=verifyNoPartner vscodeClaude.cs -i hookToEmacs; echo exit=\$?"           # EXPECT: exit=0 only

# hookToEmacs with a stale partner file (dead pid, missing socket): the same.
lpDo eval "printf '%s\n' '{\"socket\": \"/tmp/verifyNoSuchSocket\", \"pid\": 999999, \"display\": \":1\", \"time\": \"2026-01-01T00:00:00+0000\"}' > ${partnerDir}/partner-verifyStale.json"
lpDo eval LOGNAME=verifyStale USER=verifyStale vscode.cs -i vscodePartner           # EXPECT: none, stale partner file: no process 999999
lpDo eval "echo '${hookEvent}' | LOGNAME=verifyStale USER=verifyStale vscodeClaude.cs -i hookToEmacs; echo exit=\$?"           # EXPECT: exit=0 only
lpDo rm -f /bisos/var/blee/vscode/partner-verifyStale.json

# ---- vscode-sbom.pcs ----
lpDo vscode-sbom.pcs -i aptPkgs_list           # EXPECT: wget, gpg, vscode
lpDo vscode-sbom.pcs -i extsReport           # EXPECT: each extension, pinned= and installed=
lpDo dpkg-query -W -f='${Package} ${Version}\n' code           # EXPECT: code <version> (the apt package is "code")
