# Collection of github action chains
my favorite github actions that I use across multiple projects


## pylint on push

The lint action is for linting python files. I added a function to let the action fail, if the score is too small.

**Required files**: 
- [lint.yml](https://github.com/paszin/collection-of-github-action-chains/blob/master/.github/workflows/lint.yml)
- [ci/compare.sh](https://github.com/paszin/collection-of-github-action-chains/blob/master/ci/compare.sh)
- .pylintrc

## pytest

This action performs testing.

## Cleanup artifacts as cron job

This is a simple action (no chain) that just cleans up old artifacts to free some space.

## Comment with coverage report on pull request

This actions runs pytest for pull request and comments with the coverage results.


