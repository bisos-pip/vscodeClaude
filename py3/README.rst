===============================================================================
bisos.vscodeClaude: Command-Line Interfaces to VS Code and Its Claude Extension
===============================================================================


.. contents::
   :depth: 3
..

Overview
========

*bisos.vscodeClaude* drives the local (desktop) VS Code and its Claude
Code extension from the command line: open a file at a line, a folder, a
diff or a URI in VS Code; list the running Claude sessions; hand a
session a prompt, and optionally submit it. A shell, a script, Claude
itself, a VS Code task or an editor (Emacs) uses it the same way.

It is layer 2 of the AI-Activity layers (below): VS Code, with its
Claude extension. It also holds the Python of layers 3 and 4, as
separate modules, so that every command-line interface to VS Code is in
one package. It needs no editor: an AI-Activity conducted purely in VS
Code uses it from a shell. The Emacs side, layers 3 to 5, is the Blee
package `vscode-claude <https://github.com/bx-blee/vscode-claude>`__.

*For the local (desktop) VS Code; the remote VS Code server is not a
target.*

.. _table-of-contents:

Table of Contents TOC
=====================

-  `Overview <#overview>`__
-  `Its Place in the Layers <#its-place-in-the-layers>`__
-  `Part of BISOS — ByStar Internet Services Operating
   System <#part-of-bisos--bystar-internet-services-operating-system>`__
-  `bisos.vscodeClaude is a Command-Only PyCS
   Facility <#bisosvscodeclaude-is-a-command-only-pycs-facility>`__
-  `Installation <#installation>`__

   -  `Installation With pip <#installation-with-pip>`__
   -  `Installation With pipx <#installation-with-pipx>`__
   -  `Installing VS Code and Its Extensions:
      ``vscode-sbom.pcs`` <#installing-vs-code-and-its-extensions-vscode-sbompcs>`__

-  `Usage <#usage>`__

   -  `VS Code Itself: ``vscode.cs`` <#vs-code-itself-vscodecs>`__
   -  `VS Code and Its Partner Emacs:
      ``vscode.cs`` <#vs-code-and-its-partner-emacs-vscodecs>`__
   -  `Its Claude Sessions:
      ``vscodeClaude.cs`` <#its-claude-sessions-vscodeclaudecs>`__
   -  `The Emacs Layer:
      vscode-claude <#the-emacs-layer-vscode-claude>`__

-  `Key Files <#key-files>`__
-  `Documentation and Blee-Panels <#documentation-and-blee-panels>`__
-  `Support <#support>`__
-  `Planned Improvements <#planned-improvements>`__

Its Place in the Layers
=======================

AI-Activity, VS Code and Emacs are layered; each layer is usable without
those above it, and a lower layer never names an upper one. The figure
of the layers and their three uses (VS Code only; Blee and VS Code
Claude; Blee, VS Code Claude and AI-Activity) is in the README of
`vscode-claude <https://github.com/bx-blee/vscode-claude>`__.

+---+--------------------+--------------------+--------------------+
| # | Layer              | Package            | Modules            |
+===+====================+====================+====================+
| 0 | Templates          | ``aiTem            | assembled into a   |
|   |                    | plates-workFlow``, | base               |
|   |                    | ``aiTemplates-DE`` |                    |
+---+--------------------+--------------------+--------------------+
| 1 | AI-Activity        | ``                 | ``aiActivity.cs``  |
|   |                    | bisos.aiActivity`` |                    |
+---+--------------------+--------------------+--------------------+
| 2 | VS Code (+ Claude) | **bi               | ``vscode_csu``     |
|   |                    | sos.vscodeClaude** |                    |
+---+--------------------+--------------------+--------------------+
| 3 | Emacs <-> VS Code  | **bis              | `                  |
|   |                    | os.vscodeClaude**, | `vscodeEmacs_csu`` |
|   |                    | Blee               |                    |
|   |                    | ``vscode-claude``  |                    |
+---+--------------------+--------------------+--------------------+
| 4 | Emacs <-> VS Code  | **bis              | ``                 |
|   | Claude             | os.vscodeClaude**, | vscodeClaude_csu`` |
|   |                    | Blee               |                    |
|   |                    | ``vscode-claude``  |                    |
+---+--------------------+--------------------+--------------------+
| 5 | + AI-Activity      | Blee               | (elisp only)       |
|   |                    | ``vscode-claude``  |                    |
+---+--------------------+--------------------+--------------------+

