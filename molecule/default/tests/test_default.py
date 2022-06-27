#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_pkg(host):
    pkg = host.package("openssh-server")
    assert pkg.is_installed


def test_svc(host):
    if host.system_info.distribution in ['debian', 'ubuntu']:
      svc = host.service("ssh")
    else:
      svc = host.service("sshd")
    assert svc.is_running
    assert svc.is_enabled
    
def test_config_file(host):
    assert host.run_test("sshd -t")

def test_listen_ssh(host):
    assert host.socket("tcp://22").is_listening