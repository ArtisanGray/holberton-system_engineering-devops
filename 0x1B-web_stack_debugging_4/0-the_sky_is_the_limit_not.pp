# changes the number of maximum processes
file { '/etc/nginx/nginx.conf' :
  ensure => present,
}
exec { 'update worker_processes' :
  command  => 'cat /etc/nginx/nginx.conf | sed \'s/worker_processes 4/worker_processes 1024/g\' | sudo tee /etc/nginx/nginx.conf ; service nginx restart',
  provider => 'shell',
}
