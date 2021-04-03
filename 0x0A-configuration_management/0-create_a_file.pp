# creates a file.
file { '/tmp/holberton':
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
