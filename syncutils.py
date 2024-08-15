# Thanks to @Vexed01 on GitHub for this code (https://github.com/Vexed01/Vex-Cogs)!
# Copy the utils from https://github.com/AAA3A-AAA3A/AAA3A_utils to each cog in this repo.

import datetime
import json
import os
import shutil
from pathlib import Path

import git
from git import Repo

# git -C %USERPROFILE%\Documents\GitHub\AAA3A_utils rev-list HEAD --count AAA3A_utils
VERSION = 6.7

if VERSION is None:
    utils_repo_clone_location = Path(
        os.environ["USERPROFILE"] + "\\Documents\\GitHub\\AAA3A_utils_clone_for_sync"
    )
    utils_repo = Repo.clone_from(
        "https://github.com/AAA3A-AAA3A/AAA3A_utils.git", utils_repo_clone_location
    )

    utils_location = utils_repo_clone_location / "AAA3A_utils"
    commit = utils_repo.head.commit

    README_MD_TEXT = """## My utils

    Hello there! If you're contributing or taking a look, everything in this folder
    is synced from a master repo at https://github.com/AAA3A-AAA3A/AAA3A_utils by GitHub Actions -
    so it's probably best to look/edit there.

    ---

    Last sync at: {time}
    Commit: [`{commit}`](https://github.com/AAA3A-AAA3A/AAA3A_utils/commit/{commit})
    """
    readme = README_MD_TEXT.format(
        time=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z"),
        commit=commit,
    )

    with open(utils_location / "README.md", "w") as fp:
        fp.write(readme)

    with open(utils_location / "commit.json", "w") as fp:
        fp.write(json.dumps({"latest_commit": str(commit)}))
else:
    destination = Path(os.environ["USERPROFILE"] + "\\Documents\\GitHub\\AAA3A_utils\\AAA3A_utils")
    with open(destination / "__version__.py", "w") as fp:
        fp.write(f"__version__ = {VERSION}\n")

all_cogs = [
    "AcronymGame",
    "AntiNuke",
    "AutoTraceback",
    "Calculator",
    "ClearChannel",
    "CmdChannel",
    "CodeSnippets",
    "CommandsButtons",
    "ConsoleLogs",
    "CtxVar",
    "Dashboard",
    "Dev",
    "DevUtils",
    "DiscordEdit",
    "DiscordModals",
    "DiscordSearch",
    "Draw",
    "DropdownsTexts",
    "EditFile",
    "EmbedUtils",
    "ExportChannel",
    "GetDocs",
    "GetLoc",
    "GistsHandler",
    "GuildStats",
    "Ip",
    "LinkQuoter",
    "LintCodes",
    "Medicat",
    "MemberPrefix",
    "MemoryGame",
    "Minecraft",
    "PresenceChart",
    "ReactToCommand",
    "Recipes",
    "Reminders",
    "RolesButtons",
    "RunCode",
    "Seen",
    "SimpleSanction",
    "Snipe",
    "SplitOrStealGame",
    "Sudo",
    "TempRoles",
    "TicketTool",
    "TransferChannel",
    "UrlButtons",
    "ViewPermissions",
    "Webhook",
]
cog_folders = [cog.lower() for cog in all_cogs]
for cog in cog_folders:
    destination = (
        Path(os.environ["USERPROFILE"] + "\\Documents\\GitHub\\AAA3A-cogs") / cog / "AAA3A_utils"
    )
    if destination.exists():
        shutil.rmtree(destination)
    if VERSION is None:
        shutil.copytree(utils_location, destination)
    else:
        destination = Path(os.environ["USERPROFILE"] + "\\Documents\\GitHub\\AAA3A-cogs") / cog
        with open(destination / "utils_version.json", "w") as fp:
            fp.write(json.dumps({"needed_utils_version": VERSION}))

if VERSION is None:
    utils_repo.close()
    git.rmtree(utils_repo_clone_location)
