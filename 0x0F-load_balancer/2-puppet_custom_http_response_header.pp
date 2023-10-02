# custom HTTP header response with puppet

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present',
}

file_line { 'http_header':
  path => '/etc/nginx/nginx.conf',
  line => "add_header X-Served-By '${hostname}';",
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['http_header'],
}
