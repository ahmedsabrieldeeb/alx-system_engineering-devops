#!/usr/bin/env bash
# configuration automation manifest

file { 'school_config':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config.d/school_config.conf',
  content => "Host school_server\n\
    HostName 54.234.64.96\n\
    User ubuntu\n\
    IdentityFile ~/.ssh/school\n\
    PasswordAuthentication no\n",
}

file_line { 'no_password':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config.d/school_config.conf',
  line    => '       PasswordAuthentication no',
  require => File['school_config'],
}