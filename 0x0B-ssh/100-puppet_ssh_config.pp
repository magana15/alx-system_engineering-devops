#!/usr/bin/env bash
#configure using puppet
file { '/etc/ssh/ssh_config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "
# SSH client configuration
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
