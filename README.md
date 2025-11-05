# Collection certification onboarding

This repository aims to provide a clear set of instructions and content to help Red Hat partners:

- onboard their collections as [certified content on Ansible Automation Hub](https://connect.redhat.com/sites/default/files/2025-04/V28_Ansible_Certification_Policy_Guide_2025.pdf)
- reduce the probability of a collection version upload rejection

## Collection testing

Errors in Automation Hub import logs is the most common reason for collection rejection.
Make sure the collection passes Galaxy-importer checks before uploading.

To make the checks run against every pull request in your GitHub repository automatically and on a scheduled basis:

1. [ ] Copy the [Ansible collection certification GitHub Actions workflow](https://github.com/ansible-collections/certification/blob/main/.github/workflows/cert-tests.yml) to the `.github/workflows` directory of your collection repository.
  - [ ] Check the `Actions` tab on GitHub UI to make sure the workflow is running.
  - [ ] Fix any failures.

    - [ ] If your collection ignores some errors by using `ignore-*.txt` files, make sure there are entries of [allowed types](https://ansible.readthedocs.io/projects/lint/rules/sanity/) only.

2. [ ] Keep a list of `ansible-core` versions in the `Sanity` job of the workflow updated when new versions of `ansible-core` come out:

  - [ ] Subscribe to the [news-for-maintainers](https://forum.ansible.com/tag/news-for-maintainers) tag on the Ansible Forum by clicking the bell button in the upper-right corner to get notified about new `ansible-core` versions available for testing.
  - [ ] Check out the [ansible-core support matrix](https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix) periodically to remove EOL versions of `ansible-core` from your workflow's test matrix that your collection does not support.

3. If your repository is not hosted on GitHub, please run the checks locally as described in the `STEP 6: Test and lint your Ansible Collection` section of the [Certification workflow guide](https://connect.redhat.com/sites/default/files/2025-06/Ansible-Certification-Workflow-Guide202506.pdf).

## Check the following before uploading a collection version

Before uploading a tarball of your collection to Automation Hub:

- [ ] Consult the [Ansible Certification Workflow Guide](https://connect.redhat.com/sites/default/files/2025-06/Ansible-Certification-Workflow-Guide202506.pdf) to ensure the collection meets the requirements listed in STEPS 5-7.
- [ ] Ensure that `README.md` in your collection contains all required sections such as Description, Installation, Support, and Changelog/Release notes.

  - [ ] To avoid rejection of your collection due to insufficient or absent sections, use the [Ansible Certified Collections README Template](https://github.com/ansible-collections/certification/blob/main/README_template.md).
  - [ ] Ensure that the `Support` section refers users to **Automation Hub** for support similar to [README_template#support](https://github.com/ansible-collections/certification/blob/main/README_template.md#support).

    - Additionally, for users who obtained the collection from Galaxy and have no access to Automation Hub, you can refer them for support to GitHub issues in your repository or to Ansible Forum.

- [ ] Make sure the collection passes Galaxy-importer checks on GitHub as described in the [Collection testing section](https://github.com/ansible-collections/certification/blob/main/README.md#collection-testing).
- [ ] Ensure the collection follows the [Versioning and Release Strategy](https://access.redhat.com/articles/4993781) and specifically [Semantic Versioning](https://semver.org/) when determining which version to release. Practically, it means that given a version number `MAJOR.MINOR.PATCH`, increment the following:

  - `MAJOR` version: when making incompatible API changes.
  - `MINOR` version: when adding features or functionality in a backward-compatible manner (e.g., adding new module options).
  - `PATCH` version: when adding backward-compatible bug fixes or security fixes (strict).
  - The collection version must be at least `1.0.0` to be accepted.

- [ ] Ensure the collection tarball you upload contains a changelog with an entry for the version being uploaded.

  - https://access.redhat.com/articles/4993781
  - We recommend using the [antsibull-changelog](https://ansible.readthedocs.io/projects/antsibull-changelog/) tool for changelog generation.

## Optional

- If you want to cover your collection with other kinds of tests (for example, unit and/or integration) to ensure your code stability, you can use the following resources:

  - [Ansible Nox](https://ansible.readthedocs.io/projects/antsibull-nox/introduction/)
  - [Ansible Test GitHub Actions](https://github.com/marketplace/actions/ansible-test)
  - [Ansible Content Actions](https://github.com/ansible/ansible-content-actions/)

- If you want to learn community best practices related to collection development and maintenance, see the [Ansible community package collection requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html).

## Contributing to this repository

There are a lot of good things we could recommend that partners do to improve the quality of their collections,
but let's deliberately limit this repository's content to only what is **required**.
