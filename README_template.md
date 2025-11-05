# Title of Collection

> The collection title should indicate, at a high level, what the collection is for.

> [!WARNING]
> To be correctly rendered on Automation Hub, all links in the README must be full URLs, not GitHub relative links

## Description

> In this section, give a high-level description of the collection including information about what the collection contains, why it is relevant, who should use it, and what it allows the user to do. This section is often referenced in marketing materials, so be sure to highlight any benefits of the collection and its purpose.

## Requirements

This section must list the required minimum versions of Ansible and Python, and any Python or external collection dependencies. Include additional information on other prerequisite tasks needed, if applicable.

## Installation

> This section must not include details about installing Ansible or ansible-core as that is installed as part of the AAP installation and execution environments. This section should focus on installing the collection from automation hub and must not include references to installing from GitHub.

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:

```
ansible-galaxy collection install NAMESPACE.COLLECTION_NAME
```

You can also include it in a requirements.yml file and install it with ansible-galaxy collection install -r requirements.yml, using the format:

```yaml
collections:
  - name: NAMESPACE.COLLECTION_NAME
```

To upgrade the collection to the latest available version, run the following command:

```
ansible-galaxy collection install NAMESPACE.COLLECTION_NAME --upgrade
```

You can also install a specific version of the collection. Use the following syntax to install version 1.0.0:

```
ansible-galaxy collection install NAMESPACE.COLLECTION_NAME:==1.0.0
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

> In addition to the above boilerplate, this section should include any additional details specific to your collection, and what to expect at each step and after installation. Be sure to include any information that supports the installation process, such as information about authentication and credentialing. 

## Use cases

> This section should outline in detail 3-5 common use cases for the collection. These should be informative examples of how the collection has been used, or how you’d like to see it be used. 

## Testing

> This section should include information on how the collection was tested and how it performed. Include information on what environments it’s been tested against, and any known exceptions or workarounds necessary for its use.

## Support

> This section should include information about what is supported and how to get support for the collection. This can include supported versions of the collection, how to submit a support request, and any other information about how to get additional assistance. We recommend the following text for certified content only:

As Red Hat Ansible Certified Content, this collection is entitled to support through the Ansible Automation Platform (AAP) using the **Create issue** button on the top right corner. If a support case cannot be opened with Red Hat and the collection has been obtained either from Galaxy or GitHub, there may community help available on the [Ansible Forum](https://forum.ansible.com/).

## Release notes and roadmap

> Collections must link to their release notes or changelog. Collections that have a public roadmap available should also link to that. All links must be full URLs, not GitHub relative links. Private repositories can include this information in their README file, or include the file in the collection tarball. Collections can optionally add a release note or changelog file to the docs/ directory as simplified markdown to display this information in automation hub. The [antsibull-changelog](https://ansible.readthedocs.io/projects/antsibull-changelog/) tool provides a convenient way to generate a changelog.

## License Information

> Link to the license that the collection is published under. All links must be full URLs, not GitHub relative links. For private repositories, mention the license used in this README and that the user can find the license included in the downloaded collection.

## Contributing (Optional)

> If your interested in community involvement and contributions to your collection, you might be interested in adding the following sections from the [Community-recommended README template](https://github.com/ansible-collections/collection_template):
  - [Communication](https://github.com/ansible-collections/collection_template#communication)
  - [Code of Conduct](https://github.com/ansible-collections/collection_template#code-of-conduct)
  - [Contributing to this collection](https://github.com/ansible-collections/collection_template#contributing-to-this-collection)
  - [Collection maintenance](https://github.com/ansible-collections/collection_template#collection-maintenance)
  - [Governance](https://github.com/ansible-collections/collection_template#governance)
