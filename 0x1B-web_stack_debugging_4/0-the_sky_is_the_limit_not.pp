# Nginx sever lrequest limit increment

# change the ULIMIT  value in /etc/default/nginx
exec {'ulimit-value':
  command => 'sed -i "s/15/5089/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
service { 'nginx-restart':
  ensure  => 'running',
  name    => 'nginx',
  require => Exec['ulimit-value'],
}
