# creates a file with content in tmp folder
file { '/tmp/holberton':
  ensure  => 'file',
  mode    => '0774',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  }
