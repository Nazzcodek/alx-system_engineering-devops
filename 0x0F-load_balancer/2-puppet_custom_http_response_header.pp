# custom HTTP header response with puppet

# install nginx
package { 'nginx':
  ensure => 'installed',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
        listen 80;
        listen [::]:80 default_server;
        add_header X-Served-By $::hostname;
        root /var/www/html;
        index index.html index.html index.htm index.nginx-debian.html;

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }

        error_page 404 /404.html;
        location = /404.html {
                root /var/www/html/;
                internal;
        }
  }",
  require => package['nginx'],
}

service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => [File['/etc/nginx/sites-available/default']],
}
