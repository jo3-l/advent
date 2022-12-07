import math
from dataclasses import dataclass, field
from functools import cached_property
from typing import Dict, List, Union

FsEntry = Union["File", "Directory"]

@dataclass
class File:
	name: str
	size: int


@dataclass
class Directory:
	name: str
	children: Dict[str, "FsEntry"] = field(default_factory=dict)

	@cached_property
	def size(self) -> int:
		total_size = 0
		for entry in self.children.values():
			total_size += entry.size
		return total_size

@dataclass
class Command:
	name: str
	args: List[str]
	stdout: List[str]

TOTAL_DISK_SPACE = 70_000_000
UNUSED_SPACE_REQUIRED = 30_000_000

def solve(data: str):
	cmds: list[Command] = []
	lines = data.splitlines()
	i = 0
	while i < len(lines):
		cmd, *args = lines[i].removeprefix("$ ").split()
		i += 1
		start = i
		while i < len(lines) and not lines[i].startswith("$ "):
			i += 1
		cmds.append(Command(cmd, args, lines[start:i]))
	
	root = Directory("/")
	cur_path: list[str] = []
	for cmd in cmds:
		if cmd.name == "cd":
			match cmd.args[0]:
				case "/":
					cur_path.clear()
				case "..":
					cur_path.pop()
				case dir_name:
					cur_path.append(dir_name)
		else:
			cur_dir = root
			for dir_name in cur_path:
				cur_dir: Directory = cur_dir.children[dir_name] # type: ignore
			for entry in cmd.stdout:
				if entry.startswith("dir"):
					dir_name = entry.removeprefix("dir ")
					cur_dir.children[dir_name] = Directory(dir_name)
				else:
					size, name = entry.split()
					cur_dir.children[name] = File(name, int(size))
	
	ans = math.inf
	def process(entry: FsEntry):
		nonlocal ans
		if isinstance(entry, Directory):
			if (TOTAL_DISK_SPACE - root.size + entry.size) >= UNUSED_SPACE_REQUIRED:
				ans = min(ans, entry.size)
			for child in entry.children.values():
				process(child)

	process(root)
	return ans