Layers 3 and 4 are each a Python half here and an elisp half in Blee.
Within this package the same rule holds: ``vscode_csu`` names neither
Emacs nor Claude, ``vscodeEmacs_csu`` names no Claude, and
``vscodeClaude_csu`` imports the two below it.

Part of BISOS — ByStar Internet Services Operating System
=========================================================

Layered on top of Debian, **BISOS** (By\* Internet Services Operating
System) is a unified and universal framework for developing both
internet services and software-service continuums that use internet
services. See `Bootstrapping ByStar, BISOS and
Blee <https://github.com/bxGenesis/start>`__ for information about
getting started with BISOS.

**BISOS** is a foundation for **The Libre-Halaal ByStar Digital
Ecosystem** which is described as a cure for losses of autonomy and
privacy in a book titled: `Nature of
Polyexistentials <https://github.com/bxplpc/120033>`__

*bisos.vscodeClaude* is part of BISOS. It is a standalone package that
can be used independently of the full BISOS environment.

bisos.vscodeClaude is a Command-Only PyCS Facility
==================================================

bisos.vscodeClaude is a command-line tool. It is a PyCS single-unit
command service. PyCS is a framework that converges development of CLI
tools and services. PyCS is an alternative to FastAPI, Typer and Click.

bisos.vscodeClaude uses the PyCS-Framework to:

#. inspect the local VS Code and open things in it (``vscode.cs``);
#. join VS Code with a partner Emacs, in both directions
   (``vscode.cs``);
#. list the VS Code Claude sessions and prompt them
   (``vscodeClaude.cs``);
#. install VS Code and its extensions at pinned versions
   (``vscode-sbom.pcs``).

The core of PyCS-Framework is the *bisos.b* package (the
PyCS-Foundation). See `bisos.b <https://github.com/bisos-pip/b>`__ for
an overview.

Installation
============

The sources for the bisos.vscodeClaude pip package are maintained at:
https://github.com/bisos-pip/vscodeClaude.

Installation With pip
---------------------

.. code:: bash

   pip install bisos.vscodeClaude

On a BISOS host, install it editable from its source, in ``py3/``:

.. code:: bash

   ./pypiProc.sh -v -n showRun -i pkgReInstall edit /bisos/venv/bisos3

Installation With pipx
----------------------

.. code:: bash

   pipx install bisos.vscodeClaude

The following commands are made available:

-  ``vscode.cs``
-  ``vscodeClaude.cs``
-  ``vscode-sbom.pcs``

Installing VS Code and Its Extensions: ``vscode-sbom.pcs``
----------------------------------------------------------

``vscode-sbom.pcs`` installs VS Code itself from Microsoft's apt
repository, and the extensions of the local VS Code, per user, at pinned
versions: among them ``anthropic.claude-code`` (the Claude panel, whose
``/open`` URI is the prompt channel) and the Emacs keymap and org-mode
extensions.

::

   vscode-sbom.pcs -i aptPkgs_update all     # VS Code (code) from packages.microsoft.com
   vscode-sbom.pcs -i extsReport             # the pinned versions against the installed ones
   vscode-sbom.pcs -i extsInstallPinned      # install at the pinned versions (as the VS Code user)
   vscode-sbom.pcs -i extsInstallLatest      # install, or upgrade, to the latest versions

Usage
=====

Each command program is a small CSXU over its CSUs, whose examples it
shows: ``vscode.cs`` with no arguments lists its examples, and so does
``vscodeClaude.cs``.

VS Code Itself: ``vscode.cs``
-----------------------------

Layer 2, ``vscode_csu``: no Emacs, no Claude.

