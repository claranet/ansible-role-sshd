# Ansible role - sshd
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-sshd?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-sshd?style=flat-square)](https://github.com/claranet/ansible-role-sshd/releases)
[![Status](https://img.shields.io/github/workflow/status/claranet/ansible-role-sshd/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-sshd/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/sshd)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure SSHd. Manages Certificate Authority

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.sshd
```

## :gear: Role variables

Variable                              | Default value                                                           | Description
--------------------------------------|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------
sshd_trustedusercakeys_content        | **empty**                                                               | Content of the Trusted User Keys Certificate Authority
sshd_principals                       | **{}**                                                                  | Content of [AuthorizedPrincipalsFile](https://man.openbsd.org/sshd_config#AuthorizedPrincipalsFile)
sshd_principals_list_merge            | **append**                                                              | How `sshd_principals` and `sshd_principals_default` are combined.
sshd_config_template                  | **sshd_config.j2**                                                      | Default template name for /etc/ssh/sshd_config
sshd_config_chmod                     | **444**                                                                 | Default mode for /etc/ssh/sshd_config
sshd_config                           | **{}**                                                                  | ssh config options
sshd_config_list_merge                | **append**                                                              | How `sshd_config` and `sshd_default_default` are combined.
sshd_config_list_separated_by_comma   | **[]**                                                                  | sshd_config options separated by coma
sshd_config_list_separated_by_newline | **[]**                                                                  | sshd_config options multi line splited
sshd_yes_i_know_what_i_am_doing       | **false**                                                               | by-pass check AuthorizedPrincipalsFile ends
sshd_config_d_include                 | **false**                                                               | Enable "Include config.d/*"
sshd_banner_template                  | https://raw.githubusercontent.com/claranet/motd/master/banner           | SSH banner template<br>Can be a URL, a local template or `null`
sshd_banner_template_prepend          | **empty**                                                               | Prepend raw content to `sshd_banner_template`
sshd_banner_template_append           | See [defaults/main/main.yml](defaults/main/main.yml)                    | Append raw content to `sshd_banner_template`
sshd_banner_template_username         | **empty**                                                               | Used when `sshd_banner_template` is an URL
sshd_banner_template_password         | **empty**                                                               | Used when `sshd_banner_template` is an URL

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  vars:
    sshd_trustedusercakeys_content: "{{ lookup('community.hashi_vault.hashi_vault', 'secret=secret/public_key') }}"
    sshd_principals_default:
      admin:
        - adm

  roles:
    - claranet.sshd
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
