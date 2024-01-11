# This manifests creates a file with some attributes

file {'/tmp/school':
    ensure  => 'present',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet'
}
