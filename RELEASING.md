# Releasing re-usable workflows

## Changelog

To track changes in this repository made between versions and to generate a changelog, we use [changelog fragments](https://docs.ansible.com/ansible/latest/community/development_process.html#creating-a-changelog-fragment).

## Release process

1. Based on the [Semantic Versioning](https://semver.org/) conventions and [changelog/fragments](changelog/fragments), determine a proper release version number.

   - When we change any versions of tools, their arguments or anything else that might result in failures on partners' side, we release a major version.
2. Follow the [Releasing guidelines](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_release_without_branches.html) where applicable (for example, we don't publish this collection on Galaxy).
3. When releasing a major release, besides a tag for the release `X.y.z`, also create a corresponding tag `vX` that will always point to the latest release of this major release. For example, if you released version `1.0.0`, create tag `v1` that will point to the same commit as tag `v1.0.0`.
4. When releasing a minor or patch release `x.Y.Z`, move a corresponding `vX` tag to point to it. For example, when releasing version `1.1.0`, move tag `v1` to point to the same commit as `v1.1.0`.

   1. Get the commit SHA for the tag: `git rev-parse v1.1.0`
   2. Move the existing local `v1` tag to the new commit SHA: `git tag -f v1 <commit-sha-of-v1.1.0>`
   3. Force push the tag to GitHub: `git push upstream -f v1`

## Post-release actions

TBD when defined
