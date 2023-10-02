# custom HTTP header response with puppet
#
exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'present',
}

~> file { '/etc/nginx/nginx.conf':
  ensure  => 'file',
  content => "http {\n\tadd_header X-Served-By \"\${hostname}\";\n}",
}

~> exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {\n\tlisten 80;\n\tserver_name _;\n\tlocation / {\n\t\treturn 404;\n\t}\n\tlocation /redirect_me {\n\t\treturn 301 https://www.github.com/Cofucan;\n\t}\n\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\troot /var/www/html/;\n\t\tinternal;\n\t}\n}",
}

~> exec { 'reload_nginx':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
}

