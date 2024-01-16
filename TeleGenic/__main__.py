import subprocess
import sys
from typing import Optional

import certifi

from . import __version__ as TeleGenic_ver
from .constants import BOT_API_VERSION


def _git_revision() -> Optional[str]:
    try:
        output = subprocess.check_output(  # skipcq: BAN-B607
            ["git", "describe", "--long", "--tags"], stderr=subprocess.STDOUT
        )
    except (subprocess.SubprocessError, OSError):
        return None
    return output.decode().strip()


def print_ver_info() -> None:  # skipcq: PY-D0003
    git_revision = _git_revision()
    print(f'TeleGenic {TeleGenic_ver}' + (f' ({git_revision})' if git_revision else ''))
    print(f'Bot API {BOT_API_VERSION}')
    print(f'certifi {certifi.__version__}')  # type: ignore[attr-defined]
    sys_version = sys.version.replace('\n', ' ')
    print(f'Python {sys_version}')


def main() -> None:  # skipcq: PY-D0003
    print_ver_info()


if __name__ == '__main__':
    main()
