# fixes a typo within a configuration file.
file { '/var/www/html/wp-settings.php' :
  ensure => present,
}
exec { 'replaces typo' :
  command  => 'cat /var/www/html/wp-settings.php | sed \'s/phpp/php/g\' | sudo tee /var/www/html/wp-settings.php',
  provider => 'shell',
}
