Problem: the --generator-output option in gyp causes weirdness

This is a problem because tools like node-gyp depend on this 
option. The core error in GYP is that it calculates relative
paths before switching to the generator-output directory, at
which point its relative paths are wrong.

The result is output generated in the wrong directories; this
causes a variety of issues such as garbage in the file tree,
or failures (as GYP tries to work outside the home directory
in some case).

The behavior is visible when you use dependencies to other gyp
files.

I've made a minimal test case with two projects, one that uses
the other. They are at the same level. So, the path to the 2nd
gyp file is ../world/project.gyp. This is what GYP calculates
and uses (even if we specify full, absolute paths). However 
when we specify --generator-output=build (for instance), GYP
switches to that directory and THEN generates the makefiles for
world. These end up in `build/../world/project.gyp`, which is
wrong.

Solution: if user specifies --generator-output, then GYP must
calculate its relative paths FROM THIS DIRECTORY and not from
the location of the gyp file.
