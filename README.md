# Collection of github action chains
my favorite github actions that I use across multiple projects



# General

## Cleanup artifacts as cron job

This is a simple action (no chain) that just cleans up old artifacts to free some space.

**Required files**: 
- [.github/workflows/remove-old-artifacts.yml](https://github.com/paszin/collection-of-github-action-chains/blob/master/.github/workflows/remove-old-artifacts.yml)


# Python

## pylint on push

The lint action is for linting python files. I added a function to let the action fail, if the score is too small.

**Required files**: 
- [.github/workflows/lint.yml](https://github.com/paszin/collection-of-github-action-chains/blob/master/.github/workflows/lint.yml)
- [ci/compare.sh](https://github.com/paszin/collection-of-github-action-chains/blob/master/ci/compare.sh)
- [.pylintrc](https://github.com/paszin/collection-of-github-action-chains/blob/master/.pylintrc)


## pytest

This action performs testing with pytest. This example also contains instructions on how to install external packages with apt.

**Required files**: 
- [.github/workflows/test.yml](https://github.com/paszin/collection-of-github-action-chains/blob/master/.github/workflows/test.yml)


## Comment with coverage report on pull request

This actions runs pytest for pull request and comments with the coverage results including coverage badge.

**Required files**: 
- [.github/workflows/coverage.yml](https://github.com/paszin/collection-of-github-action-chains/blob/master/.github/workflows/coverage.yml)




# VueJS

## deploy to firebase


## build electron app


