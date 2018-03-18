
DB_SAMPLE = [
	["ls -la", ["file", "list"], "A command description"],
	["ls -ld /etc", ["file", "list"], "A command description"],
	["ls  -Rla", ["file", "list"], "A command description"],
	["ls -l -a file", ["file", "list", "file", "list", "file", "list", "file", "list", "file", "list", "file", "list", "file", "list", "file", "list"], "long tags"],
	["ls --all file", ["file", "list"], "double flags"],
	["ls -ls; ls --all", ["file", "list"], "multi"],
	["ls -ls; rm -l file", ["file", "list"], "multi"],
	["srm -l -r -v -z file1 file2 dir1/", ["secure", "remove", "file"], "secure delete files from disk"],
	["srm -lrvz file1 file2 dir1/", ["secure", "remove", "file"], "secure delete files from disk"],
	["git add -b branchName", ["git", "branch", "file"], "sub commands"],
	["git checkout -b branchName", ["git", "branch", "file"], "sub commands"],
	["cd /dir/dir 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890",  ["directory", "file"], "list file and direc"],
	["cd /dir/dir 12345678901234567890123456789012345678901234567890",  ["directory", "file"], "list file and direct"],
	["cd /dir/dir 12345678901234567890123456789012345678901234567890",  ["directory", "file"], "list file and directory 1234567889"],
	["ls -l -a file",  ["file", "list", "list2", "list3", "list4", "list5"], "print all files description"],
	["cat file", ["read", "file"], "read file"],
	["while true; do lsof -v -f /paht/to/file; done;", ["loop", "list", "file"], "find open files"],
	["while true; do ls -lva /paht/to/file; done;", ["loop", "list", "file"], "find open files"],
	["tar --anchored hello2", ["zip", "archive"], "tar with flags"],
	["tar --group --atime-preserve hello3", ["zip", "archive"], "tar with flags"],
	["tar -rvt hello4", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello5", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello6", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello3", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello4", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello5", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello6", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello3", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello4", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello5", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello6", ["zip", "archive"], "tar unzip"],
	["tar -rvt hello7", ["zip", "archive"], "tar unzip"]
]