+----------------------------+----------------------------------------+
| Command                    | What it does                           |
+============================+========================================+
| ``vscodeVersion``          | version, commit, architecture          |
+----------------------------+----------------------------------------+
| ``vscodeTopology``         | can this shell reach a desktop VS      |
|                            | Code, on which ``DISPLAY``             |
+----------------------------+----------------------------------------+
| ``vscodeWorkspaces``       | the folders VS Code has state for,     |
|                            | newest first (a history)               |
+----------------------------+----------------------------------------+
| ``vscodeExtensions``       | the installed extensions (installing   |
|                            | them: ``vscode-sbom.pcs``)             |
+----------------------------+----------------------------------------+
| ``vscodeExtensionVersion`` | one extension's version, e.g.          |
|                            | ``anthropic.claude-code``              |
+----------------------------+----------------------------------------+
| ``vscodeFocus``            | bring a window to the front, by its    |
|                            | folder's name                          |
+----------------------------+----------------------------------------+
| ``vscodeOpenFile``         | a file, at a line and column           |
+----------------------------+----------------------------------------+
| ``vscodeOpenFolder``       | a folder, in the last active window or |
|                            | a new one (``--window=``)              |
+----------------------------+----------------------------------------+
| ``vscodeAddFolder``        | add a folder to the current window's   |
|                            | workspace                              |
+----------------------------+----------------------------------------+
| ``vscodeDiff``             | the diff view of two files             |
+----------------------------+----------------------------------------+
| ``vscodeOpenUri``          | hand a URI to the desktop VS Code      |
|                            | (``code --open-url``)                  |
+----------------------------+----------------------------------------+

::

   vscode.cs -i vscodeTopology
   vscode.cs -i vscodeOpenFile README.org 40 1

VS Code and Its Partner Emacs: ``vscode.cs``
--------------------------------------------

Layer 3, ``vscodeEmacs_csu``, in the same command program: no Claude.

+---------------------------+-----------------------------------------+
| Command                   | What it does                            |
+===========================+=========================================+
| ``vscodePartner``         | the partner Emacs (Blee), or why there  |
|                           | is none                                 |
+---------------------------+-----------------------------------------+
| ``bleeOpenFile``          | a file in the partner Emacs, at a line  |
|                           | (VS Code to Emacs)                      |
+---------------------------+-----------------------------------------+
| ``vscodeBleeLinkSnippet`` | the VS Code task and key that run       |
|                           | ``bleeOpenFile``, to paste              |
+---------------------------+-----------------------------------------+
| ``bleeMagit``             | a repo's magit status in the partner    |
|                           | Emacs (a commit walk)                   |
+---------------------------+-----------------------------------------+

**The partner Emacs is optional.** These commands, and ``hookToEmacs``
below, read the partner file that Blee's ``b:vscode/init`` writes
(``/bisos/var/blee/vscode/partner-<user>.json``): one Emacs partners
with one VS Code. A partner is live only if its pid is a running Emacs
and its socket exists.

For ``/bx-git-commit-walk`` to open each repo in Blee, set aiActivity's
``gitOpener``:

::

   aiActivity.cs -i userConfig_set --parName=gitOpener --parValue='vscode.cs -i bleeMagit'

Its Claude Sessions: ``vscodeClaude.cs``
----------------------------------------

Layer 4, ``vscodeClaude_csu``, over the two above.

+--------------------------+------------------------------------------+
| Command                  | What it does                             |
+==========================+==========================================+
| ``claudeSessionsList``   | the running sessions, one line each,     |
|                          | newest first                             |
+--------------------------+------------------------------------------+
| ``claudeSessionsLatest`` | the sessionId of the most recently       |
|                          | active local session                     |
+--------------------------+------------------------------------------+
| ``claudePromptUri``      | the URI ``claudePrompt`` would use;      |
|                          | sends nothing                            |
+--------------------------+------------------------------------------+
| ``claudePrompt``         | the prompt into the latest session, a    |
|                          | given one, or a new one                  |
+--------------------------+------------------------------------------+
| ``hookToEmacs``          | a Claude Code hook: the event to the     |
|                          | partner Emacs, if any                    |
+--------------------------+------------------------------------------+
| ``hooksSnippet``         | the ``~/.claude/settings.json`` hooks    |
|                          | entry for ``hookToEmacs``                |
+--------------------------+------------------------------------------+

