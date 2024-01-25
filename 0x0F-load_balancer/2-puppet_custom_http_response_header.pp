# configuration automation manifest

$hostname_parts = split($::hostname, '-')
$server_name = "${hostname_parts[1]}-${hostname_parts[2]}"

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80;

    add_header X-Served-By ${server_name};

    location / {
      root /var/www/html;
      index test.html;
    }

    location /redirect_me {
      rewrite ^/redirect_me/(.*)$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }

    error_page 404 /404.html;
    location = /404.html {
      root /var/www/html;
      internal;
    }
  }",
}

file { '/var/www/html/test.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => 'Ceci n\'est pas une page',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
