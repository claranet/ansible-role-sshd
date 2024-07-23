#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_ssh_config_key_absent(host):
    sshd_config = host.file(f"/etc/ssh/sshd_config")
    assert sshd_config.exists
    assert sshd_config.contains("PermitRootLogin")