``claudeSessionsList`` takes ``--mode`` (local, remote, all) and
``--cwd``; ``claudePrompt`` takes ``--session`` (an id, or ``new``),
``--cwd``, and ``--submit=yes`` to press Enter as well (default: you
do).

::

   vscodeClaude.cs -i claudeSessionsList
   DISPLAY=:1 vscodeClaude.cs -i claudePrompt "/bx-git-commit-msg ."

``claudePrompt`` opens the session through the Claude extension's URI
handler (``code --open-url``), so it needs the ``DISPLAY`` of the
desktop VS Code. A session that is already open only comes to the front
that way, so for a running session the text goes on the X clipboard
(``xclip``) and is pasted with ``xdotool``. Each command it runs is
shown on stderr.

With no live partner, ``hookToEmacs`` does nothing, at once and
silently, so installing the hooks does not affect pure VS Code use.

Both the session list (Claude Code's ``~/.claude/sessions/``) and the
URI handler are undocumented Claude Code internals, read as they are in
Claude Code 2.1.311; an upgrade may change them.

The Emacs Layer: vscode-claude
------------------------------

For those who work in Emacs, the Blee package
`vscode-claude <https://github.com/bx-blee/vscode-claude>`__ is layered
over this one: ``b:vscode.el`` over ``vscode.cs``,
``b:vscode:claude.el`` (prompts, sessions, hooks) over
``vscodeClaude.cs``, and ``b:vscode:claude:aiActivity.el`` (root and
here, the commit cycle, the commit walk) over that. It is optional and
does not interfere with pure VS Code use. Its README has the design: the
partnership, the sessions and their AI-Activities, the channels in both
directions, and the figure of the layers.

Key Files
=========

+----------------------------------+----------------------------------+
| File, in ``py3/``                | What                             |
+==================================+==================================+
| ``bin/vscode.cs``                | CSXU over ``vscode_csu`` and     |
|                                  | ``vscodeEmacs_csu``              |
+----------------------------------+----------------------------------+
| ``bin/vscodeClaude.cs``          | CSXU over ``vscodeClaude_csu``   |
|                                  | (was ``claudeSessions.cs``)      |
+----------------------------------+----------------------------------+
| ``bin/vscode-sbom.pcs``          | VS Code and its extensions,      |
|                                  | pinned                           |
+----------------------------------+----------------------------------+
| ``bi                             | layer 2: VS Code itself; the     |
| sos/vscodeClaude/vscode_csu.py`` | ``xclip`` and ``xdotool``        |
|                                  | helpers                          |
+----------------------------------+----------------------------------+
| ``bisos/v                        | layer 3: the partner file,       |
| scodeClaude/vscodeEmacs_csu.py`` | ``emacsclient``                  |
+----------------------------------+----------------------------------+
| ``bisos/vs                       | layer 4: the session registry,   |
| codeClaude/vscodeClaude_csu.py`` | the ``/open`` URI, hooks         |
+----------------------------------+----------------------------------+

-  ``vscode_csu.py`` inspects the local VS Code (its processes and
   ``DISPLAY``, the workspaces it keeps state for in its undocumented
   ``workspaceStorage/``, its extensions) and opens things in it.
-  ``vscodeEmacs_csu.py`` reads the partner file and evaluates in the
   partner Emacs.
-  ``vscodeClaude_csu.py`` reads the session registry, builds the
   extension's ``/open`` URI, prompts, and relays hook events.

All bisos-pip repos in the https://github.com/bisos-pip github
organization follow the same structure. They all have
`setup.py <./setup.py>`__ files driven by
`pypiProc.sh <./pypiProc.sh>`__.

Documentation and Blee-Panels
=============================

bisos.vscodeClaude is part of ByStar Digital Ecosystem
http://www.by-star.net.

Its Blee-Panel,
``./panels/bisos.vscodeClaude/_nodeBase_/fullUsagePanel-en.org``, is not
written yet (*planned*).

Support
=======

| For support, criticism, comments and questions; please contact the
  author/maintainer
| `Mohsen Banan <http://mohsen.1.banan.byname.net>`__ at:
  http://mohsen.1.banan.byname.net/contact

Planned Improvements
====================

-  Write the fullUsagePanel-en.org Blee-Panel.
-  Upload to PyPI and test as pipx install.
