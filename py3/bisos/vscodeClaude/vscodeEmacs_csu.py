# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= for Emacs <-> VS Code (layer 3): the partner Emacs (Blee) of the local
VS Code, and opening things in it. In =vscode.cs='s csuList; a library of =vscodeClaude_csu= too.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: This File, Authors, version
** This File: /bxRepos/bisos-pip/vscodeClaude/py3/bisos/vscodeClaude/vscodeEmacs_csu.py
** File True Name: /bisos/git/auth/bxRepos/bisos-pip/vscodeClaude/py3/bisos/vscodeClaude/vscodeEmacs_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inDev"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['vscodeEmacs_csu'], }
csInfo['version'] = '202610310000'
csInfo['status']  = 'inDev'
csInfo['panel'] = 'vscodeEmacs_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]]
Layer 3 of blee/vscode-claude's five (WorkPlan Stage 13): Emacs <-> VS Code, with no Claude in it.
The partner file =/bisos/var/blee/vscode/partner-<user>.json= (written by Blee's =b:vscode/init=)
names the one Emacs that partners with this user's VS Code; =partnerRead= checks it is alive. On it:
=bleeOpenFile= (VS Code to Emacs at a line), =bleeMagit= (a repo's magit, the =gitOpener= of
=/bx-git-commit-walk=), =vscodeBleeLinkSnippet=, =vscodePartner=. Split out of =vscode_csu= (layer 2),
which has no Emacs in it, 2026-10-31.
** Status: inDev
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io

import collections
####+END:

from bisos.common import csParam  # used by the generated classHead bodies

import getpass
import json
import os
import pathlib
import shlex
import stat
import subprocess
import sys


from bisos.vscodeClaude import vscode_csu
from bisos.vscodeClaude.vscode_csu import userDataDir, programPath


# The partner Emacs (Blee): one per user. b:vscode/init (blee/vscode-claude) writes the file with the
# Emacs's server socket and pid; kill-emacs-hook removes it. Readers check that it is alive: a stale
# file (dead pid, missing socket) counts as no partner. VS Code alone needs none of this.
partnerDir = pathlib.Path('/bisos/var/blee/vscode')


def partnerFile(user: typing.Optional[str] = None) -> pathlib.Path:
    return partnerDir / f"partner-{user or getpass.getuser()}.json"


def partnerRead() -> typing.Tuple[typing.Optional[typing.Dict[str, typing.Any]], str]:
    """(the live partner's entry, ''), or (None, why there is none)."""
    path = partnerFile()
    try:
        entry = json.loads(path.read_text())
        socket = entry['socket']
        pid = int(entry['pid'])
    except FileNotFoundError:
        return None, f"no partner file ({path})"
    except (OSError, ValueError, KeyError, TypeError) as err:
        return None, f"unreadable partner file {path}: {err}"
    try:
        exe = pathlib.Path(f'/proc/{pid}/exe').readlink().name
    except OSError:
        return None, f"stale partner file {path}: no process {pid}"
    if not exe.startswith('emacs'):
        return None, f"stale partner file {path}: process {pid} is {exe}, not emacs"
    try:
        if not stat.S_ISSOCK(os.stat(socket).st_mode):
            return None, f"stale partner file {path}: {socket} is not a socket"
    except OSError:
        return None, f"stale partner file {path}: no socket {socket}"
    return entry, ''


def elispString(text: str) -> str:
    """text as an elisp string literal (JSON's string syntax is a subset of elisp's, with ASCII only)."""
    return json.dumps(text, ensure_ascii=True)


def emacsEvalCommand(socket: str, form: str) -> typing.List[str]:
    return ['emacsclient', '-s', socket, '--eval', form]


def emacsEval(socket: str, form: str, timeout: float = 10) -> typing.Optional[subprocess.CompletedProcess]:
    """Evaluate form in the Emacs of socket; None when it does not answer within timeout."""
    try:
        return subprocess.run(emacsEvalCommand(socket, form), capture_output=True, text=True,
                              check=False, timeout=timeout)
    except subprocess.TimeoutExpired:
        return None


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Examples of the Emacs <-> VS Code layer's commands.
    #+end_org """
    cmnd = cs.examples.cmndEnter
    literal = cs.examples.execInsert
    od = collections.OrderedDict

    cs.examples.menuChapter('=Blee= -- the partner Emacs (optional; b:vscode/init of blee/vscode-claude)')
    cmnd('vscodePartner', comment="# The live partner Emacs (socket, pid), or why there is none")
    cmnd('bleeOpenFile', args='README.org 10 5', comment="# This file in the partner Emacs, at line 10, column 5")
    cmnd('vscodeBleeLinkSnippet', comment="# The VS Code task and key that run bleeOpenFile on the current file")
    cmnd('vscodeBleeLinkCheck', comment="# Read-only: are the task, key and setting in VS Code's user files")
    cmnd('vscodeBleeLinkInstall', comment="# Merge them into tasks.json, keybindings.json, settings.json (backups)")
    cmnd('vscodeBleeLinkInstall', pars=od([('key', 'ctrl+alt+e')]), comment="# The same, with another key (default ctrl+k ctrl+e)")
    cmnd('bleeMagit', args='.', comment="# This repo's magit status in the partner Emacs (a commit walk)")
    literal("aiActivity.cs -i userConfig_set --parName=gitOpener --parValue='vscode.cs -i bleeMagit'  # /bx-git-commit-walk opens repos in Blee")


def commonParamsSpecify(csParams: cs.param.CmndParamDict) -> None:
    """--key: the VS Code key of the Blee link."""
    csParams.parDictAdd(
        parName='key',
        parDescription="vscodeBleeLink*: the VS Code key that runs the task (default 'ctrl+k ctrl+e')",
        parDataType=None,
        parDefault=None,
        parChoices=[],
        argparseShortOpt=None,
        argparseLongOpt='--key',
    )


# The VS Code -> Blee link (vscodeBleeLinkSnippet, ...Install, ...Check): a user task running bleeOpenFile
# on the editor's file and line, a key for it, and the setting that saves the file first.
bleeLinkLabel = "Blee: open here"
# A VS Code chord: handled by VS Code alone, so it gets through a VNC viewer. Ctrl+Alt+E, the first
# choice, did not (on Windows Ctrl+Alt is AltGr). Another with --key.
bleeLinkKeyDefault = "ctrl+k ctrl+e"


def bleeLinkPieces(
        key: typing.Optional[str] = None,
) -> typing.Tuple[typing.Dict[str, typing.Any], typing.Dict[str, str], typing.Dict[str, str]]:
    """The task, the key (default bleeLinkKeyDefault) and the setting."""
    # The interpreter is named, not left to vscode.cs's "#!/bin/env python": VS Code started from the
    # desktop has no BISOS venv on its PATH, and there "python" is not found.
    task = {
        "label": bleeLinkLabel,
        "type": "process",
        "command": sys.executable,
        "args": [programPath('vscode.cs'), "-i", "bleeOpenFile", "${file}", "${lineNumber}", "${columnNumber}"],
        "presentation": {"reveal": "silent", "showReuseMessage": False},
        "problemMatcher": [],
    }
    binding = {"key": key or bleeLinkKeyDefault, "command": "workbench.action.tasks.runTask", "args": bleeLinkLabel}
    return task, binding, {"task.saveBeforeRun": "always"}


def bleeLinkFiles(userDir: typing.Optional[str] = None) -> typing.Tuple[pathlib.Path, pathlib.Path, pathlib.Path]:
    """tasks.json, keybindings.json and settings.json of VS Code's User directory."""
    base = pathlib.Path(userDir).expanduser() if userDir else userDataDir / 'User'
    return base / 'tasks.json', base / 'keybindings.json', base / 'settings.json'


def bleeLinkMerge(
        userDir: typing.Optional[str],
        write: bool,
        keyName: typing.Optional[str] = None,
) -> typing.List[vscode_csu.Merge]:
    """Check (write False) or install the three pieces; ours are found by the task's label, so a new key
replaces the old binding."""
    task, key, setting = bleeLinkPieces(keyName)
    tasks, keys, settings = bleeLinkFiles(userDir)

    def taskMerge(value):
        value = {"version": "2.0.0", "tasks": []} if value is None else value
        entries = value.setdefault("tasks", [])
        for i, entry in enumerate(entries):
            if isinstance(entry, dict) and entry.get("label") == bleeLinkLabel:
                if entry == task:
                    return value, 'present'
                entries[i] = task
                return value, 'differs'
        entries.append(task)
        return value, 'missing'

    def keyMerge(value):
        value = [] if value is None else value
        for i, entry in enumerate(value):
            if isinstance(entry, dict) and entry.get("command") == key["command"] \
               and entry.get("args") == bleeLinkLabel:
                if entry == key:
                    return value, 'present'
                value[i] = key
                return value, 'differs'
        value.append(key)
        return value, 'missing'

    def settingMerge(value):
        value = {} if value is None else value
        (name, wanted), = setting.items()
        if value.get(name) == wanted:
            return value, 'present'
        state = 'missing' if name not in value else 'differs'
        value[name] = wanted
        return value, state

    merges = (vscode_csu.jsoncMerge(tasks, [(f'task "{bleeLinkLabel}"', taskMerge)], write)
              + vscode_csu.jsoncMerge(keys, [(f'key {key["key"]}', keyMerge)], write)
              + vscode_csu.jsoncMerge(settings, [('task.saveBeforeRun', settingMerge)], write))
    # Another user binding on the same key would shadow or be shadowed: say so (VS Code's defaults and
    # the desktop's own shortcuts are not visible from here).
    try:
        others = [e for e in (vscode_csu.jsoncRead(keys).value or [])
                  if isinstance(e, dict) and e.get("key") == key["key"] and e.get("args") != bleeLinkLabel]
    except ValueError:
        others = []
    if others:
        merges.append(vscode_csu.Merge(keys, f'key {key["key"]}', 'note',
                                       f"also bound to {', '.join(str(e.get('command')) for e in others)}"))
    return merges


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodePartner" :comment "The partner Emacs, or why there is none" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodePartner>>  *The partner Emacs, or why there is none*  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodePartner(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """The partner Emacs, or why there is none"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Read the partner file (=/bisos/var/blee/vscode/partner-<user>.json=,
written by =b:vscode/init=) and check that its Emacs is alive. Prints =live= and the entry's fields, one
=key value= line each, or =none= and why. Read-only; VS Code alone needs no partner.
        #+end_org """)
        entry, why = partnerRead()
        if entry is None:
            print(f"none\t{why}")
        else:
            print("live")
            for key in ('socket', 'pid', 'display', 'time', 'emacsVersion'):
                print(f"{key}\t{entry.get(key, '')}")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bleeMagit" :comment "Open a repo's magit status in the partner Emacs" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bleeMagit>>  *Open a repo's magit status in the partner Emacs*  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bleeMagit(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Open a repo's magit status in the partner Emacs"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Show the git repo of the directory (its top level) in the partner Emacs
(=vscodePartner=) with =magit-status=, and raise its frame. Used by =/bx-git-commit-walk=: the user then
stages, asks Claude for the message (magit =x x=) and commits. Prints the repo's top level. Refused
when there is no live partner, or the directory is not in a git repo.
        #+end_org """)
        given = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        if not given:
            b_io.eh.problem_usageError("No repo: give its directory as the argument")
            return failed(cmndOutcome)
        directory = pathlib.Path(given).expanduser().absolute()
        result = subprocess.run(['git', '-C', str(directory), 'rev-parse', '--show-toplevel'],
                                capture_output=True, text=True, check=False)
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"Not in a git repo: {directory}")
            return failed(cmndOutcome)
        top = result.stdout.strip()
        entry, why = partnerRead()
        if entry is None:
            b_io.eh.problem_usageError(f"No partner Emacs: {why} (b:vscode/init in Blee)")
            return failed(cmndOutcome)
        form = (f"(progn (magit-status {elispString(top + '/')})"
                " (let ((f (selected-frame))) (raise-frame f) (select-frame-set-input-focus f))"
                " (buffer-name))")
        b_io.ann.note(shlex.join(emacsEvalCommand(entry['socket'], form)))
        done = emacsEval(entry['socket'], form)
        if done is None:
            b_io.eh.problem_usageError(f"emacsclient did not answer within 10s ({entry['socket']})")
            return failed(cmndOutcome)
        if done.returncode != 0:
            b_io.eh.problem_usageError(f"emacsclient failed ({done.returncode}): {done.stderr.strip()}")
            return failed(cmndOutcome)
        print(top)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="repo",
            argDefault=None,
            argChoices=[],
            argDescription="A directory in the git repo",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "bleeOpenFile" :comment "Open a file in the partner Emacs, at a line" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 3 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<bleeOpenFile>>  *Open a file in the partner Emacs, at a line*  =verify= argsMin=1 argsMax=3 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class bleeOpenFile(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 3,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Open a file in the partner Emacs, at a line"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  VS Code to Emacs: visit the file in the partner Emacs (=vscodePartner=), at
the line and column when given (=emacsclient -n +LINE:COL=), and raise its frame. Run by the VS Code
task of =vscodeBleeLinkSnippet=. Refused when there is no live partner.
        #+end_org """)
        file = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        line = self.cmndArgsGet("1", cmndArgsSpecDict, argsList)
        column = self.cmndArgsGet("2", cmndArgsSpecDict, argsList)
        if not file:
            b_io.eh.problem_usageError("No file: give it as the first argument")
            return failed(cmndOutcome)
        entry, why = partnerRead()
        if entry is None:
            b_io.eh.problem_usageError(f"No partner Emacs: {why} (b:vscode/init in Blee)")
            return failed(cmndOutcome)
        path = str(pathlib.Path(file).expanduser().absolute())
        where = [f"+{line}" + (f":{column}" if column else "")] if line else []
        command = ['emacsclient', '-s', entry['socket'], '-n', *where, path]
        b_io.ann.note(shlex.join(command))
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
        except subprocess.TimeoutExpired:
            b_io.eh.problem_usageError(f"emacsclient did not answer within 10s ({entry['socket']})")
            return failed(cmndOutcome)
        if result.returncode != 0:
            b_io.eh.problem_usageError(f"emacsclient failed ({result.returncode}): {result.stderr.strip()}")
            return failed(cmndOutcome)
        emacsEval(entry['socket'], "(let ((f (selected-frame))) (raise-frame f) (select-frame-set-input-focus f))")
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="file",
            argDefault=None,
            argChoices=[],
            argDescription="The file",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="line",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: the line",
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="2",
            argName="column",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: the column",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeBleeLinkSnippet" :comment "The VS Code task and key that run bleeOpenFile" :extent "verify" :ro "cli" :parsMand "" :parsOpt "key" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeBleeLinkSnippet>>  *The VS Code task and key that run bleeOpenFile*  =verify= parsOpt=key ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeBleeLinkSnippet(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'key', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             key: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:
        """The VS Code task and key that run bleeOpenFile"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'key': key, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        key = csParam.mappedValue('key', key)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print, to paste by hand, the user task (=~/.config/Code/User/tasks.json=,
"Tasks: Open User Tasks") and the key (=keybindings.json=) that run =bleeOpenFile= on the file and line
of the VS Code editor. Also the setting that saves the file first. Nothing is written:
=vscodeBleeLinkInstall= merges them into the files, =vscodeBleeLinkCheck= says what is there.
        #+end_org """)
        task, binding, setting = bleeLinkPieces(key)
        tasks, keys, settings = bleeLinkFiles()
        print(f"// {tasks}: add to \"tasks\"")
        print(json.dumps(task, indent=2))
        print(f"// {keys}: add to the list")
        print(json.dumps(binding, indent=2))
        print(f"// {settings}: so that Emacs gets what is on screen")
        print(json.dumps(setting, indent=2))
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeBleeLinkCheck" :comment "Is the VS Code task and key of bleeOpenFile installed" :extent "verify" :ro "cli" :parsMand "" :parsOpt "key" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeBleeLinkCheck>>  *Is the VS Code task and key of bleeOpenFile installed*  =verify= parsOpt=key argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeBleeLinkCheck(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'key', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             key: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Is the VS Code task and key of bleeOpenFile installed"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'key': key, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        key = csParam.mappedValue('key', key)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Read-only: for each piece of =vscodeBleeLinkSnippet= (the task in
=tasks.json=, the key in =keybindings.json=, =task.saveBeforeRun= in =settings.json=), one line:
=present=, =missing= or =differs=, the file and the piece. A file =vscodeBleeLinkInstall= would refuse
(comments inside its JSON) is said so. The optional argument is another User directory (tests).
        #+end_org """)
        userDir = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        vscode_csu.mergesReport(bleeLinkMerge(userDir, write=False, keyName=key), write=False)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="userDir",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: VS Code's User directory (default ~/.config/Code/User); for tests",
        )
        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "vscodeBleeLinkInstall" :comment "Merge the VS Code task and key of bleeOpenFile into the user files" :extent "verify" :ro "cli" :parsMand "" :parsOpt "key" :argsMin 0 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<vscodeBleeLinkInstall>>  *Merge the VS Code task and key of bleeOpenFile into the user files*  =verify= parsOpt=key argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class vscodeBleeLinkInstall(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ 'key', ]
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             key: typing.Optional[str]=None,  # Cs Optional Param
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:
        """Merge the VS Code task and key of bleeOpenFile into the user files"""
        failed = b_io.eh.badOutcome
        callParamsDict = {'key': key, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
        key = csParam.mappedValue('key', key)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Merge the pieces of =vscodeBleeLinkSnippet= into VS Code's user files:
the task into =tasks.json= (created when missing), the key into =keybindings.json=,
=task.saveBeforeRun= into =settings.json=. Idempotent: a piece already there is left alone; one of
ours that differs (found by the task's label) is replaced; other entries are never touched. Each file
written is backed up first (=<name>.<time>.bak=). A comment block before the JSON is kept; a file with
comments inside is refused, its piece to be added by hand. VS Code reloads the files by itself.
=--key= sets the key (default =ctrl+k ctrl+e=); it replaces the binding installed before.
Per-user setup after =vscode-sbom.pcs=; not an sbom.
        #+end_org """)
        userDir = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)
        if not vscode_csu.mergesReport(bleeLinkMerge(userDir, write=True, keyName=key), write=True):
            b_io.eh.problem_usageError("Some pieces were refused: add them by hand (vscodeBleeLinkSnippet)")
            return failed(cmndOutcome)
        return cmndOutcome.set(opError=b.op.OpError.Success, opResults=None)

    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="userDir",
            argDefault=None,
            argChoices=[],
            argDescription="Optional: VS Code's User directory (default ~/.config/Code/User); for tests",
        )
        return cmndArgsSpecDict
