# Collection certification onboarding

This repository aims to provide a clear set of instructions and content to help Red Hat partners:

- onboard their collections as [certified content on Ansible Automation Hub](https://connect.redhat.com/sites/default/files/2025-04/V28_Ansible_Certification_Policy_Guide_2025.pdf)
- reduce the probability of a collection version upload rejection


## Contributing to this repository

There are a lot of good things we could recommend partners to do to improve the quality of their collections,
but let's deliberately limit this repository's content to only what is **required**.

## Process

Before uploading a tarball of your collection to Automation Hub:

- Consult the [Ansible Certification Workflow Guide](https://connect.redhat.com/sites/default/files/2025-06/Ansible-Certification-Workflow-Guide202506.pdf) to ensure the collection meets the requirements listed in STEPS 5-7.

  - TBD: Add README template link (add a file to this repo)
  - TBD: Add a LICENSE file link (add a file to this repo)

- Make sure the collection passes Galaxy-importer checks on GitHub:

  - Copy the [Ansible collection certification GitHub Actions workflow](https://github.com/ansible-collections/certification/blob/main/.github/workflows/cert-tests.yml) to the `.github/workflows` directory of your collection repository.
  - Check the `Actions` tab on GitHub UI to make sure the workflow is running.
  - Fix all the failures if any. TBD ERRORS THAT CANNOT BE IGNORED LINK

    - If you collection ignores some errors by using `ignore-*.txt` files, make sure there are entries of [allowed types](https://ansible.readthedocs.io/projects/lint/rules/sanity/) only.

  - Keep a list of `ansible-core` versions in the `Sanity` job of the workflow updated when new versions of `ansible-core` come out:

   - Subscribe to the [news-for-maintainers](https://forum.ansible.com/tag/news-for-maintainers) tag on the Ansible Forum by clicking the bell button in the upper-right corner to get notified about new `ansible-core` versions available for testing.
   - Check out the [ansible-core support matrix](https://docs.ansible.com/ansible/devel/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix) periodically to remove EOL versions of `ansible-core` from your workflow's test matrix that your collection does not support.

- Ensure the collection tarball you upload contains a changelog with an entry for the version being uploaded.

  - We recommend using the [antsibull-changelog](https://ansible.readthedocs.io/projects/antsibull-changelog/) tool for changelog generation.

## Optional

- If you want to cover your collection with other kinds of tests (for example, unit and/or integration) to ensure your code stability, you can use the following resources:

  - [Ansible Nox](https://ansible.readthedocs.io/projects/antsibull-nox/introduction/)
  - [Ansible Test GitHub Actions](https://github.com/marketplace/actions/ansible-test)
  - [Ansible Content Actions](https://github.com/ansible/ansible-content-actions/)

- If you want to learn community best practices related to collection development and maintenance, see the [Ansible community package collection requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html).
