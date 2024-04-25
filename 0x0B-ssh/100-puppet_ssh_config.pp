#!/usr/bin/env bash
#configure using puppet

file { 'etc/ssh/ssh_config':
  ensure => present,

content =>"
  #SSH client configuration
  host*
  IdentityFile ~/.ssh/school
  PasswordAuthentification no

}
