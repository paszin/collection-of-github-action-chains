# collection-of-github-action-chains
my favorite github actions that I use across multiple projects


## pylint

The lint action is for linting python files. I added a function to let the action fail, if the score is too small.
Required files: lint.yml, ci/compare.sh, .pylintrc

## pytest

This action performs testing.

## Cleanup Artifacts

This is a simple action (no chain) that just cleans up old artifacts to free some space.

## Comment Coverage on Pull Requests

This actions runs pytest for pull request and comments with the coverage results.


