import itertools
from collections.abc import Iterator
from dataclasses import dataclass, field
from functools import cached_property
from typing import Union

FsEntry = Union["File", "Directory"]


@dataclass
class File:
    name: str
    size: int


@dataclass
class Directory:
    name: str
    children: dict[str, "FsEntry"] = field(default_factory=dict)

    def all_subdirs(self) -> Iterator["Directory"]:
        for child in self.children.values():
            if isinstance(child, Directory):
                yield child
                yield from child.all_subdirs()

    @cached_property
    def size(self) -> int:
        total_size = 0
        for entry in self.children.values():
            total_size += entry.size
        return total_size


CLI_PROMPT = "$ "


@dataclass
class Command:
    name: str
    args: list[str]
    stdout: list[str]

    @staticmethod
    def iter(cli_output: str):
        lines = cli_output.splitlines()
        i = 0
        while i < len(lines):
            name, *args = lines[i].removeprefix(CLI_PROMPT).split()
            stdout: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].startswith(CLI_PROMPT):
                stdout.append(lines[i])
                i += 1
            yield Command(name, args, stdout)


class FsState:
    def __init__(self):
        self.root = Directory("/")
        self.cur_dir_path: list[str] = []

    def update(self, cmd: Command):
        if cmd.name == "cd":
            self._process_cd(cmd.args[0])
        else:
            self._process_ls(cmd.stdout)

    def _process_cd(self, path: str):
        match path:
            case "/":
                self.cur_dir_path.clear()
            case "..":
                self.cur_dir_path.pop()
            case sub_dir:
                self.cur_dir_path.append(sub_dir)

    def _process_ls(self, entries: list[str]):
        cur_dir = self._get_cur_dir()
        for entry in entries:
            if entry.startswith("dir "):
                name = entry.removeprefix("dir ")
                cur_dir.children[name] = Directory(name)
            else:
                size, name = entry.split()
                cur_dir.children[name] = File(name, int(size))

    def _get_cur_dir(self):
        cur_dir = self.root
        for subdir_name in self.cur_dir_path:
            subdir = cur_dir.children[subdir_name]
            assert isinstance(subdir, Directory)
            cur_dir = subdir
        return cur_dir


MAX_SIZE = 100_000


TARGET_DISK_SPACE = 70_000_000 - 30_000_000


def solve(data: str):
    state = FsState()
    for cmd in Command.iter(data):
        state.update(cmd)

    return min(
        dir.size
        for dir in itertools.chain([state.root], state.root.all_subdirs())
        if state.root.size - dir.size <= TARGET_DISK_SPACE
    )
