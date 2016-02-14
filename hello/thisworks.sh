#! /bin/sh

git clean -x -f -d -q
gyp --depth=.
echo "Where is world.target.mk?"
( cd .. && find . -name world.target.mk )

