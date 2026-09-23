# Changelog

## [1.6.0](https://github.com/claranet/ansible-role-sshd/compare/ansible-role-sshd-1.5.0...ansible-role-sshd-1.6.0) (2026-09-23)


### Features

* add in pre-tasks install of openssh lib ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* add new keys to special variables ([0d1a966](https://github.com/claranet/ansible-role-sshd/commit/0d1a96626f7eca134710eed3bf9bd91754cf52c8))
* add schedule for run workflow each three months ([a45a54d](https://github.com/claranet/ansible-role-sshd/commit/a45a54dacc15e207d7f3e43dab6f99a29af17ae9))
* add user_ca_key scenario ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* allow actions to run all scenario ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* allow using 'null' to delete a key ([68ce057](https://github.com/claranet/ansible-role-sshd/commit/68ce057fff7f0e1c72c93c14f34aafa97a153fe8))
* **ci:** add ubuntu 24.04 in test workflow ([19c92f5](https://github.com/claranet/ansible-role-sshd/commit/19c92f540b9c41ff80932e25a42d1f4150390e3a))
* defaults for Oracle Linux 9 ([6fcf322](https://github.com/claranet/ansible-role-sshd/commit/6fcf322346dfd993d58aad7e34b3db36d1255274))
* load ansible callback for show scenario execution time ([f09be11](https://github.com/claranet/ansible-role-sshd/commit/f09be11882631544ae8d35c78dffddbd11d00e1e))
* populate trusted ca key content with template ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* upgrade molecule to v5 ([403b956](https://github.com/claranet/ansible-role-sshd/commit/403b956bed70d82fabbbd70bdbc2f1c291b66999))
* upgrade to molecule v5 ([5426076](https://github.com/claranet/ansible-role-sshd/commit/54260761d49bb8605ba7a8adc1a670d09b3bbe9d))


### Bug Fixes

* 'is not none' instead of 'is string' ([95f7de4](https://github.com/claranet/ansible-role-sshd/commit/95f7de48cc8f5a3a22976816c62803dfee128530))
* add sshd config for ubuntu noble ([19d0e9a](https://github.com/claranet/ansible-role-sshd/commit/19d0e9a8236e35efe888cc1ad0cdac4abf8029f8))
* ansible lint option on verifier deprecated ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* ansible lint task must begin with upper case letter ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* ansible_version type. replace float by string ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* ansible-lint jinja spacing ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* change file config for fedora to redhat ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* defne new ansible-lint rules ([535c194](https://github.com/claranet/ansible-role-sshd/commit/535c194e57149a4d7fb1e5e8f8ca6d9c00e505ce))
* idempotency with replacing copy module by template and ansible-lint jinja spacing ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* invert assert condition ([2b83bf3](https://github.com/claranet/ansible-role-sshd/commit/2b83bf3bd0f2166c4eefc351e3c18c1a0dcd5513))
* **redhat:** loop path ([d7417d5](https://github.com/claranet/ansible-role-sshd/commit/d7417d503aa97563285fa66415d06801d0e74cf5))
* remove dsa host key ([56c9981](https://github.com/claranet/ansible-role-sshd/commit/56c9981c644624657fd0754a5032ca6cca2aff27))
* remove firewalld install for redhat family ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* rename file, change to redhat ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* trusted_ca's scenario idempotent ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* update instance name ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* upgrade runs-on image ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* use ansible_facts instead of injected fact variables ([92c37d0](https://github.com/claranet/ansible-role-sshd/commit/92c37d003ed76b0f775614ad8fa454a68ce6686d))
* use ansible_facts instead of injected fact variables ([cc406d1](https://github.com/claranet/ansible-role-sshd/commit/cc406d176b8ad83a18950aa6d855c6d24359b3b8))
* use only admin as principals ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))
* use only admin user as principal ([0f57777](https://github.com/claranet/ansible-role-sshd/commit/0f57777b582670dd5a5b5fe898c8ccc3a9bd951c))


### Documentation

* update testing badge status ([0a6fe6d](https://github.com/claranet/ansible-role-sshd/commit/0a6fe6dec05f47211483035d24e8bd700e1157ae))


### Miscellaneous Chores

* add in worflow tests on ubuntu 24 ([b255062](https://github.com/claranet/ansible-role-sshd/commit/b2550629e3c83a115dc0836d0b20ceb6585e6e71))


### Tests

* add RHEL 9 tests ([891b8c6](https://github.com/claranet/ansible-role-sshd/commit/891b8c68eeab75c51f0a01506438ea0e5d6771ab))


### Continuous Integration

* add release-please for automated releases ([5ba0ac2](https://github.com/claranet/ansible-role-sshd/commit/5ba0ac2b5ebebf406df6322e62f7d03600ed001c))
* add release-please for automated releases ([790ad44](https://github.com/claranet/ansible-role-sshd/commit/790ad44a817b95136f5d6822c966a2d1a152a96f))
